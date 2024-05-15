
    """Deletes Conversation instance.

    Args:
        conversation_key: Conversation key.
    """
    if conversation_key in self.conversations:
        del self.conversations[conversation_key]
