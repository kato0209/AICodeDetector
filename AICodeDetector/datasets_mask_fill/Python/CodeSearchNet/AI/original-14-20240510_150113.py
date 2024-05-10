
    session = settings.Session()
    dags = session.query(DagModel).filter(
        DagModel.dag_id.in_([dag.dag_id for dag in dags])
    ).all()
    for dag in dags:
        dag.is_paused = is_paused
    session.commit()


def create_user(username, password, superuser=False):
    from airflow.contrib.auth.backends.password_auth import PasswordUser
    return PasswordUser(username, password, superuser)


def create_superuser(username, password, superuser=False):
    from airflow