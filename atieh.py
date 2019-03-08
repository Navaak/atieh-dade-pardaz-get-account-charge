# ### This script checks Atieh balance amount. you should add a config.py file that has json form of below configs. If the balance amount is less than config.charge_warning_amount, it will send an text message to config.mobile_number1.
# If the balance is less than config_charge_critical_amount it will send text message to 2 mobile numbers. 

import requests, datetime, logging, os
import config



now          = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M")
day          = now.strftime("%Y-%m-%d")

critical_daily_sent_sms_limit = 4
daily_sent_sms_limit   = 2
charge_critical_amount = int(config.charge_critical_amount)
charge_warning_amount  = int(config.charge_warning_amount)
mobile_number1         = config.mobile_number_list[0]
mobile_number2         = config.mobile_number_list[1]
mobile_number3         = config.mobile_number_list[2]
username               = config.username
password               = config.password
srcaddress             = config.srcaddress
logfile                = 'sms-limit-100k-'+day+"-"+mobile_number1+'.log'


if os.path.isfile( logfile ):
    sent_messages_count = len(open(logfile, "r").readlines())
else:
    sent_messages_count = len(open(logfile, "w+").readlines())


def terminal_logger(current_charge, mobile_number, current_time):
    logger = logging.getLogger("Atieh balance")
    logging.basicConfig(level=logging.INFO)
    return logger.info("{0} sent to {1} on {2}".format(current_charge, mobile_number, current_time))


def send_message(UserName, Password, Srcaddress , MobileNumber , CurrentCharge):
    requests.get("http://ws.adpdigital.com/url/multisend?username={0}&password={1}&srcaddress={2}&dstaddress0={3}&unicode0=1&body0=Atieh Balance: {4}".format(UserName, Password, Srcaddress , int(MobileNumber), CurrentCharge ))


def get_currrent_charge(Username, Password):
    current_charge_response  = requests.get("http://ws.adpdigital.com/url/balance?username={0}&password={1}&facility=send".format(username, password))
    current_charge_response_status_code = current_charge_response.status_code
    response_body  = current_charge_response.text

    if current_charge_response_status_code == 200:
        response_body = (str(response_body)[15:23])
        current_charge = int(response_body.rstrip("\n-"))
        return(current_charge)

    else:
        return("status code is ", current_charge_response_status_code)

current_charge = get_currrent_charge(username, password)




if current_charge > charge_warning_amount:
    exit()


if current_charge > charge_critical_amount:
    
    if sent_messages_count < daily_sent_sms_limit:

        send_message(username, password, srcaddress , mobile_number1 , current_charge)
       
        terminal_logger(current_charge, mobile_number1, current_time)

        ### tuye file benevisam       
        with open( logfile , 'a') as the_file:
            the_file.write("message sent\n, {}".format(current_time))
            print(logfile)

    else:
        print("you passed the limit.")


if current_charge < charge_critical_amount:
    
    if sent_messages_count < critical_daily_sent_sms_limit:    
    
        send_message(username, password, srcaddress , mobile_number1 , current_charge)
        send_message(username, password, srcaddress , mobile_number2 , current_charge)


        terminal_logger(current_charge, mobile_number1, current_time)
        terminal_logger(current_charge, mobile_number2, current_time)

    ### tuye file benevisam       
        with open( logfile , 'a') as the_file:
            the_file.write("message sent\n,  {}".format(current_time))
       
    else:
        print("you passed the limit")
