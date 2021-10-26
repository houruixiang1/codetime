import json

import requests
import execjs

n= input('请输入一个单词：')
url = 'https://fanyi.baidu.com/v2transapi?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Cookie': 'BAIDUID=240E84CC7AEC35238EC78A603DAEF141:FG=1; BIDUPSID=240E84CC7AEC35238EC78A603DAEF141; PSTM=1633677380; __yjs_duid=1_55cc14052825c2a3b1b02670f23fab2d1633765722672; BDUSS=J4UUNGbXVuWFlmWlR4bmdZdzNYbERGUHM3T1EtVWNKZWctRTctNDU5SUt2WkJoSVFBQUFBJCQAAAAAAAAAAAEAAAAuO63yaHJ4MTIzNDU2MTE4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAowaWEKMGlhRX; BDUSS_BFESS=J4UUNGbXVuWFlmWlR4bmdZdzNYbERGUHM3T1EtVWNKZWctRTctNDU5SUt2WkJoSVFBQUFBJCQAAAAAAAAAAAEAAAAuO63yaHJ4MTIzNDU2MTE4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAowaWEKMGlhRX; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34834_34068_31254_34860_34584_34518_34709_34578_34812_26350; PSINO=6; BAIDUID_BFESS=240E84CC7AEC35238EC78A603DAEF141:FG=1; delPer=1; BA_HECTOR=a02g058la4a1852g581gnetak0q; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1634611608,1634611646,1634611650,1635218776; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1635218776; ab_sr=1.0.1_NDQ4MTZiZTc0ODNjNTM4ODdkOWYzNzY0YWQ4ZTJhNWY1NjRkM2JiYWIwZjFlMTg5ZTA4M2VhYmIzZTA2MWUzNWRlODZlZDJhOTYwMTAwNDJjOWJhNmU2OTU5MDljMjk1MjViMDU2YjczNzdjMGVjNzE5YWNlNDQ1ZmY0ODFlYWFlYzQzMmQ5YzA3Y2I5MmJmNzhkMTcwNTBmNTlkNjRiZDg2YTZkYzMxMTc3ZWZlN2JhZWY5YWVmN2RiOWQ2M2Fk'
}
node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\js\baidufanyi.js',encoding='utf-8').read())
funcName = 'e("{0}")'.format(n)
sign = ctc.eval(funcName)
# if n[0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] else 'zh'
data = {
    'from': 'en' or 'zh' ,
    'to': 'zh' or 'en',
    'query': n,
    'transtype': 'realtime',
    'simple_means_flag': 3,
    'sign': sign,
    'token': '9c95f9496972cf937a5454dddd8553ca',
    'domain': 'common'
}
# method 1
resp = requests.post(url = url,headers=headers,data=data).json()
# method 2
# data = json.loads(resp.text)
print(resp)