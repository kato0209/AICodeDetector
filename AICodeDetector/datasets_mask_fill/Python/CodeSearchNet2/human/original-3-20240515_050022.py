
        session.expunge_all()

        enable_pickling = configuration.getboolean('core', 'enable_xcom_pickling')
        if enable_pickling:
            value = pickle.dumps(value)
        else:
            try:
                value = json.dumps(value).encode('UTF-8')
            except ValueError:
                log = LoggingMixin().log
                log.error("Could