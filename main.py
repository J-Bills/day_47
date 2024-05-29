import smtplib
import requests
from selectolax.parser import HTMLParser
from email_config import email

headers = {
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15',
    'language': 'en-US,en;q=0.9'
}

def send_email(dest_email, product_cost, product_name, product_url):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email['address'], password=email['password'])
        connection.sendmail(from_addr=email['address'], to_addrs=dest_email, msg=f"Subject:Price drop on {product_name} \n\nCurrent Price: ${product_cost} \n\nLink:{product_url}")
        print("email sent")

def track_product(url):
    product_url = url
    response = requests.get(product_url, headers=headers)
    html = HTMLParser(response.text)
    price = [node.text() for node in html.css('span.a-offscreen')]
    title = html.css_first('span#productTitle').text().encode('utf-8').strip()
    current_price = float(price[1].replace('$', ''))
    
    return current_price, title

def main():
    email = str(input("input your email\n"))
    url = str(input('paste amazon url of product\n'))
    target_price = float(input('input target price for item\n'))
    cost, name = track_product(url)
    
    if cost < target_price:
        send_email(email, str(cost), name, url)

main()
