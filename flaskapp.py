from flask import Flask, request, render_template
import subprocess, time

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("root.html")

@app.route("/echo", methods=['POST'])
def echo():
	createuser=subprocess.Popen('aws iam create-user --user-name ' + str(request.form['text']), shell=True)
	time.sleep(4)
	wait=subprocess.Popen('aws iam user-exists --user-name ' +str(request.form['text']), shell=True)
	addgroup=subprocess.Popen('aws iam add-user-to-group --user-name ' + str(request.form['text']) + ' --group-name workshopGrp', shell=True)
	createpass=subprocess.Popen('aws iam create-login-profile --user-name ' + str(request.form['text']) + ' --password hackpsu', shell=True)
	return render_template("confirmationpage.html", username=str(request.form['text']))
	#return "User " + str(request.form['text']) +  ' has been created. Your password is: hackpsu <br> Log into the AWS environment at <a href="https://hackpsu.signin.aws.amazon.com/console"> https://hackpsu.signin.aws.amazon.com/console </a>'

#add arns to iam policies

if __name__ == "__main__":
	app.run(debug=True)