#Made by Kapitan (RooftopKorean) 
#Please be aware that too many request may blacklists you

import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue
import urllib.request
import os

def main():

	try:
		os.mkdir('output')
	except:
		pass

	def process(l):
		x,y = l
		try:
			url = f'https://maps.izurvive.com/maps/ChernarusPlus-Sat/1.23.0/tiles/8/{x}/{y}.webp'
			urllib.request.urlretrieve(url, f"output/{x}-{y}.webp")
			print(f"{x}-{y}.webp downloaded succesfully")
		except Exception as e:
			print(f'Exception in {x}-{y}.webp downloaded succesfully | {str(e)}')
			fl = open('log.txt','w',encoding='utf-8-sig')
			fl.write(f'Exception in {x}-{y}.webp downloaded succesfully | {str(e)}\n')
			fl.close()

	def threader():
	    while True:
	        worker = q.get()
	        process(worker)
	        q.task_done()

	for x in range(246):
		q = Queue()
		for k in range(50):
			t = threading.Thread(target=threader)
			t.daemon = True
			t.start()

		for y in range(9,256):
		    q.put([x,y])
		    
		q.join()

main()