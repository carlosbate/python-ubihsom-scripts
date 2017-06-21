import requests as api

dsUrl = 'http://localhost:8585/datastreamers'
hsomUrl = 'http://localhost:8888/hsoms'


def createseqds(dbname, timer, selectors):
    data = {
        'type': 'DB',
        'db': dbname,
        'timer': timer,
        'selectors': selectors,
        'pull-type': 'SEQUENTIAL'
    }
    response = api.post(dsUrl, json=data)
    result = response.json()
    response.close()
    return result


def createrandomds(dbname, timer, randomness, selectors):
    data = {
        'type': 'DB',
        'db': dbname,
        'timer': timer,
        'randomness': randomness,
        'selectors': selectors,
        'pull-type': 'RANDOM'
    }
    response = api.post(dsUrl, json=data)
    result = response.json()
    response.close()
    return result


def createhsom(name):
    data = {'name': name}
    response = api.post(hsomUrl, json=data)
    result = response.json()
    response.close()
    return result


def createhsomnode(hsomid, order, timer, name, weightlabels, dim):
    data = {
      'order': order,
      'timer': timer,
      'model': {
        'name': name,
        'weight-labels': weightlabels,
        'width': 40,
        'height': 20,
        'dim': dim,
        'alpha_i': 0.1,
        'alpha_f': 0.08,
        'sigma_i': 0.6,
        'sigma_f': 0.2,
        'beta_value': 0.7,
        'normalization': {
          'type': 'NONE'
        }
      }
    }

    response = api.post(hsomUrl + '/' + hsomid + '/nodes', json=data)
    result = response.json()
    response.close()
    return result


def linknode(hsomid, source, target):
    data = {
        'source': source,
        'target': target
    }

    response = api.post(hsomUrl + '/' + hsomid + '/edges', json=data)
    response.close()


def createproxy(source, target):
    data = {
        'type': 'PROXY',
        'in': source + '-out',
        "out": target + '-in'
    }

    response = api.post(dsUrl, json=data)
    result = response.json()
    response.close()
    return result


def linkdatasource(datasourceid, hsomnodeid):
    response = createproxy(datasourceid, hsomnodeid)
    result = response
    return result

