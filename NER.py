import thulac
import flask
from flask import Flask, request, jsonify, make_response
from flask_cors import *
from flask import url_for
from flask import json, render_template
import json
import main

app=Flask(__name__)

def tagging(content):
    thu1 = thulac.thulac()
    text = thu1.cut(content, text=True)
    return text
CORS(app, supports_credentials=True)

@app.route("/POSTagging/", methods=["POST", "OPTIONS"])
def POStagg():
    if request.method == 'OPTIONS':
        res = flask.make_response()
        print("options response done!")
    if request.method == "POST":
        json_dict = request.get_json()
        content = json_dict["content"]
        tag_result = tagging(content)
        tag_result1 = {"success": "true", "msg": tag_result}
        result1 = json.dumps(tag_result1, ensure_ascii=False)
        return result1
    else:
        return """<html><dody>
        Something went horribly wrong
        </body></html>"""

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