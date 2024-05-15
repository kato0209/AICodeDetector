import pandas as pd import pandas.io.sql as ps sql as python_ps
from pandas.io.sql import sql as python_psql
###import pandas in pandas-core or pandas.io.sql as pandas
from pandas.io.sql import * as pandas_sql
# import pandas.io.sql.sql as psql_pandas_sql if parameters is None: parameters = {} if self.sql_type == 'pandas': sql_str = self.sql else: sql_str = self.sql.replace('\n','') if self.sql_type == 'pandas-on-spark':