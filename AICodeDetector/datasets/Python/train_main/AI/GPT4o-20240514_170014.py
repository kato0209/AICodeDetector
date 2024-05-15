

class MNISTDownloader:
        self.processed_folder = processed_folder
        self.url_base = 'http://yann.lecun.com/exdb/mnist/'
        self.files = {
            'train_images': 'train-images-idx3-ubyte.gz',
            'train_labels': 'train-labels-idx1-ubyte.gz',
            'test_images': 't10k-images-idx3-ubyte.gz',
            'test_labels': 't10k-labels-