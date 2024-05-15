

    """Factory for making summary statistics, eg, mean, mode, stddev."""
        if attr == 'mean':
            return np.mean(data)
        elif attr == 'median':
            return np.median(data)
        elif attr == 'mode':
            return stats.mode(data).mode[0]
        elif attr == 'stddev':
            return np.std(data)
        elif attr == 'variance':
            return np.var(data)
        else:
            raise ValueError(f"Unknown attribute: