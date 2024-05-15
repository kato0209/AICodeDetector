
        if parameters is None:
            parameters = {}
        if hql is None:
            hql = "SELECT * FROM %s" % self.db_name
        hql += " WHERE %s" % self.db_name
        hql += " ORDER BY %s" % self.db_name
        hql += " LIMIT %s" % self.db_name
        hql += " OFFSET %s" % self.db_name
        hql += ";"
     