
        X = self._transform_batch(data)
        objects_number, lengths = len(X[0]), [len(elem) for elem in data[0]]
        Y = self.model_.predict_on_batch(X)
        labels = np.argmax(Y, axis=-1)
        answer: List[List[str]] = [None] * objects_number
        for i, (elem, length) in enumerate(zip(labels, lengths)):
            elem = elem[:length]
            answer[i] = elem if return_indexes else self.tags.idxs2toks(elem)
        return answer