import logging
import time
import threading
from os import getenv, makedirs
from os.path import join, dirname
from datetime import datetime, timedelta
from dotenv import load_dotenv
from user_agent import generate_user_agent
from modules.emailer import Emailer
from modules.product_status import Status
from modules.util import getDuration
from products import products

makedirs("log", exist_ok=True)
logging.basicConfig(handlers=[logging.FileHandler(filename=join(dirname(__file__), "log/notifier_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"),
                                                 encoding='utf-8', mode='a+'), logging.StreamHandler()],
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s [%(threadName)s] ",
                    datefmt="%F %A %T",
                    level=logging.INFO)
load_dotenv()
proxy_country_code = getenv("PROXY_COUNTRY_CODE").lower()
emailer_host = getenv("EMAILER_HOST")
emailer_port = int(getenv("EMAILER_PORT"))
emailer_email = getenv("EMAILER_EMAIL")
emailer_password = getenv("EMAILER_PASSWORD")
emails_to_notify = getenv("EMAILS_TO_NOTIFY").split(",")
checking_delay = int(getenv("CHECKING_DELAY"))
emailer = Emailer(emailer_host,emailer_port,emailer_email,emailer_password)
start_time = datetime.now()
notify_uptime_time = start_time + timedelta(hours=12)

def notify_emails(subject, body):
    for email in emails_to_notify:
        emailer.send_email(email, subject, body)
        time.sleep(1)

class NotifierThread(threading.Thread):
   def __init__(self, threadID, name, product):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.product = product

   def run(self):
        global notify_uptime_time
        logging.info("Starting " + self.name + " - " + self.product.get_product())
        while True:
            status = self.product.check(generate_user_agent(), proxy_country_code)
            if status == Status.NOTIFY_STOCK:
                logging.info("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - IN STOCK - " + self.product.get_url())
                notify_emails("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - IN STOCK",self.product.get_url())
            elif status == Status.FAIL:
                logging.info("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - FAIL REQUEST - " + self.product.get_url())
            elif status == Status.PAGE_CHANGED_SHOULD_NOTIFY:
                logging.info("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - Store page changed - " + "Update css in the store class!")
                notify_emails("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - Store page changed","Update css in the store class!")
                break
            elif status == Status.PAGE_CHANGED:
                logging.info("notifier - " + self.product.get_product() + ":"+ self.product.get_store() + " - Store page changed - " + "Update css in the store class!")
                break
            if datetime.now() > notify_uptime_time:
                notify_uptime_time = datetime.now() + timedelta(hours=12)
                uptime = getDuration(start_time)
                logging.info("notifier - uptime - All good! Will notify back in 12 hours. Uptime: " + uptime)
                notify_emails("notifier - uptime","All good! Will notify back in 12 hours. Uptime: " + uptime)
            time.sleep(checking_delay)
        logging.error("Exiting " + self.name + " - " + self.product.get_product())

def main():
    logging.info("Starting...")
    notify_emails("notifier has started", "all good!")
    thread_id_prefix = "Thread-"
    thread_id = 1
    threads = []
    for product in products:
        thread = NotifierThread(thread_id, thread_id_prefix + str(thread_id), product)
        thread.start()
        threads.append(thread)
        thread_id += 1
    
    for t in threads:
        t.join()

    notify_emails("notifier has exited", "something went wrong!")

if __name__ == "__main__":
    main()
