
    if tags is None:
        tags = {}
    reservation = ec2_conn.run_instances(
        image_id=ec2_config['image_id'],
        count=count,
        key_name=ec2_config['key_name'],
        security_groups=[ec2_config['security_group']],
        instance_type=ec2_config['instance_type'],
        placement=region,
        user_data=ec2_config['user_data'],
        instance_profile_name=ec2_config['instance_profile_name'],
        instance_profile_arn=ec