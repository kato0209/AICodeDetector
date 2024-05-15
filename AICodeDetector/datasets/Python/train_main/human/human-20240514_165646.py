
        client = self.get_conn()
        self.log.info("Synthesizing input: %s" % input_data)
        return client.synthesize_speech(
            input_=input_data, voice=voice, audio_config=audio_config, retry=retry, timeout=timeout
        )