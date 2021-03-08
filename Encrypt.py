import os , sys , time

import base64
os.system ('clear')
def jalan(T):
   for r in T :
     sys.stdout.write(r)
     sys.stdout.flush()
     time.sleep(10/200)
print ("\033[1;92mtype\033[1;97m: '  GTA  '  !")
password= "GTA"
word = " "
count= 0
limit= 3
out = False
while word != password and not(out):
    if count < limit:
      word= input("\033[1;95mEnter password\033[1;97m:")
      count += 1
      os.system("clear")
    else:
        exit()
###########################
print ('\033[1;36m')
logo = """
███████╗███╗  ██╗ █████╗ ██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝████╗ ██║██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
█████╗  ██╔██╗██║██║  ╚═╝██████╔╝ ╚████╔╝ ██████╔╝   ██║
██╔══╝  ██║╚████║██║  ██╗██╔══██╗  ╚██╔╝  ██╔═══╝    ██║
███████╗██║ ╚███║╚█████╔╝██║  ██║   ██║   ██║        ██║
╚══════╝╚═╝  ╚══╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝
"""
print (logo)
jalan('''\033[1;96m--------------E---N---C---R---Y---P---T----------------
\033[1;92mWelcome, I hope you like this simple encoder and decoder
\033[1;96m-------------------------------------------------------
\033[1;94m
    [1] Decode


    [2] Decode


    [3] my Facebook


    [4] Exit\n''')

x =input("\033[1;94m»")
if x == "1":
      print ('\033[1;92m')
      encode_text = input("Enter Your Text For Encode It >>: ")
      encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')
      print ("\033[1;92m-----------------")
      print ("\033[1;92mDoen:\033[1;97m "+ encode_hash)
      print ("\033[1;92m----------------------")
elif x == "2":
      print ('\033[1;92m')
      decode_text = input("Enter Your Hash For Decode It >>: ")
      decode_hash = base64.b64decode(decode_text)
      decodeit = decode_hash.decode('UTF-8')
      print ("\033[1;92m------------------")
      print ("\033[1;92mDone:\033[1;97m "+ decodeit)
      print ("\033[1;92m-----------------------")
elif x == "3":
      os.system('xdg-open https://www.facebook.com/clavier.azerty.999') 
      os.system("clear")
      exit()
else:
      print ("\033[1;91mType Just 1 Or 2 !!")
      exit()
############################
