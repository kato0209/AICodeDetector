
        try:
            self.log("Checking if remote_log_location " + remote_log_location + " exists")
            response = self.storage_client.exists(remote_log_location)
            return response.success
        except CloudError as ex:
            self.log('Did not find remote log:'+ str(ex.message))
            return False

    def create_on_device(self):
        self.log("Creating on device")
        if not self.location_exists(self.remote_log_location):
      