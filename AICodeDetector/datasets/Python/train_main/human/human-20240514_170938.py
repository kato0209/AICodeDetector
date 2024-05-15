
        intent_name = self.config['intent_name']
        slot_name = self.config['slot_name']

        request_id = request['request']['requestId']
        request_intent: dict = request['request']['intent']

        if intent_name != request_intent['name']:
            log.error(f"Wrong intent name received: {request_intent['name']} in request {request_id}")
            return {'error': 'wrong intent name'}

        if slot_name not in request_intent['slots'].keys():
            log.error(f'No slot named {slot_name} found in request {request_id}')
         