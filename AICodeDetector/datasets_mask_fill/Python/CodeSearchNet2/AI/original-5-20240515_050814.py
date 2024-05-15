
        import pandas as pd
        import pandas.io.sql as psql
        import pandas.io.sql.sql as psql_pandas_sql

        if parameters is None:
            parameters = {}

        if self.sql_type == 'pandas':
            sql_str = self.sql
        else:
            sql_str = self.sql.replace('\n','')

        if self.sql_type == 'pandas-on-spark':
           