# Bulk intent upload to DialogFlow:
Simple bulk intent upload in Dialogflow - google's chatbot creation platform
## Note: I'm using acronym upload as an example- you can extend this functionality to whatever!

# Some file information:
* `intentUpload.py` is the shitty version, wherein I used selenium webdriver to automate the clicking and entering of text directly into the Dialogflow console, to create new intent._This is very slow and painful and **not recommended**_
. It's just here for future me to refer back, if I need to.
* `intentUpload_V2.py` is the better one. The steps to execute it are given below, with an example.

# The bulk intent upload
### Export the current agent as a `.zip` file.
Extract it, and observe the intents folder. Each intent has two `.json` files associated with it: `{intentName}.json` and `{intentName}_usersays_en.json`. We aim to reproduce these using `fake.json` and `fake_usersays_en.json` as templates.

Refer to the image below:

![export and import screen](https://user-images.githubusercontent.com/17317792/56147934-d5be3600-5fdb-11e9-9907-a21e2ad120c5.png)


### Run `intentUpload_V2.py`
*make sure you have the `acronyms` folder created in the same directory* (tho this can be easily also done in python). This uses `fake.json` and `fake_usersays_en.json` as templates to generate two files for each intent.


### Upload all the `.json` files generated into the intents folder (in the extracted `.zip` of the agent)


###  Zip the folder containing the intents folder, and select the `Import from zip` option in the dialogflow console 
This is under "export and import" in settings of the agent.
Since there are no ID's for what we uploaded, they will be generated automatically by Dialogflow.


### ..and this is what the result is!
![the dialogflow console after bulk upload](https://user-images.githubusercontent.com/17317792/56147386-c094d780-5fda-11e9-846e-f6d8249f0fd9.png)

### There's many ways you can thus make mass changes to intent and entity structure through there files... this was just a simple use case. Have fun with your chatbot!
