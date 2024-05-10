
        if self.state == State.RUNNING:
            self.end_date = datetime.now()
            self.state = State.SUCCESS
            session.merge(self)
        elif self.state == State.SUCCESS:
            self.end_date = datetime.now()
            self.state = State.RUNNING
            session.merge(self)
        session.commit()

    @provide_session
    def run(
        