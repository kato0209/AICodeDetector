
    a = self.do_json_request('3/ImportFiles.json',
        timeout=timeoutSecs,
        params={"path": path}
    )
    verboseprint("\nimport_files result:", dump_json(a))
    h2o_sandbox.check_sandbox_for_errors()
    return a