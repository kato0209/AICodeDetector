log = LoggingMixin().log if logging.isDebug() else logging.getLogger()

if args.execute or input( "This will delete all existing records related to the specified DAG. " "Proceed? (y/n)").upper() == "Y": try: message = api_client.delete_dag(dag_id=args.dag_id) except IOError as err: log.error(err) raise AirflowException(err) log.info(message) else: