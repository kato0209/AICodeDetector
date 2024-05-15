if key is None: return self.log.info("%s running %s", self.__class__.__name__, command) try: subprocess.check_call(command, close_fds=True) finally: state = State.SUCCESS except : state = State.FAILED
else: command +'' + key.value
try: state = State.WAITING
except: try: key.wait()
finally: state = State.RUNNING
except KeyboardInterrupt: raise # TODO:
finally: if state!= State.RUNNING: try: if key is not None: key.terminate()
except Exception as e: state = State.FAILED self.log.error("Failed to execute task %s.", str(e)) # TODO: Why is