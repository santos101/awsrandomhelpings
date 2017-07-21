#! /usr/bin/env python2

import json
import os
import os.path
import glob

os.chdir('/home/chris.kirby/cloudtrail')
for file in glob.glob("*.json"):
    fileNamestr = str(file)

    with open (fileNamestr) as data_file:
        data = json.load(data_file)

    for item in data["Records"]:
        userName = None
        eventName = None
        eventSource = None
        arn = None
        if 'userName' in item['userIdentity']:
            userName = item['userIdentity']['userName']
        elif 'sessionContext' in item['userIdentity']:
            userName = item['userIdentity']['sessionContext']['sessionIssuer']['userName']
            arn = item['userIdentity']['sessionContext']['sessionIssuer']['arn']
        
        eventName =  item['eventName']
        eventSource = item['eventSource']
        #print userName, eventName, eventSource, arn
        userNamestr = str(userName)
        eventNamestr = str(eventName)
        eventSourcestr = str(eventSource)
        arnstr = str(arn)
        f = open( 'file', 'a' )
        f.write(userNamestr)
        f.write(" ")
        f.write(eventSourcestr)
        f.write(" ")
        f.write(eventNamestr)
        f.write(" ")
        f.write(arnstr)
        f.write("\n")
