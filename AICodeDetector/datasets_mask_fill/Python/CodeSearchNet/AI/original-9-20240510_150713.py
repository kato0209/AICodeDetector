
        if isinstance(x, RDD):
            return x.map(lambda lp: self.evaluate(lp, y, batch_size))

        if not isinstance(x, RDD):
            raise TypeError("Expected x to be RDD, but got %s." % type(x))
        if batch_size is None:
            batch_size = len(x)

        if self._distribution:
            batch_size = min(batch_size, len(self._distribution))

        def func(rdd):
         