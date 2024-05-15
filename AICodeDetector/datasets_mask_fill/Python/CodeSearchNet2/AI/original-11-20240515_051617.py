
        self.word_embeddings = tf.get_variable(
            name='word_embeddings',
            shape=[self.config.vocab_size, self.config.embedding_size],
            initializer=self.initializer)
        self.word_embeddings = tf.nn.l2_normalize(self.word_embeddings, 1)
        self.word_embeddings = tf.nn.dropout(self.word_embeddings, self.config.keep_prob)
        self.word_embeddings = tf.nn.l2_normalize(self.word_embeddings, 1)
        self.word_embeddings =