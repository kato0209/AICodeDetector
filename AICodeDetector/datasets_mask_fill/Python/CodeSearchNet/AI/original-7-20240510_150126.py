
        if database_name is None:
            database_name = self.database_name
        if self.db_engine =='sqlite':
            self.db_engine = 'innodb'
        self.db_engine = 'innodb'
        self.db_name = database_name
        self.collection_name = collection_name
        self.db_connection = None
        self.db_cursor = None
        self.db_cursor.execute('DROP DATABASE IF EXISTS %s' % self.database_name)
        self.db_cursor.execute('DROP DATABASE IF EXISTS %s'