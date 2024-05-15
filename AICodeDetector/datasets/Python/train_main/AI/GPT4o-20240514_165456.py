

    """ Helper method that binds parameters to a SQL query. """
    if isinstance(parameters, dict):
        for key, value in parameters.items():
            placeholder = f":{key}"
            if isinstance(value, str):
                value = f"'{value}'"
            operation = operation.replace(placeholder, str(value))
    elif isinstance(parameters, (list, tuple)):
        for value in parameters:
            placeholder = re.search(r'\?', operation)
            if placeholder:
                if isinstance(value, str):
                    value = f"'{value}'"
                operation = operation