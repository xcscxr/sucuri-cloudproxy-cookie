import re
import js2py
import requests

def sucuri_bypass(url):
    res = requests.get(url, headers={
        'user-agent': "Mozilla/5.0 Chrome/96.0.4664.45 Safari/537.36"
    })
    scr = re.findall('<script>([\s\S]*?)<\/script>', res.text, re.MULTILINE)[0]
    a=(scr.split("(r)")[0][:-1]+"r=r.replace('document.cookie','var cookie');")

    b = (js2py.eval_js(a))

    sucuri_cloudproxy_cookie = js2py.eval_js(b.replace("location.","").replace("reload();",""))
    cookies={sucuri_cloudproxy_cookie.split("=")[0]:sucuri_cloudproxy_cookie.split("=")[1].replace(";path","")}

    return cookies

# ========================================

# Some url with sucuri firewall
url = ""
cookie = sucuri_bypass(url)

print(cookie)

'''
SAMPLE OUTPUT:

{
    'sucuri_cloudproxy_uuid_c0a2d045c': 'a2bb1c33db6abbafcbf83b784a2a9eea'
}
'''
