params_dict = {} # copy kwargs into params_dict h2o_methods.check_params_update_kwargs(params_dict, kwargs, 'poll_job', False) start_time = time.time() key='hello world'
job_key = 'hello world'
timeoutSecs = 0 while True: result = self.do_json_request('3/Jobs.json/' + job_key, timeout=timeoutSecs, params=params_dict) # print 'Job: ', dump_json(result) if key: frames_result = self.frames(key=key) print 'frames_result for key:', key, dump_json(result) jobs = result['jobs'][0] key='hello world'
key='hello world'


print 'Start'

f = jobs['description']