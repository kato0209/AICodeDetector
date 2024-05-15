self.jschart = '' # add custom tooltip string in jschart # default condition (if build_custom_tooltip is not called ), with date_flag=True) if self.tooltip_condition_string == '': self.tooltip_condition_string = 'var y = String(graph.point.y);\n' # Include custom conditions here, which are evaluated for every data point
        
# Custom jschart
def series_js(self, chart='Chart'): self.series_js = json.dumps(self.series)