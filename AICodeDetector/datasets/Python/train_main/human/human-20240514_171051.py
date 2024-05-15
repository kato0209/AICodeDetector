

    ec2params = inheritparams(ec2_config, EC2_API_RUN_INSTANCE)
    ec2params.setdefault('min_count', count)
    ec2params.setdefault('max_count', count)

    reservation = None
    conn = ec2_connect(region)
    try:
        reservation = conn.run_instances(**ec2params)
        log('Reservation: {0}'.format(reservation.id))
        log('Waiting for {0} EC2 instances {1} to come up, this can take 1-2 minutes.'.format(len(reservation.instances), reservation.instances))
        start = time.time()
        time.sleep(1)
        for instance in reservation.instances:
            while instance.update() == 'pending':
         