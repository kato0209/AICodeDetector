if not model['name']: raise ValueError("Model name must be <extra_id_0> and " "could not be an <extra_id_1> string") project = 'projects/{}'.format(project_id) request = self._mlengine.projects().models().create( parent=project, body=model) return request.execute()