

        hook = SQSHook(aws_conn_id=self.aws_conn_id)

        result = hook.send_message(queue_url=self.sqs_queue,
                                   message_body=self.message_content,
                                   delay_seconds=self.delay_seconds,
                                   message_attributes=self.message_attributes)

  