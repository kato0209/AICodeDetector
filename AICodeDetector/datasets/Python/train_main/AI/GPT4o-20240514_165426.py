
    """
    This function creates the command list from available information
    """
    cmd = [self.base_command]
    if self.options:
        for option, value in self.options.items():
            cmd.append(f"--{option}")
            if value is not None:
                cmd.append(str(value))
    if self.arguments:
        cmd.extend(self.arguments)
    return cmd
