
        self.hook = SlackWebhookHook(
            self.http_conn_id,
            self.webhook_token,
            self.message,
            self.attachments,
            self.channel,
            self.username,
            self.icon_emoji,
            self.link_names,
            self.proxy
        )
 