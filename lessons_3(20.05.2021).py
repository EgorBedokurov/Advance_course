import random
import string

from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/random")
def get_random():
    #print(request.args)
    #print(request.args['var'])
    length = request.args.get('length', '10')
    if length.isdigit():
        length = int(length)
    else:
        return Response('Error: length is not a number')

    length = int(request.args.get('length', '10'))
    return ''.join(random.choices(string.ascii_lowercase, k=length))

app.run(debug=True, port=5001)