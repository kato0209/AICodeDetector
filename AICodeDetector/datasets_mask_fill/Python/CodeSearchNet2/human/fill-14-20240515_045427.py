output = output_dir + '.' + output if not (output_dir == '.'): output = output_dir + '/' + output print('Downloading '+ output + ' content with FFmpeg, or press q to stop recording...') if stream: ffmpeg_params = [FFMPEG] + ['-y', '-re', '-i'] else: ffmpeg_params = [FFMPEG] + ['-y', '-i'] ffmpeg_params.append(files) #not the same here!!!! if FFMPEG == 'avconv': #who cares? ffmpeg_params += ['-c', 'copy', output] else: ffmpeg_params += ['-c', 'copy',