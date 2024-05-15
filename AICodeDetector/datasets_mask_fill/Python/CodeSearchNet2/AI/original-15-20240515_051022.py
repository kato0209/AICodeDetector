
        schema_fields = []
        for field in cursor.description:
            field_name = field[0]
            field_type = field[1]
            field_mode = field[2]
            field_comment = field[3]
            field_type_name = field[4]
            field_mode_name = field[5]
            field_comment_name = field[6]
        