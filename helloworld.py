import pyotp
import time

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        totp = pyotp.TOTP('JBSWY3DPEHPK3PXP')
        otp = totp.now() 
        return otp

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')

    


