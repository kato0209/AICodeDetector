
    """Handles IntentRequest Alexa request.

    Args:
        request: Alexa request.
    Returns:
        response: "response" part of response dict conforming Alexa specification.
    """
    intent_name = request['request']['intent']['name']
    
    if intent_name == "HelloWorldIntent":
        response_text = "Hello, world!"
    else:
        response_text = "Sorry, I don't know that one."

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "