from twython import Twython
from twython import TwythonStreamer



class MyStreamer(TwythonStreamer):
    counter = 00
    def on_success(self,data):
        if 'text' in data:
            self.counter = self.counter+1
            if self.counter > 2:
                print("Ian G. Harris is popular!")

#API Key                :
C_KEY = "Pass"
#API Secret Key         :
C_SECRET = "Pass"
#Access token           :
A_TOKEN = "Pass-Pass"
#Access token secret    :
A_SECRET = "Pass"

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
stream.statuses.filter(track="Ian G. Harris")
