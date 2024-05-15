
    """
    Create perm-vm if not exist and insert into FAB security model for all-dags.
    """

    session: Session = self.get_session()
    security_manager: AirflowSecurityManager = self.appbuilder.sm

    all_dags = session.query(DagModel).all()
    for dag in all_dags:
        view_menu