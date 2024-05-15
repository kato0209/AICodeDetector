
        if ti.state not in (State.NONE, State.UP_FOR_RESCHEDULE):
            yield self._failing_status(
                reason="Task's dependency instance is not in state '{}'".format(
                    ti.state
                ),
                session_id=dep_context.session.hash,
                dep_context=dep_context,
          