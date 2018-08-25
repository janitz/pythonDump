#!/usr/bin/env python3
#need to install http://docs.python-requests.org/en/stable/user/install/ (run cmd as admin (sudo) pip install requests)
#python .\request.py

import sys
import requests

r = requests.get('http://www.der-postillon.com/search/label/Newsticker')
liste_raw = r.text.split('+++')
i=0
liste=[]
for strings in liste_raw:
	if strings[0:1] == ' ':
		strings = strings.replace('&quot;', '"')
		strings = strings.replace('&#39;', "'")
		strings = strings.replace('&#8211;', "-")
		if len(strings) < 162 : #longer as sms is unimportant
			if "<br>" not in strings:
				strings = "+++" + strings + "+++"
				liste.append(strings)

pythonfor stri in liste:
	print(stri)
