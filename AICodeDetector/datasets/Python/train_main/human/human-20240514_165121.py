
        while True:
            loop_start_time = time.time()

            if self._signal_conn.poll():
                agent_signal = self._signal_conn.recv()
                if agent_signal == DagParsingSignal.TERMINATE_MANAGER:
                    self.terminate()
                    break
              