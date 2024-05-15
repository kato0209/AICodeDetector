
    """generate javascript code for the chart"""
    chart_data = {
        'type': 'bar',
        'data': {
            'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            'datasets': [{
                'label': 'My First Dataset',
                'data': [65, 59, 80, 81, 56, 55, 40],
                'backgroundColor': [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54,