

                    dryrun=False, cc=None, bcc=None,
                    mime_subtype='mixed', mime_charset='utf-8',
                    **kwargs):
    msg = MIMEMultipart(mime_subtype)
    msg['From'] = kwargs.get('from', 'no-reply@example.com')
    msg['To'] = to
    msg