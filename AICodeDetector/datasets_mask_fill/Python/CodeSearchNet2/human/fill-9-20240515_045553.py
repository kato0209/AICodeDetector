for file_path, processor in self._processors.items(): while not processor.done: time.sleep(0.1)