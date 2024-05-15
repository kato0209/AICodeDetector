

    # POSIX systems
    text = text.translate({
        0: None,
        ord('/'): '-',
        ord('|'): '-',
    })

    # FIXME: do some filesystem detection
    if os == 'windows' or os == 'cygwin' or os == 'wsl':
        # Windows (non-POSIX namespace)
        text = text.translate({
            # Reserved in Windows VFAT and NTFS
            ord(':'): '-',
        