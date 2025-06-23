#!/usr/bin/env python3
import json
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

def test_email():
    try:
        sender_email = config['email']['sender_email']
        sender_password = config['email']['sender_password']
        recipient_email = config['email']['recipient_email']
        
        print(f"Testing email from: {sender_email}")
        print(f"To: {recipient_email}")
        
        message = MimeMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Test Email from Job Scraper MCP"
        
        body = "This is a test email from your Job Scraper MCP. If you receive this, your email setup is working!"
        message.attach(MimeText(body, "plain"))
        
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("Logging in...")
        server.login(sender_email, sender_password)
        
        print("Sending email...")
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        
        print("✅ SUCCESS! Test email sent successfully!")
        print("Check your Gmail inbox for the test email.")
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        print("\nCommon issues:")
        print("1. App password is wrong")
        print("2. 2-Step Verification not enabled")
        print("3. Email address is wrong")

if __name__ == "__main__":
    test_email()