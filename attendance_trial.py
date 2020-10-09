# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:37:33 2020

@author: Lalitha
"""


import numpy as np
import cv2
import time




import boto3
import requests

while(True):
    

    client=boto3.client('rekognition',
                    aws_access_key_id="ASIAUJOMIPXWUURRPWRC",
                        aws_secret_access_key="eA5Y8EvNXRWR5ElLcwTlqkim9RPgBy52Kshg+uDK",
                        aws_session_token="FwoGZXIvYXdzEB4aDEh8aqKUzvEcvLOB7iLHARBB8TC+Gs6cuvO9mpd8+3Ugmy6ozUiT6ego5ZlTNgPFGKUBHVA+PSzaiYV3LnBi3e0RW2FMb4XCn57ZCwujyheD8CkSZwsnmTFaTQeky29b6oNxTrK9GukfO+H8Iw2IInYecL18il8FQaXbJehqWkGVPkLHi6bgDgL+KfkS8sCv4w5h8F0ISgQd/qziSW5UX8DgDcSq6YRsSPM2bXjo+LxVf3Iq1d43zi1DTiKlL54CnIYSrv49CRi3cshK/YXy7jXNfycIwYQouraB/AUyLeLZEG2bPe+OC9nDSt3R8pXHJ71zzU+xl8/MHh/2WOFOAbjfnOW+dQpFPz+E7w==",
                        region_name='us-east-1')

    with open(r'E:\Co-curricular\Smartintern AI project\cam.jpg','rb') as source_image:
        source_bytes=source_image.read()
    print(type(source_bytes))

    print("Recognition Service")
    response = client.detect_custom_labels(
    ProjectVersionArn='arn:aws:rekognition:us-east-1:295170506221:project/Hourly_attendance/version/Hourly_attendance.2020-09-29T01.10.22/1601322025136',
   
    Image={
        'Bytes':source_bytes

    },
   
    )

    print(response)
    if not len(response['CustomLabels']):
        print('Animal not identified')

    else:
        str=response['CustomLabels'][0]['Name']
        url="https://i36bw98emf.execute-api.us-east-1.amazonaws.com/people_counting?rollno="+str
        resp = requests.get(url)
        print(resp)
    time.sleep(60*60);    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
