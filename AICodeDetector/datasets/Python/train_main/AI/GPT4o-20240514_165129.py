

    """
    Sleeps until all the processors are done.
    """
    while not self.all_processors_done():
        time.sleep(1)
