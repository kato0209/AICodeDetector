
        if self.scheduler is None:
            raise ValueError("Scheduler is not set")
        if self.scheduler_type == "linear":
            self.scheduler = LinearScheduler(scheduler, max_iteration)
        elif self.scheduler_type == "cosine":
            self.scheduler = CosineScheduler(scheduler, max_iteration)
        elif self.scheduler_type == "cosine_decay":
            self.scheduler = CosineDecayScheduler(scheduler, max_iteration)
        elif self.scheduler_type == "polynomial":
           