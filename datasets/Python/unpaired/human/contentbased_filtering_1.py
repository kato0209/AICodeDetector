import pandas as pd
import time
import redis
from flask import current_app
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def info(msg):
    current_app.logger.info(msg)


class ContentEngine(object):

    SIMKEY = 'p:smlr:%s'

    def __init__(self):
        self._r = redis.StrictRedis.from_url(current_app.config['REDIS_URL'])

    def train(self, data_source):
        start = time.time()
        ds = pd.read_csv(data_source)
        info("Training data ingested in %s seconds." % (time.time() - start))

        # redisから古い学習データを削除
        self._r.flushdb()

        start = time.time()
        self._train(ds)
        info("Engine trained in %s seconds." % (time.time() - start))

    def _train(self, ds):
        """
        エンジンに学習させる。

        各商品についてのユニグラム、バイグラム、トライグラムのTF-IDF行列を生成。
        'stop_words'パラメータにより、TF-IDFモジュールに
        'the'などの一般的な英単語を無視するよう指示。

        その後、Scikit Learnのlinear_kernel(今回はコサイン類似度と同じ)を用いて、
        全商品間の類似度を計算する。

        各商品の類似商品について繰り返した後、
        類似度の高い100件を保存。100件で止める理由は……
        あなたが本当に表示すべき似た商品はいくつですか？

        類似度とそのスコアはソート済みセットとしてredisに保存され、
        各セットが各商品に相当します。

        :param ds: description, idの2つのフィールドを持つpandasデータセット
        :return: なし
        """

        tf = TfidfVectorizer(analyzer='word',
                             ngram_range=(1, 3),
                             min_df=0,
                             stop_words='english')
        tfidf_matrix = tf.fit_transform(ds['description'])

        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
            similar_items = [(cosine_similarities[idx][i], ds['id'][i])
                             for i in similar_indices]

            # 一番目の商品はその商品自身なので削除。
            # 'sum' はタプルのリストから単一のタプルへの変換。
            # [(1,2), (3,4)] -> (1,2,3,4)
            flattened = sum(similar_items[1:], ())
            self._r.zadd(self.SIMKEY % row['id'], *flattened)

    def predict(self, item_id, num):
        """
        これ以上ないぐらいシンプル！
        類似する商品と、その'スコア'をredisから取得するだけです。

        :param item_id: string
        :param num: 類似する商品の、返すべき件数
        :return: [["19", 0.2203],["494", 0.1693], ...]のような、リストのリスト。
        各サブリストの1項目めがID、2項目めが類似度スコア。
        類似度スコアによって降順ソートされています。
        """

        return self._r.zrange(self.SIMKEY % item_id,
                              0,
                              num-1,
                              withscores=True,
                              desc=True)

content_engine = ContentEngine()
