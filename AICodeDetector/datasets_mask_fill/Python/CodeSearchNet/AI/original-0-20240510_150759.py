
        log_file = QFileDialog.getSaveFileName(
            self, self.tr("Save log file"), self.tr("Log file (*.log)"))
        if not log_file:
            return
        log_file = str(log_file)
        log_file = os.path.abspath(log_file)
        if not os.path.exists(log_file):
            return
        self.log_file = log_file
        self.log_file_edit.setText(self.tr("Log file: %s") % log_file)

    def _get_log_level