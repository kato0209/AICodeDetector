
        self.buildcontainer()
        # if the subclass has a method buildjs this method will be
        # called instead of the method defined here
        # when this subclass method is entered it does call
        # the method buildjschart defined here
        self.buildjschart()
        self.htmlcontent = self.template_chart_nvd3.render(chart=self)