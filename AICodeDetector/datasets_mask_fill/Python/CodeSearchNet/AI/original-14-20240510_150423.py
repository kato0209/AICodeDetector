
        return [s for s in cls if not s.finished]

    def __init__(self, state, task_id, runnable):
        self.state = state
        self.task_id = task_id
        self.runnable = runnable
        self.started = False
        self.finished = False
        self.result = None
        self.exception = None
        self.traceback = None

    def __repr__(self):
        return "<Task %s (%s)>" % (self.task_id, self.state)

    def