import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, jsonify
from time import strftime
import traceback
import py_modules.emp_details as edt

#translator module
import py_modules.py_translater as Ttrans
#mysqldb connection module
import py_modules.mysql_connection as my

# from wtf.app import app
app = Flask(__name__)

@app.route("/", methods = ['GET'])
@app.route("/home", methods = ['GET'])
def home():
    return render_template('home.html')

@app.route("/translate", methods = ['POST'])
def trans():
    # print request.method
    if request.method == 'POST':
      inptxt = request.form.get('inptxt')
      output = Ttrans.MyTranslater().TransText(inptxt)
      # user = request.form.json
    return jsonify({'output': output})

@app.route("/get_employee_data", methods = ['GET'])
def get_emp():
    contents = edt.Get_EDetls().Emp_dtls()
    return jsonify({'output': str(contents)})


#Logging request and response
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

#logging errors
@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return e.status_code

if __name__=="__main__":
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(debug=True)
