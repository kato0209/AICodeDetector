
        self.buildcontent()
        self.content = self.htmlcontent
        self.htmlcontent = self.template_page_nvd3.render(chart=self)