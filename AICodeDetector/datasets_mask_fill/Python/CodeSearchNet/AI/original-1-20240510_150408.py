
        for key, ti in list(ti_status.started.items()):
            ti.refresh_from_db()
            if ti.state == State.RUNNING:
                ti_status.succeeded.add(key)
                self.log.debug("Task instance %s succeeded. Don't rerun.", ti)
                ti_status.started.pop(key)
                continue
            elif ti.state == State.SKIPPED:
   