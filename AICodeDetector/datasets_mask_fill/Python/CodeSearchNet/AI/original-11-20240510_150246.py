
        local_loc = os.path.abspath(os.path.dirname(__file__))
        self.log.info("Setting up DAG file %s", local_loc)
        self.log.info("Making local session")
        session = settings.Session()
        orm_dag = session.query(
            DagModel).filter(DagModel.fileloc == local_loc).first()
        if not orm_dag:
            orm_dag = DagModel(fileloc=local_loc)
        orm_dag.fileloc = filename
        orm_dag.is_subdag = True
        session.