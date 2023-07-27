#!/usr/bin/python

""" get a ascii file grom github """

import requests, sys, os, re

def Decode_page(page):
    for lin in page.splitlines():
        l=len(lin)
        if l>1000:
            print(l)
            if "film" in str(lin)[0:50]:
                m = re.search(r"film\s*=(.+)", lin)
                if m:
                    lin2=m.group(1)
                    print (len(lin2))
                    print ("lin2 ", lin2[:50], "  ...    ", lin2[-50:])

                    m2_pattern=re.compile(r"([^\\]['])")
                    m2=m2_pattern.split(lin2)
                    if m2:
                        lin3=m2[2]+'n'
                        lin4=lin3.replace('\\n', '\n').replace("\\'", "'").replace("\\\\", "\\")
                        return (lin4)
    return '-'


def Get_film(name, URL):
    cache=0
    cache='cache'
    if cache and os.path.isfile(cache):
        print("using cache")
        with open (cache, "r", encoding='utf-8') as CACHE:
            data=CACHE.read()
    else:
        print("connecting")
        try:
            sock=requests.Session()
            sock.headers.update({'user-agent': 'curl/7.85.0'})
            Html = sock.get(URL, timeout= (2, 5) )
        except Exception as e:
            print("cant read URL: ", URL, "error:", e)
            return
        print("result", Html.status_code, "got:", len(Html.content))
        if ( 200 <= Html.status_code >299 ):
            print ("bad result", Html.status_code)
            return
        d1=bytes(Html.content)
        s=d1.rindex( bytes.fromhex("efbfbd") )
        print ("s is  ",s)
        d2=d1[:s]+b'-99999'+d1[s+3:]

        data=d2.decode('utf-8')
        if cache:
            with open (cache, "w", encoding='utf-8') as CACHE:
                CACHE.write(data)
    r=Decode_page(data)
    
    if r == '-':
        print ("cant read page result")
        return
    print("writing: ", name)
    with open (name, "w") as OUT:
        OUT.write(r)
    print("done")
        
name="star-wars.ascii"
URL="https://raw.githubusercontent.com/ArdaGurcan/star-wars-telnet-py/main/star-wars.py"
print (URL)
Get_film(name,URL)

