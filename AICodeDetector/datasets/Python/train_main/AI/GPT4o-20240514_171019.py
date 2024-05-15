

class Component:
        self.params = params
        self.mode = mode
        self.serialized = serialized
        self.extra_args = kwargs

    @classmethod
        return cls(params, mode, serialized, **kwargs)
