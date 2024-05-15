

    # Email server connection details
    imap_host = context['imap_host']
    imap_user = context['imap_user']
    imap_pass = context['imap_pass']
    
    # S3 connection details
    s3_bucket = context['s3_bucket']
    s3_folder = context['s3_folder']
    
    # Connect to the email server
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(imap_user, imap_pass