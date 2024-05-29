import smtplib
from bs4 import BeautifulSoup
from email_config import email

def send_email(dest_email):
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email['address'], password=email['password'])
            connection.sendmail(from_addr=email['address'],
                                to_addrs=dest_email,
                                msg=f"Subject:Price drop on {data.get('name')} \n\n{current_price}")
        print("email sent")
        
def main():
    pass
        