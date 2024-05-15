

    ec2 = boto3.resource('ec2', region_name=region)
    
    instances = ec2.create_instances(
        MinCount=count,
        MaxCount=count,
        **ec2_config
    )
    
    if tags:
        for instance in instances:
            instance.create_tags(Tags=tags)
    
    if waitForSSH:
        for instance in instances:
            instance.wait_until_running()
            instance.reload()
            while True:
                try:
                    response = instance.describe_instance