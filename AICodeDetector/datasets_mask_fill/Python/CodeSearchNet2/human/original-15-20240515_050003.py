
    backend = _get_backend()

    @wraps(func)
    def wrapper(self, context, *args, **kwargs):
        self.log.debug("Backend: %s, Lineage called with inlets: %s, outlets: %s",
                       backend, self.inlets, self.outlets)
        ret_val = func(self, context, *args, **kwargs)

        outlets = [x.as_dict() for x in self.outlets]
        inlets = [x.as_dict() for x in self.inlets]

        if len(self.outlets) > 0:
            self.xcom_push(context,
    