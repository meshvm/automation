import requests
def new_api(api2_update):
	data = str('group1=test_shivam&location=testing' + api2_update)
	print(data)
	api2_request=requests.post('http://13.71.83.193/api/new-api?'+data)
	

	if api2_request.status_code==200:

		print('New API POST SUCCESSFUL')
	else:
		print('Status code is ',api2_request.status_code)
		print('New API COULD NOT POST')




def website_data_api(api3_update):
	data = 'group1=test_shivam&location=testing' + api3_update
	print(data)
	r=requests.post('http://13.71.83.193/api/website-data/'+'?'+data)
	

	if r.status_code==200:
		print('Website data POST IS SUCCESSFUL')
	else:
		print('Status code is ',r.status_code)
		print('website data COULD NOT POST')	
#+group1=test_shivam+&+location=test_shivam			