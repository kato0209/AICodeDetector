
    global _db_ctx
    if _db_ctx is not None:
        _db_ctx.close()
        _db_ctx = None
    _db_ctx = None
    _db_ctx = None


def close_db(db_name):
    global _db_ctx
    if _db_ctx is not None:
        _db_ctx.close()
        _db_ctx = None
    _db_ctx = None


def close_all():
    global _db_ctx
    if _db_ctx is not None:
        _db_ctx.close()
        _db