
        if self.pid > 0:
            print("Killing JVM with PID {}".format(self.pid))
            try:
                self.child.terminate()
                self.child.wait()
            except OSError:
                pass
            self.pid = -1