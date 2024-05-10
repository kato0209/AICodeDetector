
        long_f = 'extra__google_cloud_platform__{}'.format(f)
        if hasattr(self, 'extras') and long_f in self.extras:
            return self.extras[long_f]
        else:
            return default