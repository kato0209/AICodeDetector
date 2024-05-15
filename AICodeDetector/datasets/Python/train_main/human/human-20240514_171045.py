
    params_dict = {}
    h2o_methods.check_params_update_kwargs(params_dict, kwargs, 'model_builders', False)

    request = '3/ModelBuilders.json' 
    if algo:
        request += "/" + algo

    result = self.do_json_request(request, timeout=timeoutSecs, params=params_dict)
    # verboseprint(request, "result:", dump_json(result))
    h2o_sandbox.check_sandbox_for_errors()
    return result