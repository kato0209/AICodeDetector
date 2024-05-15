
        if not self._conn:
            self._conn = VideoIntelligenceServiceClient(credentials=self._get_credentials())
        return self._conn