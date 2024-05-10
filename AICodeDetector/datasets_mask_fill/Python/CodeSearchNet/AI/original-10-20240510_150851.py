
        if label.startswith("linear"):
            return cls.linear
        elif label.startswith("cosine"):
            return cls.cosine
        elif label.startswith("exponential"):
            return cls.exponential
        elif label.startswith("onecycle"):
            return cls.onecycle
        elif label.startswith("trapezoid"):
            return cls.trapezoid
        elif label.startswith("polynomial"):
        