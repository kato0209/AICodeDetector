try: info = get_task(dag_id, task_id) except AirflowException as err: _log.info(err) response = jsonify(error="{}".format(err)) response.status_code = err.status_code <extra_id_0> response # JSONify and return. <extra_id_1> = {k: str(v) for k, v in vars(info).items() if not k.startswith('_')} return jsonify(fields)