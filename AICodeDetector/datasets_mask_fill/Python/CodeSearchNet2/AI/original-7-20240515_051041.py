
        if format is None:
            format = self.default_format

        if label is None:
            label = name

        if format == 'latex':
            label = r'$\mathrm{y}$'

        if format == 'latex_raw':
            label = r'$\mathrm{y}$'

        if format == 'latex_raw_with_labels':
            label = r'$\mathrm{y}$'

  