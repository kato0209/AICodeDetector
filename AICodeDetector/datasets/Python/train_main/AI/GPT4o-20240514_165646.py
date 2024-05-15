

    client = texttospeech_v1.TextToSpeechClient()

    if isinstance(input_data, dict):
        input_data = texttospeech_v1.SynthesisInput(**input_data)
    if isinstance(voice, dict):
        voice = texttospeech_v1.VoiceSelectionParams(**voice)
    if isinstance(audio_config, dict):
        audio_config = texttospeech_v1.AudioConfig(**audio_config)

    response