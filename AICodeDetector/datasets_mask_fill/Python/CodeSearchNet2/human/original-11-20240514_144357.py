
        service = self.get_conn()
        full_topic = _format_topic(project, topic)
        try:
            service.projects().topics().create(
                name=full_topic, body={}).execute(num_retries=self.num_retries)
        except HttpError as e:
            # Status code 409 indicates that the topic already exists.
            if str(e.resp['status']) == '409':
                message = 'Topic already exists: {}'.format(full_topic)
 