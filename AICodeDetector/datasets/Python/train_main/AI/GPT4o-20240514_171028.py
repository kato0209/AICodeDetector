
    """Processes Alexa requests from skill server and returns responses to Alexa.

    Args:
        request: Dict with Alexa request payload and metadata.
    Returns:
        result: Alexa formatted or error response.
    """
    try:
        request_type = request['request']['type']
        
        if request_type == 'LaunchRequest':
            return self._handle_launch_request(request)
        elif request_type == 'IntentRequest':
            return self._handle_intent_request(request)
        elif request_type == 'SessionEndedRequest':
            return self._handle_session_ended_request