# ### This script checks Atieh balance amount. you should add a config.py file that has json form of below configs. If the balance amount is less than config.charge_amount, it will send an text message to config.mobile_number1.
# If the balance is less than config_charge_critical_amount it will send text message to 2 mobile numbers. 


import requests, datetime, logging
import config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Atieh balance")


mobile_number1  = config.mobile_number_list[0]
mobile_number2  = config.mobile_number_list[1]
mobile_number3  = config.mobile_number_list[2]
username        = config.username
password        = config.password
srcaddress      = config.srcaddress
charge_amount   = int(config.charge_amount)
charge_critical_amount = int(config.charge_critical_amount)


now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M")


get_current_amount = requests.get("http://ws.adpdigital.com/url/balance?username={0}&password={1}&facility=send".format(username, password))

get_current_amount_status = get_current_amount.status_code
get_current_amount_body = get_current_amount.text


if get_current_amount_status == 200:
    get_current_amount_body = (str(get_current_amount_body)[15:23])
    current_charge = (int(get_current_amount_body))



if charge_critical_amount < current_charge < charge_amount:
    send_message = requests.get("http://ws.adpdigital.com/url/multisend?username={0}&password={1}&srcaddress={2}&dstaddress0={3}&unicode0=1&body0=Atieh Balance: {4}".format(username, password, srcaddress , int(mobile_number1), current_charge ))
    
    logger.info("{0} sent to {1} on {2}".format(current_charge, mobile_number1, current_time))



if current_charge < charge_critical_amount:
    send_message = requests.get("http://ws.adpdigital.com/url/multisend?username={0}&password={1}&srcaddress={2}&dstaddress0={3},{4},{5}&unicode0=1&body0=Charge Atieh!! Your balance is: {6}".format(username, password, srcaddress , int(mobile_number1), int(mobile_number2), int(mobile_number3), current_charge ))

    logger.info("{0} sent to {1}, {2}, {3} on {4}".format(current_charge, mobile_number1, mobile_number2, mobile_number3, current_time))
