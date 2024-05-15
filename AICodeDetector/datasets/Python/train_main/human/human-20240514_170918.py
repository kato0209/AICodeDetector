
        if self.word_dropout > 0.0:
            lstm_outputs = kl.Dropout(self.word_dropout)(word_outputs)
        else:
            lstm_outputs = word_outputs
        for j in range(self.word_lstm_layers-1):
            lstm_outputs = kl.Bidirectional(
                kl.LSTM(self.word_lstm_units[j], return_sequences=True,
                        dropout=self.lstm_dropout))(lstm_outputs)
        lstm_outputs = kl.Bidirectional(
    