

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
    
    conn.commit()
    conn.close()
