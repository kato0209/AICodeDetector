

    md5 = hashlib.md5()
    md5.update(upid.encode('utf-8'))
    digest = md5.digest()
    mimi = ''.join(f'{(digest[i] ^ digest[i + 8]):02x}' for i in range(8))
    return mimi
