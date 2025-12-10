import os
import random
import pandas
import hashlib
from pathlib import Path


DATA_PATH = Path.cwd()
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) 
##CSV_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, 'csv'))
##IMG_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, 'img'))

## os.path.exists(CSV_DIR) or os.mkdir(CSV_DIR)   # works also for files


print('DATA_PATH',DATA_PATH, os.path.exists(DATA_PATH))
##print('SCRIPT_DIR',SCRIPT_DIR)

class ApiUtils():

    #classWide = {}
    ##apiStatusFile = 's.csv'
    ##apiFileStatus = 'busy'
    apiStatusDF = None

    def __init__(self, group='missing', envKey='ANYAPI_KEY'):  
      # ApiUtils.classWide = 1
      # self.instanceOnly = 2
      self.group = group
      self.envKey = envKey
      if(not ApiUtils.apiStatusDF):
         self.loadStatusDF()
      return None

    def loadStatusDF(self):
      return None 

    def inqApiKey(self, envKey='ANYAPI_KEY'): 
      if(not os.getenv(envKey)):
        print(str(envKey)+" not yet set.")
        os.environ[envKey] = str(envKey)+'_isNotYetSet'
      else:
        print(str(envKey)+" already set.")
      return os.getenv(envKey)

   
    def getApiKey(self, envKey='ANYAPI_KEY'):
        wholeStr = self.inqApiKey(envKey)
        allApiKeys = wholeStr.split(',')  
        bestApiKey = random.choice(allApiKeys)  #later search the key least used    
        return bestApiKey

    #csv pandas: ['group','envKey','apiKey',       # apiKey  -> hashed!!! crc = hashlib.sha256(hashString.encode()).hexdigest()[:10]
                            
    #             'callUsed','callLimit','callDelay',
    #             'sizeUsed','sizeLimit','sizeDelay',
    #             'lastCall','callSucess','callFail']


