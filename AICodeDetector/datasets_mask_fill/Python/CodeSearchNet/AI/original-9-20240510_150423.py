
        if parameters is None:
            parameters = {}
        sql = sql.strip()
        if sql.lower().startswith("select"):
            sql, params = self.parse_select(sql, parameters)
        elif sql.lower().startswith("insert"):
            sql = self.parse_insert(sql, parameters)
        elif sql.lower().startswith("update"):
            sql = self.parse_update(sql, parameters)
        elif sql.lower().startswith("delete"):
          