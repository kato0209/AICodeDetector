
        try:
            res = self.session.http.get(url)
            data = res.text
            data = data.replace('\n', '')
            data = data.replace('\r', '')
            data = data.replace('\t', '')
            data = data.replace('\n', '')
            data = data.replace('\r', '')
            data = data.replace('\t', '')
 