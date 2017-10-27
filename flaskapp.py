from flask import Flask, request
import subprocess, time

app = Flask(__name__)

@app.route("/")
def hello():
	return '<form action="/echo" method="POST"><input name="text"><input type="submit" value="Echo"></form>'

@app.route("/echo", methods=['POST'])
def echo():
	createuser=subprocess.Popen('aws iam create-user --user-name ' + str(request.form['text']), shell=True)
	time.sleep(10)
	wait=subprocess.Popen('aws iam user-exists --user-name ' +str(request.form['text']), shell=True)
	addgroup=subprocess.Popen('aws iam add-user-to-group --user-name ' + str(request.form['text']) + ' --group-name workshopGrp', shell=True)
	createpass=subprocess.Popen('aws iam create-login-profile --user-name ' + str(request.form['text']) + ' --password hackpsu', shell=True)
	return str(request.form['text']) +  " created"

if __name__ == "__main__":
	app.run(debug=True)