log.debug("Disposing DB connection pool (PID %s)", os.getpid()) <extra_id_0> engine global Session if Session: Session.remove() Session = None if engine: engine.dispose() engine = None