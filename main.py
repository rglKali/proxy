from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs

open('list', 'w').write('')

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "lxml")
    responce = soup.find('tbody')
    proxies = str(responce).split('</tr><tr>')
    pr_list = []
    for i in proxies:
        proxy = i.split('</td>')
        pr = []
        for j in proxy:
            for h in range(len(j)-1, 0, -1):
                if j[h] == '>':
                    j = j[h+1:]
                    pr.append(j)
                    break
        pr_list.append(pr)
    files = []
    with open('list', 'a') as f:
        f.write(f'Updated on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n\n')
        for i in pr_list:
            f.write(f'IP: {i[0]}\n')
            f.write(f'Port: {i[1]}\n')
            f.write(f'Code: {i[2]}\n')
            f.write(f'Country: {i[3]}\n')
            f.write(f'Anonymity: {i[4]}\n')
            f.write(f'Google: {i[5]}\n')
            f.write(f'Https: {i[6]}\n')
            f.write(f'Last: {i[7]}\n')
            f.write('\n')

            list = {
                'IP': i[0],
                'Port': i[1],
                'Code': i[2],
                'Country': i[3],
                'Anonymity': i[4],
                'Google': i[5],
                'Https': i[6],
                'Last': i[7]
            }
            files.append(list)
    return files


list = get_free_proxies()
print('Check the file "list" to see all the aviable proxies')