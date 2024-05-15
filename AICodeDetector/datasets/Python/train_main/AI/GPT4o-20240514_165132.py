
    """
    Find zombie task instances, which are tasks haven't heartbeated for too long.
    :return: Zombie task instances in SimpleTaskInstance format.
    """

    zombie_threshold = self.zombie_threshold if hasattr(self, 'zombie_threshold') else timedelta(minutes=10)
    current_time = datetime.utcnow()

    with create_session() as session:
        zombie