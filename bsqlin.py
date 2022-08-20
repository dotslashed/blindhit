import requests
import sys
from urllib.parse import urlparse
from colorama import Fore
import urllib3

urllib3.disable_warnings()
try:
	urlfile = sys.argv[1]
	payloadfile = sys.argv[2]

	try:

		with open(urlfile, 'r') as f1, open(payloadfile, 'r') as f2:
			n1 = f1.readlines()
			n2 = f2.readlines()
			for url_counter in n1:
				for pay_counter in n2:
					p = url_counter.count('&')
					parsed = urlparse(url_counter.strip())
					if p > 0:
						for i in range(p+1):
							x = parsed.query.split('&')[i].split('=')
							part1, part2 = url_counter.split(x[1])
							final_urls = part1 + pay_counter.strip() + part2
							no_space = final_urls.replace(' ', '%20')
							print('Testing for param: ' + Fore.RED + f'[{x[0]}]' + ' ' + Fore.WHITE + url_counter)
							resp = requests.get(no_space, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})

							if resp.elapsed.seconds >= 10:
								print(url_counter + Fore.GREEN + '[Vulnerable]' + Fore.WHITE + '')
					else:
						split_url = url_counter.strip().split('?')

						params = split_url[1].split('&')

						e = []
						for item in params:
							param_val = item.split('=')
						
							param_val[1] = f'{pay_counter}'
							partial = "=".join(param_val)
							e.append(partial)

				

						tail_join = "&".join(e)
						finale = split_url[0] + '?' + tail_join
						no_space2 = finale.replace(' ', '%20')
						print('Testing for param: ' + Fore.RED + f'[{param_val[0]}]' + Fore.WHITE + '')
						# print(no_space2)
						resp2 = requests.get(no_space2, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}, verify = False)

						if resp2.elapsed.seconds >= 10:
								print(url_counter + Fore.GREEN + ' [Vulnerable]' + Fore.WHITE + '')


	except KeyboardInterrupt:
		sys.exit()
except IndexError:
	print('Usage: python3 bsqlin.py <urls file with valid params> <time based payloads>')
