
    assert algo is not None, '"algo" parameter is null'
    # Allow this now: assert training_frame is not None, '"training_frame" parameter is null'
    assert parameters is not None, '"parameters" parameter is null'

    model_builders = self.model_builders(timeoutSecs=timeoutSecs)
    assert model_builders is not None, "/ModelBuilders REST call failed"
    assert algo in model_builders['model_builders']
    builder = model_builders['model_builders'][algo]
    
    # TODO: test this assert, I don't think this is working. . .
    if training_frame is not None:
        frames = self.frames(key=training_frame)
        assert frames is not None, "/Frames/{0} REST call failed".format(training_frame)

  