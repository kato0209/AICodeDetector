logging.info('Deleting all <extra_id_0> <extra_id_1> to the specified dag') session = settings.Session() <extra_id_2> = session.query(DagRun).filter( DagRun.dag_id == args.dag_id).delete() session.commit() session.close() logging.info('Dag deleted.') def pool_full(args): session = settings.Session() qry = session.query(Pool).filter(Pool.pool == args.pool).first() if not qry: session.close() logging.warning('Could not find pool %s