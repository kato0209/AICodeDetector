
    try:
        import git
        try:
            repo = git.Repo('.git')
        except git.exc.InvalidGitRepositoryError:
            return "unknown"
        except git.exc.GitCommandError:
            return "dirty"
        except OSError:
            return "no_git_version"
        if repo.is_dirty():
            return "dirty"
    