
class DecayType:
    @classmethod
        decay_types = {
            "linear": 0,
            "cosine": 1,
            "exponential": 2,
            "onecycle": 3,
            "trapezoid": 4
        }
        
        if label.startswith("polynomial"):
            try:
                _, k = label.split(',')
                return int(k.strip())
            except ValueError:
                raise ValueError("Invalid polynomial format. Use 'polynomial, K' where K is an integer.")
        
        if