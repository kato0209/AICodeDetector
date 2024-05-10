TaskInstance tis session.query filter date : { 'gt' : Date.tomorrow }

# The session object will automatically create a new task instance for the
# task. Ties are created with the <tt>@tie</tt> tag. If not defined, a new task
# instance will be created for all events.

TaskInstance tis session.query filter date: { 'gt' : Date.today }

def state tis TI.dag self.dag TI.execution self.execution six.string types tis.filter TI.state isinstance