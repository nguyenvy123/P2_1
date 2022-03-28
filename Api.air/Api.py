import requests
import json
from airtest.core.api import *

HTTP_PROXY = "http://172.28.103.34:3128"
HTTPS_PROXY = "https://172.28.103.34:3128"

# Lấy access token mới mỗi lần dùng tool cheat
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJSIjo2LjMxNjMyMTMyOTQ3OTEzOGUrNzYsIlMiOjMuODAwNzE5OTI5MzcyOTc2NWUrNzYsIkUiOjE2NDg0NDI2MTYsIlAiOnsiVSI6InZ5aG4iLCJHIjoiWlBTIn0sInVzZXJuYW1lIjoidnlobkB2bmcuY29tLnZuIiwiaWF0IjoxNjQ4NDMxMTYyLCJleHAiOjE2NDg1MTc1NjJ9.ySsMxcwP39fyuj_dGFzQb5gmKJrDKfeDTgUFeh0AHBw"

SERVER_HOST = "https://admin-dn-private.zingplay.com/"
BASE_URL = SERVER_HOST + "/api/"
GAME_CODE = "p2"
SERVER_ID = "PRIVATE_3_autotest(29)"

proxyDict = {
    "http": HTTP_PROXY,
    "https": HTTPS_PROXY,
    "ftp": ""
}

header = {
    "content-type": "application/json",
    "sessionKey": ACCESS_TOKEN
}

def api_postDoFunction(userId, fId, params):
    """"
        Send post function to admin tool back end
    """
#     try:
    url = BASE_URL + "doFunction"
    data = {
        "gameId": GAME_CODE,
        "mode": SERVER_ID,
        "userId": userId,
        "id": fId,
        "params": params
    }
    r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
    print("API status: %s" %r.status_code)
    sleep(1)
    return r.status_code
#     except json.decoder.JSONDecodeError:
#         print('Failed JSON')
# a = api_postDoFunction("21246207", "ADD_GOLD", "10000000")
def api_getUserInfo():
    """"
        Send get to admin tool back end
    """
    url = BASE_URL + "profile/getUserInfo"
    params = {
        "gameId": GAME_CODE,
        "mode": SERVER_ID
    }
    r = requests.get(url, headers=header, params=params)
    res = json.loads(r.text)
    print("API status: %s\nGet user info request status: %s" %(r.status_code, res))
    sleep(1)
    return r.status_code

def api_changeTimeServer(timeInMilliseconds):
    """"
        Send cheat time server
    """
    url = BASE_URL + "webmin/cheatTime"
    data = {
        "gameId": GAME_CODE,
        "mode": SERVER_ID,
        "time": timeInMilliseconds
    }
    r = requests.post(url, data=json.dumps(data), headers=header)
    res = json.loads(r.text)
    print("API status: %s\nChange time request status: %s" %(r.status_code, res))
    sleep(1)
    return r.status_code

def api_getModel(userId, modelName):
    """"
        Send post module to admin tool back end
    """
    url = BASE_URL + "player/getModel"
    data = {
        "gameId": GAME_CODE,
        "mode": SERVER_ID,
        "userId": userId,
        "modelName": modelName
    }
    r = requests.post(url, data=json.dumps(data), headers=header, timeout=1000)
    res = json.loads(r.text)['modelData']
    model = json.loads(res)
    print("API status: %s\n%s: %s" %(r.status_code, modelName, model))
    return model
# uGold = api_getModel("21246207", "UProfileModel")
# print(uGold)
# a = api_postDoFunction("21246207", 'CHEAT_TIME_SERVER', ["2021-10-02","17:00:00"])
# import datetime
# x = datetime.datetime.now().timestamp() # Timestamp - giây
# y = datetime.datetime.fromtimestamp(x) # Y-m-d h:m:s
# z = y.strftime("%m") # d/m/Y/H/M
# print("%s========%s============%s" %(x,y,z))
# t = datetime.datetime(2021, 1, 1, 13, 11, 12).timestamp() * 1000
# a = api_changeTimeServer(t)

# a = api_postDoFunction("21246207", "CHEAT_PAYMENT_VIP", ["vip.pack_1"])
# a = api_postDoFunction("21246207", "CHEAT_BUY_DCB", ["InAppPurchase.p2_1a"])
# a = api_getModel("21246207", "UProfileModel")
# a = api_postDoFunction("21246207", 'CHEAT_TIME_SERVER', ["2021-10-02","17:00:00"])
# print(a)
# start_app("com.zingplay.laviuda")
# sleep(20)

# Time running
# timeNow = str(datetime.datetime.now())
# timeNow = timeNow[:timeNow.find('.')]
# print("Start Hand %s" %timeNow)