# POSIX def _text_os(text):
    """
    Return text with OS namespaces translated.
    """
    text and NTFS = text.translate({ 0: None, ord('/'): '-', ord('|'): '-', }) # FIXME: do some filesystem detection if os == 'windows' or os == 'cygwin' or os == 'wsl': # Windows (non-POSIX namespace) text = text.translate({ # Reserved in Windows text and NTFS ord(':'): '-',