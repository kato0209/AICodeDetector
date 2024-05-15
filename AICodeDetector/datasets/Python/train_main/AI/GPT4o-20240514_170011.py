

    model = Inception3(**kwargs)
    if pretrained:
        state_dict = torch.hub.load_state_dict_from_url(
            'https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth',
            progress=True
        )
        model.load_state_dict(state_dict)
    return model
