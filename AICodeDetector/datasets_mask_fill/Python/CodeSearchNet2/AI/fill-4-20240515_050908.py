if isinstance(days, int): days = abs(days) if isinstance(days, str): days = days.split('-') if len(days) == 1: return ds +'' + days[0] if len(days) == 2: return ds + days[0] +'' + days[1] if len(days) == 3: return ds + days[0] +'' + days[1] +'' + days[2] if len(days) == 4: return ds + days[0] +''