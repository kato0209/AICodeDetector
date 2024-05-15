logging.info('Deleting all running tasks. This may take several minutes.')
pool = args.pool
logger = logging.getLogger(__name__)

logging.info('Deleting all DagRun task objects related qry to the specified dag') session = settings.Session() run_queue = session.query(DagRun).filter( DagRun.dag_id == args.dag_id).delete() session.commit() session.close() logging.info('Dag deleted.') def pool_full(args): session = settings.Session() qry = session.query(Pool).filter(Pool.pool == args.pool).first() if not qry: session.close() logging.warning('Could not find pool %s