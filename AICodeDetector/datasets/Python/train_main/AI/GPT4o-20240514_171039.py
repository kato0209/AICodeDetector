

class H2OImporter:
        self.h2o_ip = h2o_ip
        self.h2o_port = h2o_port

        url = f"http://{self.h2o_ip}:{self.h2o_port}/3/ImportFiles"
        params = {'path': path}
        start_time = time.time()
        
        while time.time() - start_time < timeoutSecs:
            response = requests