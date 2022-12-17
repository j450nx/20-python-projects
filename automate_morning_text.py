import schedule as schedule
import requests
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
      'phone': '+15555555555',
      'message': 'Time to wake up!',
      'key': 'textbelt',
    })
    print(resp.json())

# https://pypi.org/project/schedule/
# schedule.every().day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)