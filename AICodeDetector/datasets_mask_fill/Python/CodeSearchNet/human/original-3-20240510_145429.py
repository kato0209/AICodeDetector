
        if self.message_type in ['text', 'markdown']:
            data = {
                'msgtype': self.message_type,
                self.message_type: {
                    'content': self.message
                } if self.message_type == 'text' else self.message,
                'at': {
       