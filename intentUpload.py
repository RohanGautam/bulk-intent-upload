import csv, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


browser=webdriver.Firefox()
browser.get(r'https://console.dialogflow.com/api-client/#/agent/8a69754c-1511-4c6a-b282-e4ffa53e6100/intents')
inp=input('Enter "Y/y" after you have logged into dialogflow console: ').lower()

createIntentUrl='//*[@id="link-create-intent"]'
intentNameUrl='//*[@id="entity-name"]'
trainingPhrasesUrl='/html/body/div[1]/div[2]/div/div/div/section/div/div[3]/div/div/div[1]/intent-user-says-editor/div[2]/div[1]/user-says-editor/div/div/div[1]/div'
hideTrain='/html/body/div[1]/div[2]/div/div/div/section/div/div[3]/div/div/div[1]/intent-user-says-editor/div[1]/i'
responsesUrl='/html/body/div[1]/div[2]/div/div/div/section/div/div[3]/div/div/div[3]/div[2]/intent-rich-response/div/div/div/div/md-card/md-card-content/intent-response-content/intent-text-response/div/div/div/form/div[1]/div/div[2]/div/textarea'
saveIntentUrl='//*[@id="multi-button"]'

intentName='abc123'
trainingPhrase='training phrase1'
response='response'

def makeIntent(intentName,trainingPhrase,response):
    browser.find_element_by_xpath(createIntentUrl).click()
    #name intent
    browser.find_element_by_xpath(intentNameUrl).send_keys(intentName)
    browser.find_element_by_xpath(intentNameUrl).send_keys(Keys.ENTER)
    # enter training phrase
    train = browser.find_element_by_xpath(trainingPhrasesUrl)
    train.send_keys(trainingPhrase)
    train.send_keys(Keys.ENTER)
    #scroll down & hide train
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # browser.find_element_by_xpath(hideTrain).click() # not hiding train for now
    # enter response phrase
    input('have u clicked on response?: ')
    resp = browser.find_element_by_xpath(responsesUrl)
    resp.click()
    resp.send_keys(response)
    resp.send_keys(Keys.ENTER)
    # save the intent: takes around 5 seconds
    browser.find_element_by_xpath(saveIntentUrl).click()
    time.sleep(5)


# if inp=='y':
    # create intent
pattern=r'Where is (.*) \?'
with open('../bulk-LT_TR-2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count>=267:
            row=[x.replace(u'\u200b','') for x in row]
            row=[x.replace(u'\xa0',' ') for x in row]
            intentName = 'Location - '+re.findall(pattern,row[0])[0]
            trainingPhrase = row[0][:768]
            response = row[1][:4000]
            makeIntent(intentName,trainingPhrase,response)
        line_count+=1









