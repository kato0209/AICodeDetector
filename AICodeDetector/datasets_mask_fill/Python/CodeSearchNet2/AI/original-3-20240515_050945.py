
    connection = get_connection(backend=EMAIL_BACKEND)
    message = EmailMultiAlternatives(subject, text_content, from_email, to)
    if cc:
        message.cc = cc
    if bcc:
        message.bcc = bcc
    if files is None:
        files = {}
    message.attach_alternative(html_content, 'text/html')
    message.attach(files)
    message.send(fail_silently=True)


def send_mass_mail(to, subject, html_content,
                   files=None, dryrun=False, cc=