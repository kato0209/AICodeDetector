
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        request = args[0]
        try:
            return func(request, *args[1:], **kwargs)
        except Exception as exc:
            if self.system.DEBUG:
                msg = 'Error saving lineage to XCom for user_id=%d.'+ \
                      'Error: %s' % (self.user_id, str(exc))
        