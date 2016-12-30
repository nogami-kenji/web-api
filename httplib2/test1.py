'''
Created on 2016/12/30

@author: nogami_kenji
'''

import httplib2

if __name__ == '__main__':
    h = httplib2.Http(".cache")
    (res_h, c) = h.request("https://www.google.co.jp/webhp?source=search_app", "GET")
    print(res_h)
    print(c)
    