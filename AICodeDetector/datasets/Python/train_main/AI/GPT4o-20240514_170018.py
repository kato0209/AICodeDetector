

    method = params.get('method', 'GET')
    headers = params.get('headers', {})
    data = params.get('data', {})
    url = params.get('url', '')
    category = params.get('category', '')
    pageno = params.get('pageno', 1)

    if method == 'POST':
        response = requests.post(url, headers=headers, data=data)
    else:
        response = requests.get(url, headers=headers, params={'query': query, 'category': category, 'pageno': pageno})

    return response.json