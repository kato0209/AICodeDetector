

        assert vid

        self.prepare(vid = vid, title = title, **kwargs)

        self.extract(**kwargs)

        self.download(output_dir = output_dir, 
                    merge = merge, 
                    info_only = info_only, **kwargs)