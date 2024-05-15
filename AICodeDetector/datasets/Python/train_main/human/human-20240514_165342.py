
        if dep_context.ignore_in_reschedule_period:
            yield self._passing_status(
                reason="The context specified that being in a reschedule period was "
                       "permitted.")
            return

        if ti.state not in self.RESCHEDULEABLE_STATES:
            yield self._passing_status(
                reason="The task instance is