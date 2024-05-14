if not obj: obj = None d = {} for c in obj.__table__.columns: value = getattr(obj, c.name) if type(value) == datetime: value = value.isoformat() d[c.name] = value obj.__repr__ = lambda self: "{0}(obj={1}".format(type(self).__module__, str(obj)))

def select(obj):
    values = d