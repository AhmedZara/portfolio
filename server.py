from flask import Flask,request,jsonify,render_template, url_for

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/landing',methods=['GET'])
def landing():
    return render_template('landing.html')

@app.route('/contactme',methods=['GET','POST'])
def contactme(): 
   return jsonify({"firstname":request.form['firstname'], "lastname":request.form['lastname']})

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')