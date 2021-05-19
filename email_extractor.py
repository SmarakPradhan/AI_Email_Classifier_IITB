import os
import extract_msg
import csv
import regex as re
import pandas as pd

def extract(path):
    os.chdir(path)
    email=[]
    file_name=[]

    
    for f in os.listdir('.'):
        emails=[]
        if not f.endswith('.msg'):
            continue
        file_name.append(f)
        msg = extract_msg.Message(f)
        msg_message = msg.body
        regex = re.compile(r'[\n\r\t]')
        msg_message = regex.sub(" ", msg_message)
        emails=msg_message.split("From:")
        emails.pop(0)
        concat_emails=""
        for mail in emails:
            mail=mail.split("Subject:")[-1]
            #print(mail)
            #mail=mail.replace("ABC","")
            #mail=mail.replace("XYZ,","")
            #mail=mail.replace("XYZ","")
            #mail=mail.replace("DEF","")        
            mail=mail.replace("[WARNING: MESSAGE ENCRYPTED]","")
            mail=mail.replace("[MESSAGE ENCRYPTED]","")
            mail=mail.replace("[EXTERNAL]","")
            mail=mail.replace("[DEF0000]","")
            mail=mail.replace("RE:","")
            mail=mail.replace("Re:","")
            mail=mail.replace("FW: Mr","")
            mail=mail.replace("Fw:","")
            mail=mail.replace("Fwd:","")
            mail=mail.replace("Mrs","")
            mail=mail.replace("Mr","")
            mail=mail.replace("Urgent:","")
            mail=mail.replace("URGENT","")
            mail=mail.replace("FW:","")
            mail=mail.replace("Content:","")
            mail=mail.replace("Sent from my iPad","")
            mail=mail.replace("[Not Virus Scanned - Password Protected]","")
            mail=mail.replace("ALERT: This message originated outside of Fin Corp Ltd. network. BE CAUTIOUS before clicking any link or attachment.","")
            mail=mail.replace("Importance: High","")
            mail=mail.replace("test.pensions@pensions.com <mailto:test.pensions@pensions.com>","")
            mail=mail.replace("Sent from Mail<https://go.microsoft.com/fwlink/?LinkId=550986> for Windows 10","")
            mail=mail.replace("*","")
            mail=mail.replace(">","")
            mail=mail.replace("-","")
            mail=mail.replace("•","")
            mail=mail.replace("_","")
            mail=mail.replace("CAUTION: This email originates from a nonJaguarlandrover source. Do not click links or open attachments unless you recognise the sender and know the content is safe.","")
            mail=mail.split("Kind regards")[0]
            mail=mail.split("Kind Regards")[0]
            mail=mail.split("Many thanks")[0]
            if mail.find("Thank you for")==-1:
                mail=mail.split("Thank you")[0]
            mail=mail.split("Regards")[0]
            mail=mail.split("Thanks")[0]
            mail=mail.split("Yours sincerely")[0]
            concat_emails=concat_emails+""+mail
        concat_emails=" ".join(concat_emails.split())
        email.append(concat_emails)
        
        
        
    df = pd.DataFrame({'Filename':file_name,'data':email})
    
    
    df.to_csv('test.csv',encoding='utf-8-sig',index=False)
   
   