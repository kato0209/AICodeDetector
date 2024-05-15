

    client = pubsub_v1.PublisherClient()
    topic_path = client.topic_path(project, topic)
    
    try:
        client.create_topic(request={"name": topic_path})
    except AlreadyExists:
        if fail_if_exists:
            raise
