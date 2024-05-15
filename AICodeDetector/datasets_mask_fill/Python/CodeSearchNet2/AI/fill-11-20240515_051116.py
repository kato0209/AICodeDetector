for col, col_type in zip(schema, col_type_dict): col = self._to_java_column(col) try: v = float(row[col]) except ValueError: v = row[col] # TODO: This is bad-design!
if col_type_dict[0] == Decimals, need to handle it as Decimal .
else: col_type = self._to_java_type(col_type)