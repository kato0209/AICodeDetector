

    output_path = os.path.join(output_dir, f"{title}.{ext}")
    ffmpeg_command = ['ffmpeg']

    for key, value in params.items():
        ffmpeg_command.extend([f"-{key}", str(value)])

    if stream:
        ffmpeg_command.extend(['-i', files, output_path])
    else:
        ffmpeg_command.extend(['-i', files, '-c', 'copy', output_path])

    subprocess.run(ffmpeg_command, check=True)
