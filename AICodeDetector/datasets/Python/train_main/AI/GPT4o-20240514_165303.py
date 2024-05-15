
    """
    Converts a user type to RECORD that contains n fields, where n is the
    number of attributes. Each element in the user type class will be converted to its
    corresponding data type in BQ.
    """

        type_map = {
            int: 'INTEGER',
            float: 'FLOAT',
            str: 'STRING',
            bool: 'BOOLEAN',
            dict: 'RECORD',
            list: 'RECORD'
        }
        return type_map.get(py