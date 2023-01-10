from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['POST', 'GET'])
def push_image():
    # 要是不知道信息在哪儿，都打印出来完事
    postfrom = request.form
    postvalues = request.values
    postjson = request.json
    print(postfrom )
    print(postvalues )
    print(postjson )
    return ok


if __name__ == '__main__':
    # 这里隐去了我的IP和端口
    app.run(host='10.6.200.51', port=23123)
    #app.run()
