

log_file

waring_msg

critical_msg


get_daily_sent_sms_num()



if amount < warning:

	if amount > critical:
		if get_daily_sent_sms_num() < daily_sent_sms_limit
			warning_msg()
			log_file()
		else:
			exit()

	if amount < critical:
		if get_daily_sent_sms_num < critical_daily_sent_sms_limit
			critical_msg()
			log_file()
		else:
			exit()

else:
	exit()
