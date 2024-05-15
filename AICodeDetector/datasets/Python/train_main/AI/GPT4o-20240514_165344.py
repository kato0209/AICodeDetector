

               files=None, dryrun=False, cc=None, bcc=None,
               mime_subtype='mixed', mime_charset='utf-8', **kwargs):
    """
    Send email using backend specified in EMAIL_BACKEND.
    """
    msg = MIMEMultipart(mime_subtype