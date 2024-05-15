

class FileProcessor:
        self.start_time = time.time()
        self.processed_files = 0

        # Simulate file processing
        time.sleep(0.1)
        self.processed_files += 1
        self._print_stat()

        elapsed_time = time.time() - self.start_time
        if elapsed_time > 0:
            files_per_second = self.processed_files / elapsed_time
            print(f"Processed {self.processed_files} files in {elapsed_time