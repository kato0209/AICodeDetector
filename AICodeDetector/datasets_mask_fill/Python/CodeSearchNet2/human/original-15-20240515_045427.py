

    for tIndex in range(len(json_api_content[0]['Topics'])):
        for pIndex in range(len(json_api_content[0]['Topics'][tIndex]['Parts'])):
            wanmen_download_by_course_topic_part(json_api_content,
                                                 tIndex,
                                                