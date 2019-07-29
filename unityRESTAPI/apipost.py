#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
requests.packages.urllib3.disable_warnings()

##
UNITY='10.241.167.231'          #Unity のIPアドレス
USER='admin'                  # Unity のユーザ
PASSWORD='Password1234#'    #パスワード

## post
##
headers = {'X-EMC-REST-CLIENT': 'true'}
r = requests.post('https://'+UNITY+'/api/instances/alertConfig/0/action/testEmailAlert' ,headers=headers, auth=(USER, PASSWORD), verify=False)
if r.status_code == 201:
    print ('Successed to post request')
    print (r.status_code )
    print (r.headers)
else:
    print ('Failed to get request')

