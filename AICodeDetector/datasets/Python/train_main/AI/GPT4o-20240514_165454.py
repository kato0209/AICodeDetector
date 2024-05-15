
    """
    Build different type of Dingding message
    As most commonly used type, text message just need post message content
    rather than a dict like ``{'content': 'message'}``
    """
    if self.message_type == 'text':
        return self.message_content
    elif self.message_type == 'markdown':
        return {
            'msgtype': 'markdown',
            'markdown': {
                'title': self.message_title,
                'text': self.message_content
            }
        }
    elif self.message_type == 'link':
        return {
            'msgtype