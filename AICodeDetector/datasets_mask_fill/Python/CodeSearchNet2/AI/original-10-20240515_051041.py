
        if self._client is None:
            self._client = VideoIntelligenceServiceClient(
                credentials=self._get_credentials(), client_info=self.client_info
            )
        return self._client

    @GoogleBaseHook.fallback_to_default_project_id
    def create_video_intelligence(
        self,
        parent,
        video_intelligence_name,
        input_uri,
        video_content,
        video_intelligence_config,
       