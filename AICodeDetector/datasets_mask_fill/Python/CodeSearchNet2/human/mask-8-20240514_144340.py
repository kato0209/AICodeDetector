log = LoggingMixin().log if args.yes or input( "This will <extra_id_0> all existing <extra_id_1> related to the specified DAG. " "Proceed? (y/n)").upper() == "Y": try: message = api_client.delete_dag(dag_id=args.dag_id) except IOError as err: log.error(err) raise AirflowException(err) log.info(message) else: