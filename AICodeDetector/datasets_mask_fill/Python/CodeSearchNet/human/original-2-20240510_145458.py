
        if not self.api_params:
            self.construct_api_call_params()
        slack = SlackHook(token=self.token, slack_conn_id=self.slack_conn_id)
        slack.call(self.method, self.api_params)