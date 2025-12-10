import os

if(not os.getenv('ANYAPI_KEY')):
    print("ANYAPI_KEY not yet set.")
    os.environ['ANYAPI_KEY'] = '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'
else:
    print("ANYAPI_KEY already set.")
