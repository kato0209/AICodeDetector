
        if format is None:
            format = self.default_format
        if date:
            self.date_format = date
        if label is None:
            label = self.default_label
        axis = self.axes[name]
        axis.set_title(label)
        axis.set_xlabel(name)
        axis.set_ylabel(name)
        axis.set_zlabel(name)
        axis.set_zlim(self.z_limits[name])
    