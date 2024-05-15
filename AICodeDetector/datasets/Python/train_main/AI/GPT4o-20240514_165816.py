

    @wraps(func)
    @provide_session
        result = func(*args, **kwargs)
        
        # Assuming lineage information is available in the function's return value
        lineage_info = result.get('lineage', {})
        
        # Save lineage to XCom
        task_instance = kwargs.get('ti')
        if task_instance:
            task_instance.xcom_push(key='lineage', value=lineage_info)
        
        # Send