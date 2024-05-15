# this avoids a circular dependency from airflow.ti_deps.dep_context import later:
# if dep_context is None: dep_context = DepContext() if self.IGNOREABLE and dep_context.ignore_all_deps: dep_context = None
# return self._passing_status( reason="Context specified all dependencies should be ignored.") return if self.IS_TASK_DEP and dep_context.ignore_task_deps: