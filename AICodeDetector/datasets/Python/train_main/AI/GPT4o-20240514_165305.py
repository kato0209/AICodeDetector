

    client = speech_v1.SpeechClient()
    
    if isinstance(config, dict):
        config = speech_v1.RecognitionConfig(**config)
    
    if isinstance(audio, dict):
        audio = speech_v1.RecognitionAudio(**audio)
    
    response = client.recognize(config=config, audio=audio, retry=retry, timeout=timeout)
    
    return response
