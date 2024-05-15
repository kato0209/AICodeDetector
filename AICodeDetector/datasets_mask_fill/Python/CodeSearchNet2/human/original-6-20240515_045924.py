
        axis = {}
        if custom_format and format:
            axis['tickFormat'] = format
        elif format:
            if format == 'AM_PM':
                axis['tickFormat'] = "function(d) { return get_am_pm(parseInt(d)); }"
            else:
                axis['tickFormat'] = "d3.format(',%s')" % format

        if label:
     