

    """
    Execute the bash command in a temporary directory
    which will be cleaned afterwards
    """
    command = context.get('command')
    if not command:
        raise ValueError("No command provided in context")

    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            result = subprocess.run(command, shell=True, cwd=temp_dir, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"