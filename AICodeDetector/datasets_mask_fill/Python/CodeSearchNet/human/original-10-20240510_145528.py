

        BJ = jobs.BaseJob
        payload = {}
        scheduler_health_check_threshold = timedelta(seconds=conf.getint('scheduler',
                                                                         'scheduler_health_check_threshold'
                        