
    """
    SlackAPIOperator calls will not fail even if the call is not unsuccessful.
    It should not prevent a DAG from completing in success
    """
    try:
        # Your Slack API call logic here
        response = self.call_slack_api(**kwargs)
        if not response['ok']:
            self.log.warning("Slack API call was not successful: %s", response['error'])
    except Exception as e:
        self.log.error("An error occurred during Slack API call: %s", str(e))
