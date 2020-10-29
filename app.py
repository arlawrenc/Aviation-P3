from flask import Flask, render_template, redirect, jsonify
import getFlight

app = Flask(__name__)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


# @app.route("/", methods=['POST', 'GET'])
@app.route("/")
def index():
    airportList = ['BOS','DCA','DEN','DFW','EWR','FLL','LGA','MIA','MCO','ORD']
    deptTime = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']
    return render_template('index - JT.html', airports=airportList, hours=deptTime)

@app.route('/predictor/<selDate>/<selHour>/<selAirport>')
def predictor(selDate, selHour, selAirport):
#    varYY = selDate[0:4]
#    varMM = selDate[5:7]
#    varDD = selDate[8:10]
#    varTime = selHour + ":00"
    varDateTime = selDate[8:10] + "/" + selDate[5:7] + "/" + selDate[0:4] + " " + selHour + ":00"
    print(varDateTime)
    probality = getFlight.predict_delay(varDateTime,selAirport)
#    probality = getFlight.predict_delay('28/10/2020 15:00:00',origin)
#    probality = getFlight.predict_delay('28/10/2020 15:00:00','BOS')
#    return jsonify("this is the predictor decorator")
#   return jsonify(f"Predictor values: {varDateTime} {selAirport}")
    return jsonify(f"Probability: {round(probality,2)*100}%")
    

@app.route("/monthly_graph/<selDate>/<selHour>/<selAirport>")
def monthly_graph(selDate, selHour, selAirport):
    print(selHour + ':00', selAirport)
    myValues = (getFlight.predict_delay('01/11/2020 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/12/2020 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/01/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/02/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/03/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/04/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('01/05/2021 ' + selHour + ':00', selAirport))
    return jsonify(myValues)

@app.route("/season_graph/<selDate>/<selHour>/<selAirport>")
def season_graph(selDate, selHour, selAirport):
    print(selHour + ':00', selAirport)
    myValues = (getFlight.predict_delay('22/12/2020 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('22/03/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('22/06/2021 ' + selHour + ':00', selAirport),
    getFlight.predict_delay('22/09/2021 ' + selHour + ':00', selAirport))
    return jsonify(myValues)
    
   

if __name__ == "__main__":
    app.run(debug=True)