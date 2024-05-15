
        if event_name == "after_validation":
            if data['impatience'] > self._learning_rate_last_impatience:
                self._learning_rate_cur_impatience += 1
            else:
                self._learning_rate_cur_impatience = 0

            self._learning_rate_last_impatience = data['impatience']

            if (self._learning_rate_drop_patience is not None) and\
                    (self._learning_rate_cur_impatience >=
 