  
import speech_recognition as sr  
                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Please enter your address. It can be a street number with the city name or postal code:")                                                                                   
    audio = r.listen(source)   
GCS = r"""{
  "type": "service_account",
  "project_id": "ad06",
  
"private_key_id": "149fcdbe71ecc1e775200000000000000000000000",
  
"private_key": "-----BEGIN PRIVATE KEY-----\JdVOYUdhJcoIe/CjjFpNiHSKaAnqejaGLA5a\n-----END PRIVATE KEY-----\n",
  "client_email": "s@ad06.iam.gserviceaccount.com",
  "client_id": "65498744974",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",


  "client_x509_cert_url": 
"https://www.googleapis.com/robot/v1/metadata/x509/40ad06.iam.gserviceaccount.com"
}
"""
try:
    #print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
    k=r.recognize_google_cloud(audio, credentials_json=GCS)
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
