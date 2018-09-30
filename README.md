# atieh-dade-pardaz-balance-check
This is for checking atieh dade pardaz balance amount and send alert if you need to charge it.

You should add a config.py file that has json form of below configs and put your own information. 

mobile_number_list = []

username = ''

password = ''

srcaddress = ''

charge_amount = ''

charge_critical_amount = ''

If the balance amount is less than config.charge_amount, it will send an text message to config.mobile_number1.
