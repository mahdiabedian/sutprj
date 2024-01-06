import requests
import time
def req(a):
    try:
        r = requests.head(a)
        return r.status_code
    except requests.ConnectionError or requests.ConnectTimeout as error:
        return error
while 1:
    u = open('D:/URLs.txt','r')
    r=u.readlines()
    for i in range(len(r)):
        if r[i]=='' or r[i]=='\n':
            pass
        else:
            if r[i][-1:]=='\n':
                status=req(r[i][:-1])
                if status == 200 :
                    print(r[i][:-1], ': ', status)
                else:
                    print(r[i][:-1], ': ', status)
                    data = {'from': '50004001339496', 'to': ['09223454335'], 'text': f'{r[i][:-1]} has problem\nstatus: {status}', 'udh': ''}
                    response = requests.post(
                        'https://console.melipayamak.com/api/send/advanced/yourmellipayamakapikey', json=data)
                    print(response.json())
            else:
                status = req(r[i])
                if status == 200:
                    print(r[i], ': ', status)
                else:
                    print(r[i], ': ', status)
                    data = {'from': '50004001339496', 'to': ['09223454335'],
                            'text': f'{r[i]} has problem\nstatus: {status}', 'udh': ''}
                    response = requests.post(
                        'https://console.melipayamak.com/api/send/advanced/yourmellipayamakapikey', json=data)
                    print(response.json())
    u.close()
    time.sleep(120)
