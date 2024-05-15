
    """
    Call the SlackWebhookHook to post the provided Slack message
    """

    slack_webhook_token = self.slack_webhook_token
    message = self.message

    hook = SlackWebhookHook(
        http_conn_id=slack_webhook_token,
        message=message
    )
    hook.execute()
