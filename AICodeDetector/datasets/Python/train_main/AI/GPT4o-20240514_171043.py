

class H2OCluster:
        self.base_url = base_url

        url = f"{self.base_url}/3/Frames/{key}"
        start_time = time.time()
        
        while time.time() - start_time < timeoutSecs:
            response = requests.delete(url, **kwargs)
            if response.status_code == 200:
                return True
            elif response.status_code == 404 and ignoreMissingKey:
                return False