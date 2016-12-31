'''
Created on 2016/12/22

@author: nogami_kenji
'''

import configparser
import urllib.parse
import requests
import json

def yapi_topics():
        
    config = configparser.ConfigParser()
    config.read('config.ini')
    '''
    proxy_host = config['proxy']['host']
    proxy_port = config['proxy']['port']
    proxy_user = config['proxy']['user']
    proxy_pwd = config['proxy']['pwd']
    
    proxy_url = "http://" + urllib.parse.quote(proxy_user) + ":" + urllib.parse.quote(proxy_pwd) + \
                "@" + proxy_host + ":" + proxy_port + "/"
    #print("url = " + proxy_url)
    proxy = {'http': proxy_url}
    '''
    
    url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/categoryRanking?'
    appid = config['yahoo']['appid']
    params = urllib.parse.urlencode(
            {'appid': appid,
             'offset':1,
             'period':'weekly',
             'generation':30,
             'gender':'female',})

    #response = requests.get(url + params, proxies=proxy)
    response = requests.get(url + params)
    #
    print(response.status_code)
    print(response.headers)

    return response.text

def do_json(s):
    data = json.loads(s)
    #print(json.dumps(data, sort_keys=True, indent=4)); sys.exit()
    
    item_list = data["ResultSet"]["0"]["Result"]
    
    #jsonの階層の"Result"以下を辞書にする。keyは番号：その次の配列がvalueになっている
    ranking = {}
    for  k, v in item_list.items():
        try:
            rank = int(v["_attributes"]["rank"])
            vector = v["_attributes"]["vector"]
            name  = v["Name"]
            ranking[rank] = [vector, name]
        except:
            if k == "RankingInfo":
                StartDate = v["StartDate"]
                EndDate = v["EndDate"]
    
    print('-' * 40)
    print("集計開始日:", StartDate)
    print("集計終了日:", EndDate)
    print('-' * 40)
    ranking_keys = list(ranking.keys())
    ranking_keys.sort()
    for i in ranking_keys:
        print(i, ranking[i][0], ranking [i][1])

if __name__ == '__main__':
    json_str = yapi_topics()
    #print(json_str.status_code) 
    
    do_json(json_str)
