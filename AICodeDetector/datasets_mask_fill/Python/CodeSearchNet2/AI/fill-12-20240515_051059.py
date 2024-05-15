if not any([ti.sla for ti in dag.tasks]): self.log.info( "Skipping SLA check for %s because no tasks in DAG have SLAs", dag ) return( dag )
    elif TI = self.queue.get(): self.doTask( TI )
else: self.log.debug( "No SLA check for %s", dag )
    if sq = ( session