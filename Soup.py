from Parse import parse_response_name,parse_response_number
from bs4 import BeautifulSoup
from Emailer import send_mail

def crawler(context,dictionary,email_limit=10):

    #Got trough all sections of response to parse out relevant section
    for div in context.findAll('div', attrs={'class':'block__row media'}):
        #print(len(div))
        for div2 in div.find('ul'):
            #if there is a section
            #print(len(div2))
            if div2:
                response = str(div2) #cast it as a string
                info_name = parse_response_name(response) #parse response for name of care provider using helper method
                info_number = parse_response_number(response) #parse response for number of spots at care provider using helper method
                print(info_name)
                print(info_number)
                if info_name: #if name is parsed succesfully
                    if info_number: #and if number
                        if info_name not in dictionary.keys():
                            updated = True
                            number_of_available = info_number.split(" ") #split string again to get first element of number of spots
                            #print(number_of_available)
                            dictionary[info_name] = int(number_of_available[0]) #store in dict
                            if(int(number_of_available[0]) > int(email_limit)):
                                send_mail(info_name,number_of_available[0])
