
    """Build HTML content only, no header or body tags. To be useful this
    will usually require the attribute `jquery_on_ready` to be set which
    will wrap the js in $(function(){<regular_js>};)
    """
    html_content = "<div>Your HTML content here</div>"
    if hasattr(self, 'jquery_on_ready') and self.jquery_on_ready:
        js_content = "$(function(){" + self.jquery_on_ready + "});"
        html_content += f"<script>{js_content}</script>"
    return html_content
