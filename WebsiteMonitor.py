import time
from data.websites import web_url
from utils.alert import send_notification, status_check, check_websites_concurrently
class WebsiteMonitor:
    def monitor_websites(self):
        while True:
            results = check_websites_concurrently(web_url)

            print(web_url)
            print("\nChecking website status...")
            for i, url in enumerate(results):
                status_check(web_url, url, i)
                send_notification(web_url, url, i)

                # Print the status of the website for the current iteration
                print(f"{url['url']} - Status: {url['status']}")

            time.sleep(2)
# Create an instance of the WebsiteMonitor class
monitor = WebsiteMonitor()

# Start monitoring the websites
monitor.monitor_websites()
