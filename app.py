from flask import Flask,request,Response

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route("/", defaults={"path": ""},methods=HTTP_METHODS)
@app.route("/<string:path>",methods=HTTP_METHODS)
@app.route("/<path:path>",methods=HTTP_METHODS)
def fallback(path):
    print(request.data)
    print(request.headers)
    print

    return  Response('',200, mimetype= 'x-application/octet-stream'  )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=11111)
