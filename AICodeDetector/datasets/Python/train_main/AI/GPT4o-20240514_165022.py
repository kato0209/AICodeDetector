

    with create_session() as session:
        session.query(DagModel).update({DagModel.is_paused: is_paused})
        session.commit()
