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
		self.driver.implicitly_wait(10)
		self.driver.get('https://www.instagram.com/accounts/login/')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name('username').send_keys(user)
		self.driver.find_element_by_name('password').send_keys(pw)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
		self.driver.implicitly_wait(10)
		#Find that annoying notification button and say no!
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(uniform(1,5))
		#database of the following people of each account
		self.dbname = '{}_following_list.csv'.format(user)
		try:
			self.following_list= pd.read_csv(self.dbname,delimiter=',').iloc[:,1]
			print('Existing User')
		except FileNotFoundError as e:
			file_status = 'missing'
			self.following_list = pd.DataFrame(columns=['users'])
			print('New User Onboarding')
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
		new_followed = []
		tag = 0
		followed = 0
		likes = 0
		comments = 0
		#10 Comments
		comm = ['Wow, amazing! you should check out @hylus__ ',"Aaahw, that's something! You should check out @hylus__ ", "Damn! S/O to @hylus__ ", "Looove it! go check @hylus__ ", "Hey where u from? Do you know about @hylus__ ", "Yoooo, @hylus__ is out there ", "That's something else... like @hylus__ ","I would like to ride it like i ride my @hylus__ ", "I kind like it, but @hylus__ is way better", "Hey, where u at? Do you know about @hylus__ ? "]

		for tag in hashtag_list:
			#Go to explore hashtag page
			self.driver.get('https://www.instagram.com/explore/tags/'+tag+'/')
			time.sleep(1)
			#Open a random foto foto out of first 9
			self.thumb = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[{0}]/div[{1}]/a/div'.format(randint(1,3),randint(1,3)))
			self.thumb.click()
			time.sleep(2)
			try:
				for x in range(1,60):
					#Identifiy the user
					self.driver.implicitly_wait(10)
					username = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
					#Interactions start here!
					#Should I comment?
					if randint(0,100) > 70:
						time.sleep(uniform(2,5))
						self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div[1]/form/textarea').click()
						self.comment_box = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div[1]/form/textarea')
						self.comment_box.send_keys(comm[randint(0,9)])
						time.sleep(1)
						self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
						self.driver.implicitly_wait(10)
						#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
						#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
						#else:
						#	comments += 1
						comments += 1
						print(username + ' commented correctly NF')
						time.sleep(uniform(1,3))

					#Should I like?
					if randint(0,100) > 65:
						time.sleep(uniform(0.5,2))
						self.driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg').click()
						#time.sleep(1)
						#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
						#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
						#else:
						#	likes += 1
						likes += 1
						print(username + ' liked correctly NF')
						time.sleep(uniform(0.5,2))

					#If account does not follow the user...
					if self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").text == "Follow":
						#Should I follow?
						if randint(0,100) > 75:
							time.sleep(uniform(2,3))
							self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
							#time.sleep(1)
							#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
							#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
							#else:
							#	new_followed.append(username)
							#	self.following_list.append(username)
							#	print(username + 'followed correctly')
							#	followed+=1
							print(username + ' ------------------ followed correctly')
							followed+=1
							# New following user names storing
							new_followed.append(username)
							self.following_list = pd.merge(self.following_list,pd.DataFrame([username], columns=['users']), how='outer')
							self.following_list.columns=['users']
							# Updating Following log
							updated_user_df = pd.DataFrame(self.following_list)
							updated_user_df.to_csv(self.dbname)
						time.sleep(uniform(0.5,3))

					else:
						print('{} already followed'.format(username))

					time.sleep(uniform(1,2))
					for i in range(1,randint(2,10)):
						self.driver.implicitly_wait(10)
						self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow").click()
						time.sleep(uniform(0.5,3))

			except Exception as e:
				print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
				print("-------DON'T PANIC, STILL WORKING-------")
				continue

		print('Liked {} photos.'.format(likes))
		print('Commented {} photos.'.format(comments))
		print('Followed {} new people.'.format(followed))
		print('supmate')

	def unfollow(self):
		for times in range(1,5):
			# Open profile page through profile pick
			self.driver.get('https://www.instagram.com/{}/'.format(self.user))
			time.sleep(4)
			fol_number = int(self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span').text)
			print(fol_number)
			self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a ').click()
			for i in range(1,15):
				time.sleep(2)
				self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child({0}) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button'.format(i)).click()
				time.sleep(0.5)
				self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()

hashtag_list = ['skateboard','tonyhawk', 'wall', 'design', 'board']
igbot(account[ale], password[ale]).newfollow(hashtag_list)
