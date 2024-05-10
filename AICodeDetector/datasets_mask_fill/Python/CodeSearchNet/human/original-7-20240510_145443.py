
        axis = {}

        if custom_format and format:
            axis['tickFormat'] = format
        elif format:
            axis['tickFormat'] = "d3.format(',%s')" % format

        if label:
            axis['axisLabel'] = "'" + label + "'"

        # Add new axis to list of axis
        self.axislist[name] = axis