
        import shutil
        import zipfile

        if self._check_exists():
            return

        makedir_exist_ok(self.raw_folder)
        makedir_exist_ok(self.processed_folder)

        # download files
        filename = self.url.rpartition('/')[2]
        file_path = os.path.join(self.raw_folder, filename)
        download_url(self.url, root=self.raw_folder, filename=filename, md5=None)

        print('Extracting zip archive')
        with zipfile.ZipFile(file_path) as zip_f:
         