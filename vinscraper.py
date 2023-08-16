import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from urllib.parse import parse_qs
from datetime import datetime

# prevent us looking like a bot by randomly generating a wait time between two given values
def randomWaitGenerator(start_value, end_value): 
    return random.randint(start_value*1000, end_value*1000)/1000 # multiply by 1000 and divide by 1000 to get a float instead of an int




# open chipex website
driver = webdriver.Firefox()
driver.get('https://chipex.co.uk/')

# open file containing registrations (each reg separated by new line)
input_file = open('reglist.txt', 'r')
data = input_file.read()
plates = data.splitlines() # list of registration plates from file

urlList = [] # list that will contain all the urls returned

for plate in plates:
    try:
        needs_click = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div/div/div/div/form/div[1]/div[9]/div/button') # stupid popup that needs to be closed
        needs_click.click()
        time.sleep(2) # need to wait after clicking the box or it still blocks the submit element
    except:
        print('no button to click')

    reg_input = driver.find_element(By.ID, 'reg_input')
    reg_submit = driver.find_element(By.CLASS_NAME, 'reg_submit')
    reg_input.send_keys(plate) 
    reg_submit.click()

    timeToSleep = randomWaitGenerator(5,8) #
    time.sleep(timeToSleep) # wait for page to load

    url = driver.current_url
    urlList.append(url) # append url to list
    
driver.quit()

now = datetime.now() # get datetime as of right now
now_string = now.strftime("%Y%m%d_%H%M%S") # create datetime string format YYYYMMDD_HHMMSS

filename = 'output_%s.txt' %(now_string) # create text file called output with the datetime appended
text_file = open(filename,'x') # open that file
text_file.write('VehReg, VIN') # write column headers
text_file.write('\n')

for item in urlList:
    parsed_url = urlparse(item) 
    vrn = parse_qs(parsed_url.query)['VRN'][0] # parse veh reg from query parameters
    vin = parse_qs(parsed_url.query)['VIN'][0] # parse vin from query parameters
    text_file.write('%s, %s' %(vrn,vin)) # write them in the format vehreg, vin
    text_file.write('\n')

text_file.close() # close file