# import Flask module
from flask import Flask, abort, jsonify, request

# import configurations variables
from instance.config import app_config

# define create_app to create and return Flask app
def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")

	# requests list
	requests = [
		{
			"id": 1,
			"title": "Leaking pipe",
			"description": "I have a busted water pipe in my bathroom. Its has been leaking for a week",
			"location": "Kisumu",
			"approved": False,
			"rejected": False,
			"resolved": False,
			"created_by": "Edwin"
		}
	]

	# accounts list
	accounts = []

	@app.route("/users/api/v1.0/requests/", methods=["POST"])
	def create_request():
		if request.json:
			req = {
				"id": requests[-1]["id"] + 1,
				"description": request.json.get('description', ''),
				"location": request.json.get('location', ''),
				"approved": False,
				"rejected": False,
				"resolved": False,
				"created_by": request.json.get('created_by', '')
			}
			requests.append(req)
			return jsonify({
				"id": req["id"],
				"description": req["description"],
				"location": req["location"],
				"approved": req["approved"],
				"rejected": req["rejected"],
				"resolved": req["resolved"],
				"created_by": req["created_by"]
			}), 201

	@app.route("/users/api/v1.0/account/register/", methods=["POST"])
	def create_account():
		if request.json:
			user = {
				"firstname": request.json.get('firstname', ''),
				"lastname": request.json.get('lastname', ''),
				"email": request.json.get('email', ''),
				"password": request.json.get('password', ''),
				"confirm_password": request.json.get('confirm_password', '')
			}
			accounts.append(user)
			return jsonify({
				"message": "Your account was created successfully."
			}), 201

	return app