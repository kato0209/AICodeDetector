

    """
    This function disables printing when not in master process
    """
    if not is_master:
        builtins.print = lambda *args, **kwargs: None

# Example usage:
# setup_for_distributed(os.getenv('RANK') == '0')
