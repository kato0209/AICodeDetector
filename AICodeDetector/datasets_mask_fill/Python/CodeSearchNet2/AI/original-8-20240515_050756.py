
    logging.info('Deleting all records related to the specified dag')
    session = settings.Session()
    qry = session.query(DagRun).filter(
        DagRun.dag_id == args.dag_id).delete()
    session.commit()
    session.close()
    logging.info('Dag deleted.')


def pool_full(args):
    session = settings.Session()
    qry = session.query(Pool).filter(Pool.pool == args.pool).first()
    if not qry:
        session.close()
        logging.warning('Could not find pool %s