
        self.log.info(
            'Transferring mail attachment %s from mail server via imap to s3 key %s...',
            self.imap_attachment_name, self.s3_key
        )

        with ImapHook(imap_conn_id=self.imap_conn_id) as imap_hook:
            imap_mail_attachments = imap_hook.retrieve_mail_attachments(
                name=self.imap_attachment_name,
                mail_folder=self.imap_mail_folder,
                check_regex=self.imap_check_regex,
 