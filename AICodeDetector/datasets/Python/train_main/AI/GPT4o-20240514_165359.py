

    try:
        # Get the latest tag
        tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).strip().decode('utf-8')
        prefix = f'release:{tag}'
    except subprocess.CalledProcessError:
        # No tags found
        prefix = 'dev0'

    # Get the current commit hash
    commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')

    # Check for uncommitted changes
    try:
        subprocess.check