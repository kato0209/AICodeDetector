
    """
    Construct the Slack message. All relevant parameters are combined here to a valid
    Slack json message
    :return: Slack message (str) to send
    """
    message = {
        "channel": self.channel,
        "username": self.username,
        "text": self.text,
        "icon_emoji": self.icon_emoji,
        "attachments": self.attachments
    }
    return json.dumps(message)
