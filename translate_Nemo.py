import httplib2
import json
import urllib
from  twilio.rest import TwilioRestClient

GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?key=AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk&source=en&target="
ACCOUNT_SID = "ACe52de0823ec698f8c793b393b51b9d65"
AUTH_TOKEN = "2bf65d5c10e520123278195ff3cddd4d"



text = ["Everything is Awesome","Everything is cool when you are part of a team","Teamwork makes the dreamwork.","This is the last string"]
translatedText1 = []


#function for the google translate API
def googleTranslate(sentences, language):
    my_url_translate = TRANSLATE_URL + language

    my_url_translate += '&q=' + '&q='.join(map(urllib.quote, sentences))

    url = my_url_translate
    http = httplib2.Http()
    response, body= http.request(url, "GET")
    parsed_body = json.loads(body)

    print (parsed_body)

#loop so that way you are going through array of text and data in entire array more than one time.
    translatedText += map()

    for i in text:
        translatedText = parsed_body['data']['translations'][0]['translatedText']
        print translatedText
        translatedText1.append(translatedText)

    return translatedText1

#function using twilio API and using code to make it easier to sed message by setting parameters
def twilio (to, message, reciever, language):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
    to = to,
    from_ = reciever,
    body = googleTranslate(message, language))

#calling the user twilio function to initialize the entire
twilio("+14159391162", ["Everything is Awesome!!!",  "Everything is cool when you are part of a team!"], "+18173857835", "ja")
