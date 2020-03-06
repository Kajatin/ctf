# lat: min=-90  max=90  step=0.0001
# lon: min=-180 max=180 step=0.0001

import requests
from time import sleep

#################################################
## solution params found by iterating the script
## this immediately returns the flag
# url = 'https://drivetothetarget.web.ctfcompetition.com/'
# token = 'gAAAAABeVYxPq5mO4dIFcz2_tlsqOyLhrL2_aFo0e2Ja0COutRkPfuNqu1QpUQnOEFeU3439HTj-_CA4KVYPkCZv-gt7urtdm1onQXU54Ki2bk5GLu1Uq3_bt8ywrbkSCIWvm8L5uZby'
# lat = 51.492099999994764
# lon = -0.19299999999999684

# payload = {'lat':str(lat), 'lon':str(lon), 'token':token}
# r = requests.get(url, params=payload, verify=False)

# resp = r.text.split('<p>')[2].split('</p>')[0]
# print(resp,lat,lon)
#################################################

directions = [
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1],
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]

url = 'https://drivetothetarget.web.ctfcompetition.com/'
token = 'gAAAAABeVVYwuCnxwG8EUaoYEDTWXejU4W55lwJqxmV2HDWrUHcT6oAcJEiC3Iosm6VJAqGn17f3E6eZ-eE4x54KkrdO9Nk2BZfXa65c8HepxbSdCWNA1CmLnHvpQJIPJNnQLqTs25d0'
lat = 51.6498
lon = 0.0982
step = 0.0001
timeout = 0.8

dir_selector = 3
direction = directions[dir_selector]

f = open('output.txt', 'w')

while 1:
    lat += step * direction[0]
    lon += step * direction[1]

    payload = {'lat':str(lat), 'lon':str(lon), 'token':token}
    r = requests.get(url, params=payload, verify=False)

    token = r.text.split('token\" value=\"')[1].split('\">')[0]
    resp = r.text.split('<p>')[2].split('</p>')[0]
    print(resp,lat,lon)
    f.write(''.join([resp,',',str(lat),',',str(lon),',',token,'\n']))

    if 'fast' in resp:
        timeout += 0.005
    elif 'away' in resp:
        dir_selector += 1
        if dir_selector >= len(directions):
            dir_selector = 0
        direction = directions[dir_selector]
    elif 'closer' not in resp:
        f.close()
        break
    
    sleep(timeout)