#通过freegeoip.net网站查找IP地址所在国家
import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('UTF-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print (getCountry("50.78.253.58"))