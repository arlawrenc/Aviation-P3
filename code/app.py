from flask import Flask, render_template, redirect

app = Flask(__name__)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    airportList = ['BOS','DCA','DEN','DFW','EWR','FLL','LGA','MIA','MCO','ORD']
    deptTime = ['01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00']
    return render_template('index.html', airports=airportList, hours=deptTime)
#    return render_template("index.html")

#@app.route('/', methods=['GET'])
#def dropdown():
#   airportList = ['BOS','DCA','DEN','DFW','EWR','FLL','LGA','MIA','MCO','ORD']
#   deptTime = ['01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','24:00']
#   return render_template('index.html', airports=airportList, hours=deptTime)
   
@app.route("/#data")
def data():
#    flight = "Test Flight"
#    return render_template("index.html#fltData")
    return render_template('index.html',message="Some text")

if __name__ == "__main__":
    app.run(debug=True)