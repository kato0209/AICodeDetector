
        if not os.path.exists(self.processed_folder):
            os.makedirs(self.processed_folder)
        if not os.path.exists(self.processed_folder + '/'):
            os.makedirs(self.processed_folder + '/')
        if not os.path.exists(self.processed_folder + '/data_batch_1'):
            os.makedirs(self.processed_folder + '/data_batch_1')
        if not os.path.exists(self.processed_folder + '/data_batch_2'):
            os.makedirs(self.processed_folder