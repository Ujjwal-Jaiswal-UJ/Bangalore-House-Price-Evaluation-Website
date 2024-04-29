from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/fetch_loc_name', methods=['GET'])
def fetch_loc_name():
    response = jsonify({
        'locations': util.fetch_loc_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/forecast_home_price', methods=['GET','POST'])
def forecast_home_price():
    tot_sqft = float(request.form['total_sqft'])
    loc = request.form['location']
    no_bhk = int(request.form['bhk'])
    no_bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_evaluated_price(loc,tot_sqft,no_bhk,no_bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For House Price Evaluation...")
    util.load_saved_guide()
    app.run()