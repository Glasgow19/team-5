#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:29:21 2019

@author: yenji
"""

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import time
from flask import Flask
from flask_mail import Message, Mail


@app.route("/")

def server():
    pass
    
def send_mail():
    smtp_server = "smtp.gmail.com"
    #port = 587  # For starttls
    sender_email = "team5c4g@gmail.com"
    password = "PaSsWoRd1"

receiver_email="maslinkin@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Help Request."
    msg['From'] = "Team5"
    msg['To'] = "maslinkin@gmail.com"

    text = "Please send help to exhibit 3."

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')

    msg.attach(part1)
    # Create a secure SSL context
    print("SSL...")
    context = ssl.create_default_context()
    print("SSL DONE...")

    with smtplib.SMTP(smtp_server, port) as server:
        print("STARTED...")
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        print("Logging in...")
        server.login(sender_email, password)
        print("Logged in...")
        print("Sending...")
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Sent...")
        server.quit()


send_mail()
