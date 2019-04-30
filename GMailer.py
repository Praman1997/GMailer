#!/usr/bin/python3

import smtplib
import os.path, os
import getpass

def sender(user, passwd):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(user,passwd)
        to_mail = input("Email To: ")
        subject = input("Subject: ")
        message = input("Message: ")
        compiled = "From: me <"+user+">\nTo: <"+to_mail+">\nSubject: "+subject+"\n\n"+message
        s.sendmail(user, to_mail, compiled)
        s.quit()
        print ("[+] Mail sent successfully!")
        pass
    except Exception as e: 
        print ("[-] Error sending mail! ",e)

def credentials():
    user = str(input("Enter your Email ID: "))
    passwd = str(getpass.getpass(prompt="Enter your Password: "))
    sender(user, passwd)

def home():
    print ("""
                                                                    
    //   ) )         /|    //| |                                    
   //               //|   // | |     ___     ( ) //  ___      __    
  //  ____   ____  // |  //  | |   //   ) ) / / // //___) ) //  ) ) 
 //    / /        //  | //   | |  //   / / / / // //       //       
((____/ /        //   |//    | | ((___( ( / / // ((____   //        
    
        Created By: PRAMAN KASLIWAL (CR4CKB0X)
        Visit My Site --> https://Praman1997.github.io/
        GitHub Link --> https://github.com/Praman1997
 
Note: For this program to work make sure that you have allowed access to less secure apps from your gmail account...
To know more visit this site --> https://support.google.com/accounts/answer/6010255?hl=en
    
""")



home()
credentials()