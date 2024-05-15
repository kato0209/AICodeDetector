

class Pod:
        self.name = name
        self.state = 'Pending'
        self.logs = ''

        # Simulate pod starting
        time.sleep(2)
        self.state = 'Running'

        # Simulate waiting for pod to complete
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.state == 'Running':
                time.sleep(2)  # Simulate some running time
               