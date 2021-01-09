# Installation

Before Procedding further make sure that you have python3 installed on your system, if not then you can download it easily from microsoft store

**Installing Libraries**

Download the Repo


![download]()

open command prompt by simply typing cmd in your windows search bar 
and make your way into the folder where you download the zip file, extract the zip file and
then run the below command in your command prompt to install the required libraries

`pip install -r requirements.txt`

![requirements](/images/requirements.png)

**Downloading Web Driver**

As this bot is created using selenium it  requires an Chrome Based Web driver to work.

Howerever webdriver is alredy included in the repo if it does not work then you can proceed with further instructions


You can download chromedriver version 87.0.4280.88 for your OS from [here](https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.88/)

If the bot throws an error regarding the complablity version of web driver you can download other version from [here](https://chromedriver.chromium.org/downloads)

Extract the chromedriver.zip file and place the chromedriver.exe file in the same folder containing the bot

# Usage

**Specifying Credentials**

Open the main.py using notepad or an editor and replace the below shown feilds with your credentials

![credentials](/images/Credentials.png)

you need to replace abc@gmail.com by your email and password by your password

***do***  ***not*** ***remove*** ***those*** ***doubble*** ***quatation*** ***marks***

Now you need to enter your Google meet link in the meeting.txt file

![meeting](/images/meeting.png)

Replace the Given meet link with your preffered meet link

**Running The Bot**

Now you are all set to go open command prompt and make your way to the folder containing the bot and then run the given command

`python3 main.py`

![run](/images/run.png)


Now you shold see an chrome window popping up and entering your credentials automatcally ;)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
More features like scheduling your meeting and setting up your Time-table will be added soon.
Then you can run the script on an RDP and relax while the bot takes care of your attendence

If you liked it do not forget to star my repository
