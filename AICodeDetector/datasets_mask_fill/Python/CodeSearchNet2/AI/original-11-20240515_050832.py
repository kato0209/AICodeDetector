
        body = copy.deepcopy(body)
        if'schedule' in body:
            body['schedule'] = body.pop('schedule')
        if 'description' in body:
            body['description'] = body.pop('description')
        if'schedule_time' in body:
            body['schedule_time'] = body.pop('schedule_time')
        if'schedule_time_offset' in body:
            body['schedule_time_offset'] = body.pop('schedule_time_offset')
        if'schedule_time_timezone' in body:
          