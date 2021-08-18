
def parse_response_name(string):
    try:
        temp_location = string.split("Boka tid via webben hos")
        temp2_location = temp_location[1]
        temp3_location = temp2_location.split('</a>')
        temp4_location = temp3_location[0]
        temp5_location = temp4_location.split("\r")
        return temp5_location[0]
    except:
        pass


def parse_response_number(string):
    try:
        temp_date = string.split("\n")
        #print(temp_date[4])
        temp2_date = temp_date[4].split('(')
        #print(temp2_date[1])
        if ("Mer än " in temp2_date[1]):
            temp5_date = temp2_date[1].split('Mer än ')
            temp6_date = temp5_date[1].split(')')
            return temp6_date[0]
        else:
            temp3_date = temp2_date[1].split(')')
            #print(temp3_date.split(""))
            return temp3_date[0]
    except:
        pass
