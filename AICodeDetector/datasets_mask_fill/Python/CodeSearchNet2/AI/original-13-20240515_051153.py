
        if not os.path.exists(self.processed_folder):
            os.makedirs(self.processed_folder)
        if not os.path.exists(self.processed_folder + '/emnist_data.npy'):
            download_url = 'http://www.iro.umontreal.ca/~lisa/deep/data/emnist_data.npy'
            urllib.request.urlretrieve(download_url, self.processed_folder + '/emnist_data.npy')
        if not os.path.exists(self.processed_folder + '/emnist_labels.