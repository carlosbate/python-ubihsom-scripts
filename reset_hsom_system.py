import json, requests

baseurl = 'http://localhost:'
hsomurl = baseurl + '8888/hsoms'
datastreamersurl = baseurl + '8585/datastreamers'
ubifactoryurl = baseurl + '8989/ubis'

def getallubis():
    response = requests.get(ubifactoryurl)
    return json.loads(response.text)

def getalldatastreamers():
    response = requests.get(datastreamersurl)
    return json.loads(response.text)

def getallhsom():
    response = requests.get(hsomurl)
    return json.loads(response.text)

def deletedatastreamer(datastreamerid):
    response = requests.delete(datastreamersurl + '/' + datastreamerid)

def deleteubi(ubiid):
    response = requests.delete(ubifactoryurl + '/' + ubiid)

def deletehsom(hsomid):
    response = requests.delete(hsomurl + '/' + hsomid)

def deletealldatastreamers():
    for datastreamer in getalldatastreamers():
        deletedatastreamer(datastreamer['id'])

def deleteallubis():
    for ubi in getallubis():
        deleteubi(ubi['id'])

def deleteallhsom():
    for hsom in getallhsom():
        deletehsom(hsom['id'])

deletealldatastreamers()
deleteallubis()

