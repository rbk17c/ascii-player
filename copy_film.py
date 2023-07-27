#!/usr/bin/python

""" get a ascii file grom github """

import requests, sys, os, re

def Decode_page(page):
    for lin in page.splitlines():
        l=len(lin)
        if l>1000:
            print(l)
            if "film" in lin[0:50]:
                m = re.search(r"film\s*=(.+)", lin)
                if m:
                    lin2=m.group(1)
                    print (len(lin2))
                    print ("lin2 ", lin2[:50], "  ...    ", lin2[-50:])

                    m2_pattern=re.compile(r"([^\\]['])")
                    m2=m2_pattern.split(lin2)
                    if m2:
                        lin3=m2[2]+'n'
                        print ("lin3 ", lin3[:50], "  ...    ", lin3[-50:])
                        lin4=lin3.replace('\\n', '\n').replace("\\'", "'")
                        return (lin4)
    return '-'


def Get_film(name, URL):
    cache='cache'
    with open (name, "w") as OUT:
        if os.path.isfile(cache):
            with open (cache, "r") as CACHE:
                data=CACHE.read()
        else:
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
            data=Html.content
        r=Decode_page(data)
        
        if r == '-':
            print ("cant read page result")
            return
        print("writing:")
        print(r, file=OUT)
    print("")
        
name="star-wars.ascii"
URL="https://raw.githubusercontent.com/ArdaGurcan/star-wars-telnet-py/main/star-wars.py"
print (URL)
Get_film(name,URL)

