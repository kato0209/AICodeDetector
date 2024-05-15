
    """Returns json compatible state of the ButtonsFrame instance.

    Returns json compatible state of the ButtonsFrame instance including
    all nested buttons.

    Returns:
        control_json: Json representation of ButtonsFrame state.
    """
    control_json = {
        'buttons': [button.json() for button in self.buttons]
    }
    return control_json
