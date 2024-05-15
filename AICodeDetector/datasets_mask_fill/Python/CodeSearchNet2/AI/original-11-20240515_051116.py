
        for col, col_type in zip(schema, col_type_dict):
            col = self._to_java_column(col)
            try:
                v = float(row[col])
            except ValueError:
                v = row[col]
            # TODO: handle Decimals, need to handle it as Decimal type
            col_type = self._to_java_type(col_type)
   