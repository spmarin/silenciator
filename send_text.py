import datetime
import logging
import requests

LOG_FILENAME = 'silenciator.log'
logger = logging.getLogger('silenciator')
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

def send_text(text):
    payload = {'msg': text, 'r': 0, 'g': 0, 'b': 255}
    r = requests.post('http://10.95.32.192:8080/texts', json=payload)
    #if r.status_code == 200:
    #    logger.info("time=%s | Text to the wall sent: %s", datetime.datetime.utcnow(), text)
    #else:
    #    logger.error("time=%s | Text to the wall has failed: %s", datetime.datetime.utcnow())
