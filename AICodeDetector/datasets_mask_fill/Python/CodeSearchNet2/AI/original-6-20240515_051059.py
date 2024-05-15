
        try:
            self.bot.loop.create_task(self.bot.send_message(
                self.bot.get_channel(self.bot.config.username),
                "Discord webhook started",
                self.bot.config.username))
        except discord.errors.Forbidden:
            await self.bot.say("I need permissions to manage Discord webhook")
        except discord.errors.HTTPException:
            await self.bot.say("I need permissions to manage Discord webhook")
 