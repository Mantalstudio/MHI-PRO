### Import module 
import os
try:
    import requests
except ImportError:
    print(" Module requests belum terinstall")
    os.system('pip install requests')
import os, sys, requests, time, json, datetime

# INI KOMBINASI WARNA OKH:V
O ='\x1b[1;96m' 
P ='\033[0;00m' 
J ='\033[0;33m'
S ='\033[0;00m'
N ='\x1b[0m' 
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;33m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
i='\033[0;32m'
mm='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
B ='\033[0;36m'
#P='\033[0;37m'
k ='\033[00m'
h ='\033[0;90m'
Q ="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
R ='\033[0;36m'                                                                                                              
h ='\033[0;90m'
W ="\033[0;00m"
i ='\033[0;32m'
mm='\033[0;36m'
m ='\033[0;31m'
c ='\033[0;32m'
C ='\033[0;32m'
O ='\033[0;33m'
H ='\033[0;33m'
G ='\033[0;36m'
p ='\033[0;00m'
b ='\033[0;36m'                                          
m ='\033[0;31m'
N ='\x1b[0m'                                              
I ='\033[0;32m'
k ='\033[0;33m'
o ='\033[0;31m'                                           
U ='\033[0;33m'
K ='\033[0;33m'
# BUAT JALAN
def jalan(z):
    for e in z :
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)
        
# Buat pembersih
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# BUAT BANNER
banner = """
\033[1;36m______________
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;36m-------------------------------------------------------------\033[0;00m[\033[0;33m•\033[0;00m]
\033[0;36m |
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m AUTHOR   \033[0;35m: \033[0;32mMantal STudio,\033[0;33m USAMA BIN IFTIKHAR Programer
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m GITHUB   \033[0;35m: \033[0;00mhttps://github.com/MantalStudio
\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m WHATSAPP \033[0;35m: \033[0;00m+923011517172
\033[0;36m |
"""

# Buat menu 
def menu():
    clear()
    jalan(banner)
    token = input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Enter token : ")
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Token successful")
#p    bot()
    try:
        k = requests.get('https://graph.facebook.com/me?access_token='+token) #<<<<<<<<< THIS IS TO CHECK USER NAME ETC, GUYS
        nan = json.loads(k.text)
        name = nan['name']
        idfb = nan['id']
        link = nan['link']
        email = nan['email']
        print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Login Successful")
        time.sleep(3)
    except:
        print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Modar token")
        os.sys.exit()
    os.system("clear")
    jalan(banner) # <<<<<< ACCOUNT INFORMATION :V JOKE KEK GITU AING IN SAYING RECORD :V BASIS
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Username  : %s "%(name))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Userid    : %s "%(idfb))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Link      : %s "%(link))
    print("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Email     : %s "%(email))
    print(" \033[0;36m| ")
    nanoid = input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Post ID : ")
    waktu = int(input("\033[0;00m[\033[0;33m•\033[0;00m]\033[0;00m Time per share : "))
    print(" \033[0;36m| ")
    asu = 0
    asu = asu + 1
    while True:
        requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(nanoid)+'&access_token='+str(token)) #<<<<<<<<< INI URL UNTUK TANCAP GAS KE SHARE
        print("\033[0;36m[\033[0;33m•\033[0;36m]\033[0;33m <<<•>>> \033[0;36m[\033[0;00m BERHASILL \033[0;36m]\033[0;33m <<<•>>> \033[0;36m[ \033[0;00m%s \033[0;36m]"%(str(nanoid)))
#        
menu()
