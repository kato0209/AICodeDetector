
    """
    Add a learning rate scheduler to the contained `schedules`

    :param scheduler: learning rate scheduler to be add
    :param max_iteration: iteration numbers this scheduler will run
    """
    if not hasattr(self, 'schedules'):
        self.schedules = []
    self.schedules.append((scheduler, max_iteration, bigdl_type))
