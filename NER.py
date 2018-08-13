import flask
from flask import Flask
from flask import jsonify
from flask import url_for
from flask import request
from flask import json,render_template
import main
app=Flask(__name__)

@app.route('/test',methods=['POST','GET'])
def sendtest():
    if request.method == 'GET':
        data = request.get_json()['sentence']
        print(data)
        json_str = json.dumps(data)
        print(json_str)
        return ('successCallback(' + json_str + ');')
    if request.method=='POST':
        rev=request.get_json()['sentence']
        return jsonify({'testResult':rev})
    else:
        return render_template('index.html')

@app.route('/index',methods=['POST','GET','OPTIONS'])
def posttest():
    if request.method == 'OPTIONS':
        res = flask.make_response()
        print("options response done!")
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        json_str = json.loads(data)
        #dic={'test':'ceshi','url':18}
        print(json_str)
        sentence = json_str['sentence']
        PER,LOC,ORG = main.demotest(sentence)
        json_re = {'PER':PER,'LOC':LOC,'ORG':ORG}
        print(json_re)
        res = flask.make_response(jsonify(json_re))
        print(res)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return res


if __name__=='__main__':
    app.run(debug=True)