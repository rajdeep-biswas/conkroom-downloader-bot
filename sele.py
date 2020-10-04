#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().system('pip install requests')


# In[3878]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from time import sleep


# In[2879]:


driver = webdriver.Chrome("C:\\Users\\I516992\\Downloads\\chromedriver.exe")


# In[2642]:


i = 171
j = 1


# In[2892]:


url = "https://my.headspace.com/play/" + str(i)


# In[3231]:


driver.get(url)


# In[ ]:





# In[3792]:


try:
    driver.find_element(By.XPATH, "//div[@aria-label='Go to meditation session']").click()
except:
    print("no skip")


# In[3794]:


try:
    driver.find_element(By.XPATH, "//button[@aria-label='play meditation']").click()
except:
    print("no click")


# In[4092]:


audioUrl = driver.find_element(By.XPATH, "//audio[@data-component='media-item-player']").get_attribute("src")


# In[3990]:


title = driver.find_element(By.XPATH, "//div[@data-component='card-header']//p").text


# In[3991]:


# fileName = "managing anxiety day " + str(j)
fileName = title + driver.find_element(By.XPATH, "//h3[@class='css-mjnpby']").text.replace('/', ' of ')

print(fileName)


# In[4093]:


r = requests.get(audioUrl)


# In[4094]:


with open("C:\\edpes\\downloads\\" + fileName + ".mp3",'wb') as f: 
    f.write(r.content) 


# In[3876]:


try:
    circle = driver.find_element(By.XPATH, "//div[@class='css-wqsnk1']")
except:
    print("no")
try:
    circle = driver.find_element(By.XPATH, "//div[@class='css-nueiy0']")
except:
    print("no")
try:
    circle = driver.find_element(By.XPATH, "//div[@class='css-1rn504n']")
except:
    print("no")
    
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(circle, 108, 20)
action.click()
action.perform()


# In[3877]:


driver.find_element(By.XPATH, "//div[@aria-label='Finish session']").click()


# In[3870]:


try:
    driver.find_element(By.XPATH, "//div[@aria-label='maybe later']").click()
except:
    print("no later")


# In[3894]:


body = driver.find_element(By.XPATH, "//div[@data-component='hero-section']")
action = webdriver.common.action_chains.ActionChains(driver)

action.move_to_element_with_offset(body, 280, 340)
action.click()
action.perform()     


# In[ ]:





# In[ ]:


for i in range(300):
    try:
        driver.find_element(By.XPATH, "//div[@aria-label='Go to meditation session']").click()
    except:
        print("no skip")
        
    sleep(2)
        
    try:
        driver.find_element(By.XPATH, "//button[@aria-label='play meditation']").click()
    except:
        print("no click")
    
    sleep(2)
    
    audioUrl = driver.find_element(By.XPATH, "//audio[@data-component='media-item-player']").get_attribute("src")
    title = driver.find_element(By.XPATH, "//div[@data-component='card-header']//p").text
    fileName = title + ' ' + driver.find_element(By.XPATH, "//h3[@class='css-mjnpby']").text.replace('/', ' of ')
    
    print(fileName)
    
    r = requests.get(audioUrl)
    with open("C:\\edpes\\downloads\\" + fileName + ".mp3",'wb') as f: 
        f.write(r.content)
    
    try:
        circle = driver.find_element(By.XPATH, "//div[@class='css-wqsnk1']")
    except:
        print("no")
    try:
        circle = driver.find_element(By.XPATH, "//div[@class='css-nueiy0']")
    except:
        print("no")
    try:
        circle = driver.find_element(By.XPATH, "//div[@class='css-1rn504n']")
    except:
        print("no")

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(circle, 108, 20)
    action.click()
    action.perform()
        
    sleep(20)

    driver.find_element(By.XPATH, "//div[@aria-label='Finish session']").click()
        
    sleep(3)

    try:
        driver.find_element(By.XPATH, "//div[@aria-label='maybe later']").click()
    except:
        print("no later")
        
    sleep(3)

    body = driver.find_element(By.XPATH, "//div[@data-component='hero-section']")
    action = webdriver.common.action_chains.ActionChains(driver)

    action.move_to_element_with_offset(body, 280, 340)
    action.click()
    action.perform()
        
    sleep(3)


# In[3958]:





# In[4107]:


singleTitles = [
'Eating with Your Senses',
'Eating With Appreciation',
'Eating without Distraction',
'Cooking',
'Eating',
'Calm Your Nerves',
'Add Some Joy',
'Hit Reset',
'Connect With the World',
'Connect With Your Body',
'Get Motivated',
'Walk Off Frustration',
'Walking in the City',
'Walking at Home',
'Walking in Nature',
'Run Easy',
'Run Smart',
'Keep Running',
'Running',
'Cycling',
'Commuting',
'Vacation',
'Business Travel',
'Burned Out',
'Feeling Overwhelmed',
'Flustered',
'Losing Your Temper',
'Panicking',
'In Pain',
'Early Mornings',
'Waking Up',
'Sleeping',
'Falling Back to Sleep',
'Goodnight',
'Mindful Cleaning for Sleep',
'Mindful Walking for Sleep',
'Alone Time',
'Reset',
'End of Day',
'For the Weekend',
'Stressed',
'Frustrated',
'Under the Weather',
'Creative Writing',
'Gardening',
'Housework',
'Managing Conflict',
'Listening to Others',
'Mindful Tech',
'Presentations',
'Taking a Break',
'Interviews',
'Fear of Flying',
'Difficult Conversations',
'Exam Prep',
'Competition',
'Concentration',
'Motivation',
'Training',
'Rehab',
'Recovery',
'Analysis',
'Communication',
'Switching Off',
'Noting',
'Deep Breathing',
'Light Visualization',
'Sunday Scaries',
'Enjoy the Weekend'
]

len(singleTitles)


# In[4108]:


for singleTitle in singleTitles:
    driver.find_element(By.XPATH, "//div[@aria-label=\' " + singleTitle + " \']").click()
    
    singleTitle = driver.find_element(By.XPATH, "//div[@id='main-content']//h1").text
    sleep(1)
    driver.find_element(By.XPATH, "//div[contains(@aria-label,'Change duration.')]").click()
    driver.find_element(By.XPATH, "//div[@aria-label='Select duration']//p[@tabindex='0'][last()]").click()
    driver.find_element(By.XPATH, "//div[@tabindex='1']").click()
    
    sleep(2)
    
    singleAudioUrl = driver.find_element(By.XPATH, "//audio[@data-component='media-item-player']").get_attribute("src")
    r = requests.get(singleAudioUrl)
    with open("C:\\edpes\\downloads\\" + singleTitle + ".mp3",'wb') as f: 
        f.write(r.content)
    print("done:", singleTitle + ".mp3")
    driver.execute_script("window.history.go(-1)")
    sleep(1)
    driver.execute_script("window.history.go(-1)")
    sleep(1)


# In[4103]:


animations = [
"Getting Started",
"Changing Perspective",
"Letting Go of Effort",
"Remember the Blue Sky",
"Accepting the Mind",
"Take a Tour of Headspace",
"About Headspace for Kids",
"Am I Doing It Right",
"Am I Making Progress",
"Get Back on the Wagon",
"Free Your Mind",
"Mind, Body, Speech",
"Thinking About Thinking",
"Learning a Skill",
"Hole in the Road",
"Monkey Mind",
"Beginner's Mind",
"Elephant Slow and Steady",
"Impatient Yogi",
"Dark Side of the Mind",
"Can't Control the Waves",
"Polishing a Pan",
"Letting Go",
"Planting a Seed",
"Happiness of Others",
"Impermanence and Change",
"Precious Human Life",
"Shared Human Condition",
"Cause and Effect",
"Quiet Confidence",
"Big Mind, Small Mind",
"Pointing at the Moon",
"Where are Thoughts",
"Waves and the Ocean",
"Emptiness",
"Limitless Mind",
"Illusion of Self",
"Compassion and Awareness",
"Body Scan",
"Visualization",
"Noting",
"Loving Kindness",
"Reflection",
"Skillful Compassion",
"Resting Awareness",
"Focused Attention"
]


# In[4042]:


id -= 5


# In[4044]:


emberId = 4680

while True:
    driver.find_element(By.XPATH, "//div[@id=\'ember" + str(emberId) + "\']").click()

    animation = animations[id]
    sleep(3)
    animVideoUrl = driver.find_element(By.XPATH, "//video[@data-component='media-item-player']").get_attribute("src")
    r = requests.get(animVideoUrl)
    with open("C:\\edpes\\downloads\\" + animation + ".mp4",'wb') as f: 
        f.write(r.content)
    print("done:", animation + ".mp4")
    
    driver.find_element(By.XPATH, "//div[@aria-label='Close video']").click()
    sleep(2)
    
    emberId += 4
    id += 1


# In[4073]:





# In[4072]:





# In[ ]:




