
        self.htmlheader = ''
        # If the JavaScript assets have already been injected, don't bother re-sourcing them.
        global _js_initialized
        if '_js_initialized' not in globals() or not _js_initialized:
            for css in self.header_css:
                self.htmlheader += css
            for js in self.header_js:
                self.htmlheader += js