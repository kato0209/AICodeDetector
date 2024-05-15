
        if not self.channel.is_web_hook_enabled:
            raise AirflowException("Slack Webhook is not enabled for this channel")

        response = self.channel.webhooks.run(
            name=self.name,
            channel=self.channel,
            text=self.text,
            username=self.username,
            icon_emoji=self.icon_emoji,
            icon_url=self.icon_url,
            icon_emoji_alt=self.icon_emoji_alt,
   