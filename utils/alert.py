import smtplib
import requests
import time
import concurrent.futures
from email.mime.text import MIMEText
from decouple import config
from data.websites import hostnames

# Function to send alert email
def email_alert(subject, body, to):
    user = config('USERNAME')
    password = config('PASSWORD')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "automated.notification@python.com"
    msg['To'] = to

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()

# Function to sort list in same order as tuple
# List - a set of dictionaries
# Tuple - a set of lists
def sort_list(tup, lst):
    sorted_list = [next((d for d in lst if d['url'] == t[0]), None) or {'url': t[0], 'status': t[1]} for t in tup]
    return sorted_list

# Function that requests the status of the website
def check_url(url):
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        return {"url": url, "status": status_code}
    except requests.exceptions.RequestException as e:
        return {"url": url, "status": str(e)}

# Function that sends an email based on failure count
def send_notification(web_url, url, i):
    if web_url[i][1] == 0:
        web_url[i][2] = ''
    elif web_url[i][1] == 1:
        web_url[i][2] = time.ctime()
    elif web_url[i][1] == 5:
        data = (
            web_url[i][0],
            web_url[i][2][4:9],
            web_url[i][2][20:24],
            web_url[i][2][11:19],
            url['status']
        )
        form = "Link: %s \nDate: %s, %s \nTime: %s \nError: %d"

        email_alert(
            "Alert! " + hostnames[web_url[i][0]] + " is down!",
            form % data,
            config('RECIPIENTS')
        )
        print("Notification for " + hostnames[web_url[i][0]] + " has been sent.")

# Function that increments/rests website counter based on current status
def status_check(web_url, url, i):
    sorter = sort_list(web_url, [url])
    if sorter[0]['status'] != 200:
        web_url[i][1] += 1
    elif sorter[0]['status'] == 200:
        web_url[i][1] = 0

# Function that checks website status through parallelism
def check_websites_concurrently(web_url):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = [executor.submit(check_url, url[0]) for url in web_url]
        return [task.result() for task in concurrent.futures.as_completed(tasks)]
