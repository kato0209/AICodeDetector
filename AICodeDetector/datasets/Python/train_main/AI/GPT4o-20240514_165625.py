
    """
    Construct the Opsgenie JSON payload. All relevant parameters are combined here
    to a valid Opsgenie JSON payload.

    :return: Opsgenie payload (dict) to send
    """
    payload = {
        "message": self.message,
        "alias": self.alias,
        "description": self.description,
        "responders": self.responders,
        "visibleTo": self.visible_to,
        "actions": self.actions,
        "tags": self.tags,
        "details": self.details,
        "entity": self.entity,
       