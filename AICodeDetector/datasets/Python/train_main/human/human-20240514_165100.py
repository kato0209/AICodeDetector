
        for dep_status in self.get_dep_statuses(ti, session, dep_context):
            if not dep_status.passed:
                yield dep_status.reason