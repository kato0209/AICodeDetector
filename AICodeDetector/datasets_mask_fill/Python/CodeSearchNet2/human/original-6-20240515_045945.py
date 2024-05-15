
        proxies = {}
        if self.proxy:
            # we only need https proxy for Discord
            proxies = {'https': self.proxy}

        discord_payload = self._build_discord_payload()

        self.run(endpoint=self.webhook_endpoint,
                 data=discord_payload,
                 headers={'Content-type': 'application/json'},
                 extra_options={'proxies': proxies})