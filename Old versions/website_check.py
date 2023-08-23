import concurrent.futures
import time
import utils.alert as alert
from decouple import config
from data.websites import *


while(True):
    # Use ThreadPoolExecutor to check URLs concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each URL
        tasks = [executor.submit(alert.check_url, url[0]) for url in web_url]

        # Wait for the tasks to complete and get the results
        results = [task.result() for task in concurrent.futures.as_completed(tasks)]

        # Sorts the task results in same order as URL tuple
        sorter = alert.sort_list(web_url, results)
    
    print(web_url)
    print("\nChecking website status...")
    for i, url in enumerate(results):
        # Checks status of each website and modifies its counter
        if sorter[i]['status'] != 200:
            web_url[i][1] += 1
        elif sorter[i]['status'] == 200:
            web_url[i][1] = 0
        else:
            pass

        # If counter reaches certain value, send email notification
        if web_url[i][1] == 0:
            web_url[i][2] = ''
        elif web_url[i][1] == 1:
            web_url[i][2] = time.ctime()
        elif web_url[i][1] == 5:
            data = (web_url[i][0], web_url[i][2][4:9], web_url[i][2][20:24], web_url[i][2][11:19], sorter[i]['status'])
            form = "Link: %s \nDate: %s, %s \nTime: %s \nError: %d"

            alert.email_alert("Alert! " + hostnames[web_url[i][0]] + " is down!",
                              form % data,
                              config('RECIPIENTS'))
            print("Notification for " + hostnames[web_url[i][0]] + " has been sent.")
        else:
            pass

        # Print status of website for current iteration
        print(f"{url['url']} - Status: {url['status']}")

    time.sleep(2)
