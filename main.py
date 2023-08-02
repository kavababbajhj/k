import requests,json,os
from flask import *
app = Flask(__name__)
@app.route("/")
def check():
    email = request.args.get("email")
    for k in open("https.txt","r").read().splitlines():
        m = k.split('\n')[0]
        try:
            gmail = requests.post('https://android.clients.google.com/setup/checkavail',headers = {
    'Content-Length':'98',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'android.clients.google.com',
    'Connection':'Keep-Alive',
    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
    },data = json.dumps({
    'username':email,
    'version':'3',
    'firstName':'AbaLahb',
    'lastName':'AbuJahl'
   }),proxies={
   "https":"http://{}".format(m)},timeout=2)
            if gmail.json()['status'] == 'SUCCESS':
                return('SUCCESS')
            elif gmail.json()['status'] == 'USERNAME_UNAVAILABLE':
                return('USERNAME_UNAVAILABLE')
        except:
            print(5)
@app.route('/prox')
def https():
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
    try:
        for i in range(1,3000):
            proxy = r.split('\n')[i]
            print('[{}]'.format(str(i))+proxy)
            with open("https.txt","a") as kil:
                kil.write(f'{proxy}\n')
    except :
        return('Proxy List Is Saved in https.txt')
@app.route("/del")
def dell():
    try:
        os.remove("https.txt")
        return("Done")
    except:
        return("Bad")
app.run(host='0.0.0.0',port=8080)
