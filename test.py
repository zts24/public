import os
import base64

ins1 = 'ZWNobyAnSGVsbG8gV29ybGQhJw=='

print(str(base64.b64decode(ins1).decode('utf-8')))
os.system(str(base64.b64decode(ins1).decode('utf-8')))