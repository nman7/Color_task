from flask import Flask, jsonify, request
from color import *

app = Flask(__name__)


@app.route('/run', methods=['POST', 'GET'])
def home() :
	try :
		if request.method == 'POST' :
			ack = request.files['image'].read()
			ack = str(ack).split("'")[1]
			#print("path used in app.py",ack)
			domi_dictionary = run_for_results(ack)
			print("SUCCESS")
			return app.make_response((jsonify(domi_dictionary), 200))
	except :
		return app.make_response((jsonify({"message": "BAD REQUEST"}),400))

	return app.make_response((jsonify({"message": "PLEASE SEND IMAGE"}),200))


app.run(debug=True)