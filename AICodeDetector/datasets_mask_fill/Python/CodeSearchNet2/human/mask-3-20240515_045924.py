self.htmlheader = '' # If the JavaScript <extra_id_0> have already been injected, don't <extra_id_1> re-sourcing them. <extra_id_2> _js_initialized if '_js_initialized' not in globals() or not _js_initialized: for css in self.header_css: self.htmlheader += css for js in self.header_js: self.htmlheader += js