

    # Parse the JSON content
    course_data = json.loads(json_api_content)
    
    # Extract the specific part of the course
    try:
        topic = course_data['topics'][tIndex]
        part = topic['parts'][pIndex]
    except IndexError:
        raise ValueError("Invalid topic index or part index")
    
    # Get the download URL and filename
    video_url = part