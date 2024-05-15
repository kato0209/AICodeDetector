
    if not info_only:
        return json_api_content

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(os.path.join(output_dir, 'course.json')):
        os.makedirs(os.path.join(output_dir, 'course.json'))

    if not os.path.exists(os.path.join(output_dir, 'course.json')):
        os.makedirs(os.path.join(output_dir, 'course.json'))

    if not os