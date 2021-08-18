from Mining import get_webpage
from Parse import parse_response_name,parse_response_number
from bs4 import BeautifulSoup
from datetime import *
from time import sleep
from Emailer import send_mail
from Soup import crawler


def get_vaccination_dates(update_frequency= 300,verbose=False,debug_mode=False):
    available_dates = {} #Dict to store available locations and number of spots
    while True:
        last_update = datetime.now() #get the current time

        miner = get_webpage() #scrape webpage using check_dates
        soup = BeautifulSoup(miner.text, 'html.parser') #Parse response with BS
        crawler(soup,available_dates,email_limit=20)

        if verbose:
            print(available_dates)
            print(last_update)

        sleep(update_frequency)

def main():
    get_vaccination_dates(verbose=True)




if __name__ == "__main__":
    main()
