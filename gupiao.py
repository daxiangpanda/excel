#coding: UTF-8
import os
import re
import sys
import time
import urllib
import urllib2

stock_list = [
                {'name': 'sh',   'code': 'sh000001', 'mPrice': '0', 'mNu': '0'},
                {'name': 'sz',   'code': 'sz399001', 'mPrice': '0', 'mNu': '0'},
                {'name': 'sdgf', 'code': 'sh600820', 'mPrice': '8.236', 'mNu': '600'},
                {'name': 'nmhd', 'code': 'sh600863', 'mPrice': '4.093', 'mNu': '1500'},
                {'name': 'ylny', 'code': 'sh600277', 'mPrice': '8.826', 'mNu': '200'},
                {'name': 'nsly', 'code': 'sh600219', 'mPrice': '8.817', 'mNu': '500'},
                {'name': 'ylgf', 'code': 'sh600887', 'mPrice': '24.907', 'mNu': '0'},
                {'name': 'wskj', 'code': 'sz300017', 'mPrice': '58', 'mNu': '0'},
             ]
url_stock = 'http://hq.sinajs.cn/list='


def getPageSourceCode(url):
        login_data = urllib.urlencode({})
        login_headers = {'Referer':url, 'User-Agent':'Opera/9.60',}
        login_request = urllib2.Request(url, login_data, login_headers)
        html = urllib2.urlopen(login_request).read()
        return html.decode("gbk").encode("utf8")

#var hq_str_sh600887="▒▒▒▒ɷ▒,26.40,26.48,25.94,26.41,25.80,25.94,25.95,24212839,632218400,3700,25.94,48100,25.93,65800,25.92,77968,25.91,121100,25.90,149288,25.95,500,25.97,4200,25.98,63000,25.99,52300,26.00,2014-10-10,14:06:58,00";
def getstockInfo(code):
    items = []
    codes = code.split(',')
    result = getPageSourceCode(url_stock + code)
    if len(codes) == 1:
       i = 0
    else:
       i = 1
    for item in result.split(";\n"):
        items.append(item[len(codes[i])+len('var hq_str_')+1:].split(','))
    return items;

    #return result[len(code)+len('var hq_str_')+1:].split(',')

def getstockInfos(code):
    result = getstockInfo(code)
    return result

def getstocksInfo():
    print 'Time' + '\t\t\t' + 'Name' + '\t' + 'Price' + '\t\t' + 'Persent' + '\t\t\t' + 'own' + '\t' + 'profit' + '\t' + '%' + '\t' + 'mPrice'
    code = ""
    for item in stock_list:
        code = code + ',' + item['code']
    info = getstockInfos(code[1:])
    i = 0
    for item in info:
        if len(item) == 1:
           print "***\n"
           continue;
        persent = (float(item[3]) - float(item[2])) / float(item[2]) * 100
        if i == 0 or i == 1:
            print item[30] + ' ' + item[31] + ' ' + item[0][1:] + '\t' + item[3] + '\t\t' + str(persent)
        else:
            profit = (float(item[3]) - float(stock_list[i]['mPrice'])) * int(stock_list[i]['mNu'])
            profit_persent = (float(item[3]) - float(stock_list[i]['mPrice'])) / float(stock_list[i]['mPrice']) * 100
            print item[30] + ' ' + item[31] + ' ' + item[0][1:] + '\t' + item[3] + '\t\t' + str(persent) + '\t\t' + str(stock_list[i]['mNu']) + '\t' + str(profit) + '\t' + str(profit_persent) + '\t' + stock_list[i]['mPrice']
        i += 1


if __name__ == '__main__':
    if sys.argv[1] == '-h':
        print_help()
        sys.exit(1)

    if sys.argv[1] == '$':
       #while 1:
            getstocksInfo()
            #time.sleep(10)
            print 'done\n'
            sys.exit(1)