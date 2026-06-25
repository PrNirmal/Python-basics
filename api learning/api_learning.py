# 1
import json
import requests

url = "https://www.nseindia.com/"
thejsonu = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

thehead = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "accept-encoding": "gzip, deflate, br"
}

session = requests.Session()
theget = session.get(url, headers=thehead)
thecook = dict(theget.cookies)
theresult = session.get(thejsonu, headers=thehead, cookies=thecook)
write_1 = theresult.json()

with open("jsonfile_1.json", 'w') as wrk:
    json.dump(write_1, wrk, indent=2)

# 2.
import requests
import json

main_url = "https://www.nseindia.com/"
api_url = ["https://www.nseindia.com/api/master-quote",
           "https://www.nseindia.com/api/merged-daily-reports?key=favCapital",
           "https://www.nseindia.com/api/merged-daily-reports?key=favDerivatives",
           "https://www.nseindia.com/api/merged-daily-reports?key=favDebt",
           "https://www.nseindia.com/api/circulars",
           "https://www.nseindia.com/api/latest-circular",
           "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY",
           """https://c.go-mpulse.net/api/config.json?key=RF6LV-Y7HBS-S5S4P-HB5LE-V8XXL&d=www.nseindia.com&t=5562322&v=1.720.0&if=&sl=0&si=8b2371bf-f29c-4c33-b13d-6fc04bc63cfc-rlhyf3&bcn=%2F%2F684d0d46.akstat.io%2F&plugins=AK,ConfigOverride,
           Continuity,PageParams,IFrameDelay,AutoXHR,SPA,History,Angular,Backbone,Ember,RT,CrossDomain,BW,PaintTiming,NavigationTiming,
           ResourceTiming,Memory,CACHE_RELOAD,Errors,TPAnalytics,UserTiming,Akamai,Early,EventTiming,LOGN&acao=&ak.ai=509815""",
           "https://www.nseindia.com/api/marketStatus",
           "https://c.go-mpulse.net/api/config.json?key=RF6LV-Y7HBS-S5S4P-HB5LE-V8XXL&d=www.nseindia.com&t=5562323&v=1.720.0&if=&sl=1&si=8b2371bf-f29c-4c33-b13d-6fc04bc63cfc-rlhyf3&r=&bcn=%2F%2F684d0d46.akstat.io%2F&acao=&ak.ai=509815"]
all_head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "accept-language": "en-GB,en-US;q=0.9,exn;q=0.8",
    "accept-encoding": "gzip, deflate, br"
}

the_session = requests.Session()
toget = the_session.get(main_url, headers=all_head)
thecook = dict(toget.cookies)
for i in range(len(api_url)):
    thesec = api_url[i]
    the_Ans = the_session.get(thesec, headers=all_head, cookies=thecook)
    write_1 = the_Ans.json()
    with open(f"jsonfile_{i}.json", 'w') as wpk:
        json.dump(write_1, wpk, indent=2)


# 2. get method

import requests

Url="http://maps.googleapis.com/maps/api/geocode/json"
locate="summa kudupom"

Paramah={'address':locate}
r=requests.get(url=Url,params=Paramah)

the_data=r.json()
print(the_data)