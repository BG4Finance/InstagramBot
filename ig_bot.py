from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import strftime
from random import randint, uniform
import pandas as pd
from secret import name, pw

account = name
password = pw
class igbot:
	def __init__(self, user, pw):
		self.driver=webdriver.Chrome("YOUR UNIQUE PATH TO ig_bot FOLDER/chromedriver")
		time.sleep(1)
		self.driver.get('https://www.instagram.com/accounts/login/')
		self.user = user
		self.pw = pw
		time.sleep(1)
		self.driver.find_element_by_name('username').send_keys(user)
		self.driver.find_element_by_name('password').send_keys(pw)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
		time.sleep(2)
		#Find that annoying notification button and say no!
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(uniform(3,5))
		#Now we are in the IG homepage, let's move around

	def randomise(self):
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/button/div[1]').click()
		for i in range(0,100):
			time.sleep(uniform(3,25))
			self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[2]/div').click()

		self.driver.close()



	def newfollow(self):
		hashtag_list = ['travel','NewYork','weed','porn','sick','trap']
		prev_user_list = []
		#After the first run comment line 40 and uncomment the following two lines 42 and 43
		#prev_user_list= pd.read_csv('20200122_users_followed_list.csv',delimiter=',').iloc[:,1:2]
		#prev_user_list = list(prev_user_list['0'])
		new_followed = []
		tag = 0
		followed = 0
		likes = 0
		comments = 0
		#7 Comments
		comm = ['Wow, amazing!',"That's something", "Damn!", "Looove it!", "Hey where u from?", "Yoooo", "That's something else..."]

		for tag in hashtag_list:
			self.driver.get('https://www.instagram.com/explore/tags/'+ tag + '/')
			time.sleep(1)
			#Open first foto
			self.thumb = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
			self.thumb.click()
			time.sleep(2)

			try:
				for x in range(1,50):
					username = self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > h2 > a').text
					#Interactions start here!
					#If you are not following the user...
					if self.driver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button").text == "Follow":
						time.sleep(1) #Erasable
						if randint(0,100) > 70:
							time.sleep(uniform(2,3))
							self.driver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button").click()
							#time.sleep(1)
							#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
							#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
							#else:
							#	new_followed.append(username)
							#	prev_user_list.append(username)
							#	print(username + 'followed correctly')
							#	followed+=1
							new_followed.append(username)
							prev_user_list.append(username)
							print(username + ' ------------------ followed correctly')
							followed+=1
						time.sleep(uniform(0,3))

						if randint(0,100) > 120:
							time.sleep(uniform(2,5))
							self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
							self.comment_box = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
							self.comment_box.send_keys(comm[randint(0,6)])
							self.comment_box.send_keys(Keys.ENTER)
							#time.sleep(1)
							#if self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/h3").text == "Action Blocked":
							#	self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
							#else:
							#	comments += 1
							comments += 1
							print(username + ' commented correctly NF')
							time.sleep(uniform(0.5,2))

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

						if randint(0,100) > 120:
							time.sleep(uniform(1,3))
							self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
							self.comment_box = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
							self.comment_box.send_keys(comm[randint(0,6)])
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
			except:
				continue

		updated_user_df = pd.DataFrame(prev_user_list)
		updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d")))
		print('Liked {} photos.'.format(likes))
		print('Commented {} photos.'.format(comments))
		print('Followed {} new people.'.format(followed))
		print('supmate')

igbot(account[1], password[1]).newfollow()
