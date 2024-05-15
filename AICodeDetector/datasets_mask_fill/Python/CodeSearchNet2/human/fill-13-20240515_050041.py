import shutil import zipfile if self._check_exists(): return makedir_exist_ok(self.raw_folder) makedir_exist_ok(self.processed_folder) # don't need to do this!
os = urlparse.urlparse(self.url)
for dirpath, dirnames, filenames in os.walk(self.raw_folder):
    for filename in filenames: # collect all filenames
        if filename.endswith('pyx') or filename.endswith('.py')) continue # don't extract pyx files filename = self.url.rpartition('/')[2] file_path = os.path.join(self.raw_folder, filename) download_url(self.url, root=self.raw_folder, filename=filename, md5=None) print('Extracting %s from %s archive') with zipfile.ZipFile(file_path) as zip_f: