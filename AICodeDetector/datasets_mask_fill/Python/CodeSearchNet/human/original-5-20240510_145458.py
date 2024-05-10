
        payload = {}

        if self.username:
            payload['username'] = self.username
        if self.avatar_url:
            payload['avatar_url'] = self.avatar_url

        payload['tts'] = self.tts

        if len(self.message) <= 2000:
            payload['content'] = self.message
        else:
            raise AirflowException('Discord message length must be 2000 or fewer '
       