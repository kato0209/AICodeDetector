
    """
    Construct the Discord JSON payload. All relevant parameters are combined here
    to a valid Discord JSON payload.

    :return: Discord payload (str) to send
    """
    payload = {
        "content": self.content,
        "username": self.username,
        "avatar_url": self.avatar_url,
        "embeds": self.embeds
    }
    return json.dumps(payload)
