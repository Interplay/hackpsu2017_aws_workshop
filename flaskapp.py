from flask import Flask, request, render_template
import subprocess, time

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html", jquerycdn='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js', bootstrapjs='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js', bootstrapcss='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-beta/css/bootstrap.min.css')

@app.route("/echo", methods=['POST'])
def echo():
	createuser=subprocess.Popen('aws iam create-user --user-name ' + str(request.form['text']), shell=True)
	time.sleep(4)
	wait=subprocess.Popen('aws iam user-exists --user-name ' +str(request.form['text']), shell=True)
	addgroup=subprocess.Popen('aws iam add-user-to-group --user-name ' + str(request.form['text']) + ' --group-name workshopGrp', shell=True)
	createpass=subprocess.Popen('aws iam create-login-profile --user-name ' + str(request.form['text']) + ' --password hackpsu', shell=True)
	return "User " + str(request.form['text']) +  ' has been created. Your password is: hackpsu <br> Log into the AWS environment at <a href="https://hackpsu.signin.aws.amazon.com/console"> https://hackpsu.signin.aws.amazon.com/console </a>'

if __name__ == "__main__":
	app.run(debug=True)

# To Do
# find a way to get html of the pages looking nicer
# see if i can add css to reposition elements
# html head equivalents