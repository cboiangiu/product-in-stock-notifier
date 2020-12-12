import getpass
from os import system

system("pip install -r requirements.txt")

print("\nConfigure .env for notifier app:\n")

with open("notifier/.env", "a") as env_file:
    env_file.write("PROXY_COUNTRY_CODE="+input("PROXY_COUNTRY_CODE (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) = ")+"\n")
    env_file.write("EMAILER_HOST="+input("EMAILER_HOST (your email's host address) = ")+"\n")
    env_file.write("EMAILER_PORT="+input("EMAILER_PORT (usually 465 since we use SSL) = ")+"\n")
    env_file.write("EMAILER_EMAIL="+input("EMAILER_EMAIL = ")+"\n")
    env_file.write("EMAILER_PASSWORD="+getpass.getpass("EMAILER_PASSWORD = ")+"\n")
    env_file.write("EMAILS_TO_NOTIFY="+input("EMAILS_TO_NOTIFY (separated by ,) = ")+"\n")
    env_file.write("CHECKING_DELAY="+input("CHECKING_DELAY (in seconds; recommended is 10) = "))
