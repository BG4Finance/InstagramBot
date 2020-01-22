# InstagramBot


### 10 minutes easy setup process 
1. Install Google Chrome & Download ChromeDriver Binary
	* Install [Google Chrome](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)(leave it in deafult path)
	* Download [ChromeDriver Binary](https://sites.google.com/a/chromium.org/chromedriver/getting-started) and place the file in a dedicated folder (let's call it ig_bot folder)

2. Install Python [Python Download](https://www.python.org/downloads/)
	
3. Open a Prompt command / Terminal in in the ig_bot folder ([How to?](https://www.groovypost.com/howto/open-command-window-terminal-window-specific-folder-windows-mac-linux/))
	* Type in `python -m pip install selenium` and hit ENTER key

4. Download ig_bot.py and secret.py from this repostiory and move them to ig_bot folder

5. Now you ready to go

----
 
First of all open secret.py and write in your user and password, save and close the file. Now open ig_bot.py file and at line 13 write in the brackets your path down to chromedriver, it should look like `self.driver=webdriver.Chrome("/User/Desktop/Bots/ig_bot/chromedriver")`.


Now you are ready to your firs run, you can set the target hashtags by modifying and even extending the hashtag_list at line 39.  
To run the code just open the Prompt command in ig_bot folder by simply repeating the third step of the setup process but this time type in: `Python ig_bot.py` and hit ENTER key.


After the first run, if you want to update the user followed log after every run, go to line 40:  
As explained in line 41, put an hash symbol `#` at the beginning of line 40 (`#` stands for comment, the line following this symbol will not be considered during the script run) and erase the hash symbol at line 42 and 43.