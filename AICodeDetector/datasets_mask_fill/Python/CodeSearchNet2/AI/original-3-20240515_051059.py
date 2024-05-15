
        if size is None:
            size = self.filesize

        if size > self.filesize:
            self.log.debug("File size is greater than the minimum allowed file size (%s < %s)" % (self.filesize, size))
            return False

        if size < self.filesize:
            self.log.debug("File size is less than the maximum allowed file size (%s > %s)" % (self.filesize, size))
            return False

