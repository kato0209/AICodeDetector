
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = COMMASPACE.join(to)
    if cc:
        msg['Cc'] = COMMASPACE.join(cc)
    if bcc:
        msg['Bcc'] = COMMASPACE.join(bcc)
    msg['Date'] = formatdate(localtime=True)
    mime_charset = mime_charset or 'utf-8'
    mime_charset = mime_charset.lower()
    mime_charset = mime_charset.