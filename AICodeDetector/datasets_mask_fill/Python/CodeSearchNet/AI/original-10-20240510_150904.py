
        if not request:
            return self._error(
                "No Alexa request received from skill server")

        if not isinstance(request, dict):
            return self._error(
                "Request payload must be a dict")

        if not isinstance(request.get("intent"), dict):
            return self._error(
             