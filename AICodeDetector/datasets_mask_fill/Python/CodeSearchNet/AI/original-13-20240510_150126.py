
        if dep_context is None:
            dep_context = DepContext()

        failed_dep_reasons = []
        if ti.state == State.SKIPPED:
            failed_dep_reasons.append('All dependencies are skipped.')

        if failed_dep_reasons:
            if self.ignore_all_deps or ti.state == State.FAILED:
                yield self._failing_status(
                    reason='The following tasks have