
        queue_name = self.queue_name
        queue_arn = self.queue_arn
        queue_attributes = self.queue_attributes
        message_attributes = self.message_attributes
        message_attributes['sqs_message_attributes'] = queue_attributes
        message_attributes['sqs_queue_name'] = queue_name
        message_attributes['sqs_queue_arn'] = queue_arn
        message_attributes['sqs_message_attributes'] = message_attributes
        message_attributes['sqs_message_attributes_list'] = message_attributes.get('sqs_message_attributes_list',