

    """
    Execute the bash command in a temporary directory
    which will be cleaned afterwards
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            result = subprocess.run(self.bash_command, shell=True, cwd=temp_dir, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{self.bash_command}' failed with error: {e.stderr}")
