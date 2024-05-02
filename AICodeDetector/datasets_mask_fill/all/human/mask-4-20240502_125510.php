

use <extra_id_0> Symfony以外の場合
$client = HttpClient::create();
$response = $client->request('GET', 'https://qiita.com/api/v2/items?query=Symfony', [
    'headers' => [
    <extra_id_1>   'Authorization' => 'Bear: ......'
    ],
]);

// ステータスコード
$statusCode = $response->getStatusCode();
// レスポンスヘッダ
$headers = $response->getHeaders();
// レスポンスを文字列で
$response->getContent();
// レスポンスを配列で
$response->toArray();

// Symfonyの場合
class SomeService
{
 <extra_id_2>  public function __construct(private <extra_id_3> $client)
    {
    }
 <extra_id_4>  
    public function someMethod()
  <extra_id_5> {
  <extra_id_6>     $response = $client->request('GET', 'https://qiita.com/api/v2/items?query=Symfony', [
        <extra_id_7>   'headers' => [
                <extra_id_8> 'Bear: ......'
           