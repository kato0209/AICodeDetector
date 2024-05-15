
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    if os.path.exists(DB_FILE_OLD):
        os.rename(DB_FILE_OLD, DB_FILE)
    if os.path.exists(DB_FILE_NEW):
        os.remove(DB_FILE_NEW)
    if os.path.exists(DB_FILE_OLD_OLD):
        os.rename(DB_FILE_OLD_OLD, DB_FILE_OLD)
    if os.path.exists(DB_FILE_NEW_OLD):
        os