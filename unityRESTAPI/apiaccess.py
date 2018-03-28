#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
requests.packages.urllib3.disable_warnings()

##
UNITY='10.241.167.231'          #Unity のIPアドレス
USER='admin'                  # Unity のユーザ
PASSWORD='Password1234#'    #パスワード

## create http session
s = requests.Session()

## get
##
headers = {'X-EMC-REST-CLIENT': 'true'}
r = s.get('https://'+UNITY+'/api/types/alertConfig/instances' ,headers=headers, auth=(USER, PASSWORD), verify=False)
if r.status_code == 200:
    print ('Successed to get request')
    print (r.status_code )
    print (r.headers)
    print ()
    print (r.text)
else:
    print ('Failed to get request')

## close http session
s.close()
