DR = DagRun exec_date = func.cast(self.execution_date, DateTime) dr = session.query(DR).filter( DR.dag_id == self.dag_id, func.cast(DR.execution_date, DateTime) == exec_date, DR.run_id == self.run_id ).one() <extra_id_0> = dr.id self.state = <extra_id_1>