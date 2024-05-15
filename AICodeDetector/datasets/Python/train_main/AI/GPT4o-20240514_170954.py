
    if event_name == "after_validation":
        self.learning_rate = data.get("learning_rate", self.learning_rate)
        self.momentum = data.get("momentum", self.momentum)
    elif event_name == "after_batch":
        self.learning_rate = data.get("learning_rate", self.learning_rate)
    elif event_name == "after_epoch":
        self.momentum = data.get("momentum", self.momentum)
    elif event_name == "after_train_log":
        self.learning_rate = data.get("learning_rate",