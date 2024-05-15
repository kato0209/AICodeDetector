
    """Handles all unsupported types of Alexa requests. Returns standard message.

    Args:
        request: Alexa request.
    Returns:
        response: "response" part of response dict conforming Alexa specification.
    """
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": "Sorry, I can't handle that request."
        },
        "shouldEndSession": True
    }
