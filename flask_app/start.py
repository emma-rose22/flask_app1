from flask import Flask

'''
troubleshooting notes for later

Under Powershell, you have to set the FLASK_APP environment variable as follows:

$env:FLASK_APP = "webapp"

Then you should be able to run "python -m flask run" inside the hello_app folder. In other words, PowerShell manages environment variables differently, so the standard command-line "set FLASK_APP=webapp" won't work.
'''

#make a global flask object
app = Flask(__name__)

#set it to be the homepage 
@app.route('/')

#our app currently prints this
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()