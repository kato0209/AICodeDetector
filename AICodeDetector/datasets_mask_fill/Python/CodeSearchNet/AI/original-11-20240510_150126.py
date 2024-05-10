
        if fail_if_exists and self.exists(project, topic):
            raise ValueError("Topic already exists: %s" % topic)

        self.log.info("Creating topic %s", topic)
        try:
            response = self.projects_api.create_topic(
                project=project,
                topic=topic,
                fail_if_exists=fail_if_exists
            )
    