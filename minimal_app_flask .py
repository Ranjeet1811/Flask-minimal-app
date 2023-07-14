from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return """Welcome to Ranjeet IT Services 
    I am providing onsite services Computer Hardware software and Networking """


# only for addition operation

'''@app.route("/add",methods= ['POST'])
def add():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        body = request.json
        return jsonify({'result':body['num1']+body['num2']})
    else:
        return 'Content- Type not supported '''


@app.route("/compute", methods=['GET', 'POST'])
def computer():
    if request.method == 'GET':
        return jsonify('supported operations: add, subtract, divide, multiply')

    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        print(content_type)
        if content_type == 'application/json':
            body = request.json
            print(body)
            return jsonify({'result': perform_operation(body['num1'], body['num2'], body['operation'])})
        else:
            return "Content- Type not supported! "



# service layer
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "invalid operation or number "


@app.route("/my", methods=['GET', 'POST'])
def mylogic():
    if request.method == 'GET':
        return ("You Can perform add,subtract,divide,multiply")
    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        resp = ({'result': perform_operation(data['num1'], data['num2'], data['operation'])})
        print(resp)
        # return "success"
        return jsonify(resp)





if __name__ == '__main__':
    app.run(host='localhost', port='5426')
