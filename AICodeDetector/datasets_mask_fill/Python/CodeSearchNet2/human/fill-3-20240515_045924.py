self.htmlheader = '' # If the JavaScript headers have already been injected, don't show them until we're re-sourcing them. def _js_initialized if '_js_initialized' not in globals() or not _js_initialized: for css in self.header_css: self.htmlheader += css for js in self.header_js: self.htmlheader += js