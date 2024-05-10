
    data = _read_data('imdb.data', 'imdb.target')
    data = data.map(lambda x: x.split(','))
    data = data.map(lambda x: x.split(' '))
    data = data.map(lambda x: x.split(' '))
    data = data.map(lambda x: x.split(' '))
    data = data.map(lambda x: x.split(' '))
    data = data.map(lambda x: x.split(' '))
    data = data.map(lambda x: x.split(' '))
    return data


def