from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
from time import strftime
from random import randint, uniform
import pandas as pd
from secret import name, pw

account = name
password = pw
ale = 1
sup = 0

class igbot:
	def __init__(self, user, pw):
		self.user = user
		self.pw = pw
		print(user)
		self.driver=webdriver.Chrome("/Users/Barbarossa/Desktop/Prog/bots/chromedriver")
		time.sleep(1)
		self.driver.get('https://www.instagram.com/accounts/login/')
		time.sleep(1)
		self.driver.find_element_by_name('username').send_keys(user)
		self.driver.find_element_by_name('password').send_keys(pw)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
		time.sleep(3.5)
		#Find that annoying notification button and say no!
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(uniform(1,5))
		#database of the following people of each account
		self.dbname='{}_following_list.csv'.format(user)
		#Now we are in the IG homepage, let's move around

	def randomise(self):
		#Run some random moves on the IG
		self.driver.get('https://www.instagram.com/')
		#First IG story open
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/button/div[1]').click()
		#Click next or back
		for i in range(0,100):
			time.sleep(uniform(0.5,25))
			if randint(0,10) > 1:
				self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[2]/div').click()
			else:
				self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[1]/div').click()
		self.driver.close()

	def newfollow(self,hashtag_list=['instagram']):
		try:
			self.following_list= pd.read_csv(self.dbname,delimiter=',').iloc[:,1:2]
			self.following_list = list(self.following_list['0'])
		except FileNotFoundError as e:
			file_status = 'missing'
			self.following_list = []
		new_followed = []
		tag = 0
		followed = 0
		likes = 0
		comments = 0
		#7 Comments
		comm = ['Wow, amazing!',"Aaahw, that's something", "Damn!", "Looove it!", "Hey where u from?", "Yoooo", "That's something else...","I would like to ride it...", "I kind like it", "Hey, where u at?"]

		for tag in hashtag_list:
			#Go to explore hashtag page
			self.driver.get('https://www.instagram.com/explore/tags/'+tag+'/')
			time.sleep(1)
			#Open first foto
			self.thumb = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
			self.thumb.click()
			time.sleep(2)

			try:
				if randint(0,100) > 4:
					for x in range(1,60):
						#Identifiy the user
						username = self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > a').text
						#Interactions start here!
						#If account does not follow the user...
						if self.driver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button").text == "Follow":
							time.sleep(1)
							#Should I follow?
							if randint(0,100) > 85:
								time.sleep(uniform(2,3))
								self.driver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button").click()
								#time.sleep(1)
								#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
								#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
								#else:
								#	new_followed.append(username)
								#	self.following_list.append(username)
								#	print(username + 'followed correctly')
								#	followed+=1
								new_followed.append(username)
								self.following_list.append(username)
								print(username + ' ------------------ followed correctly')
								followed+=1
								updated_user_df = pd.DataFrame(self.following_list)
								updated_user_df.to_csv(self.dbname)
							time.sleep(uniform(0,3))

							#Should I comment?
							if randint(0,100) > 80:
								time.sleep(uniform(2,5))
								self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
								self.comment_box = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
								self.comment_box.send_keys(comm[randint(0,9)])
								self.comment_box.send_keys(Keys.ENTER)
								#time.sleep(1)
								#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
								#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
								#else:
								#	comments += 1
								comments += 1
								print(username + ' commented correctly NF')
								time.sleep(uniform(0.5,2))

							#Should I like?
							if randint(0,100) > 60:
								time.sleep(uniform(0.5,2))
								self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg').click()
								#time.sleep(1)
								#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
								#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
								#else:
								#	likes += 1
								likes += 1
								print(username + ' liked correctly NF')
								time.sleep(uniform(0.5,2))

						#If the user is not followed?
						else:
							if randint(0,100) > 60:
								time.sleep(uniform(0.5,2))
								self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg').click()
								#time.sleep(1)
								#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
								#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
								#else:
								#	likes += 1
								likes += 1
								print(username + ' Liked correctly AF')
								time.sleep(uniform(0.5,2))

							if randint(0,100) > 85:
								time.sleep(uniform(1,3))
								self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
								self.comment_box = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
								self.comment_box.send_keys(comm[randint(0,9)])
								self.comment_box.send_keys(Keys.ENTER)
								#time.sleep(1)
								#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
								#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
								#else:
								#	comments += 1
								comment+= 1
								print(username + ' commented correctly AF')
								time.sleep(uniform(0.5,2))

						time.sleep(uniform(1,2))
						for i in range(1,randint(2,10)):
							self.driver.find_element_by_link_text('Next').click()
							time.sleep(uniform(0.5,3))
				else:
					self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button/svg')
					print('drop event')
			except Exception as e:
				print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
				print("-------DON'T PANIC, STILL WORKING-------")
				continue

		print('Liked {} photos.'.format(likes))
		print('Commented {} photos.'.format(comments))
		print('Followed {} new people.'.format(followed))
		print('supmate')

igbot(account[ale], password[ale]).newfollow(hashtag_list)
