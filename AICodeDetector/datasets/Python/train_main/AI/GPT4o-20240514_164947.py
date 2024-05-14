

    """int->None
    
    Download a WHOLE course.
    Reuse the API call to save time."""
    
    if isinstance(json_api_content, str):
        json_api_content = json.loads(json_api_content)
    
    course_title = json_api_content.get('title', 'Unknown Course')
    course_dir = os.path.join(output_dir, course_title)
    os.makedirs(course_dir, exist_ok=True)
    
    for chapter in json_api_content.get