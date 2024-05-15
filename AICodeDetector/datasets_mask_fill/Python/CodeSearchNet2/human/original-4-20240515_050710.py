
        content = {}

        if self.text:
            content['text'] = self.text

        content['controls'] = [control.json() for control in self.content]

        self.control_json['content'] = content

        return self.control_json