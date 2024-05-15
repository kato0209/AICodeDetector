
    if not HAS_DAILYMOTION:
        raise ExtractorError('No Dailymotion program available for Dailymotion')

    ydl = YoutubeDL({'outtmpl': '%s/%s' % (output_dir, url),
                     'intmpl': '1'})
    ydl.report_warning = lambda msg: True
    ydl.params['format'] = 'bestvideo+bestaudio/best'
    ydl.add_default_info_extractors()
    ydl.to_screen(u'Downloading best video')

    # the downloader doesn't like the others, but we do need to pass the