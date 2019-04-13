from flask import Flask, request
from caesar import rotate_string
import string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="post">
      <label for="rot">Rotate by&colon;</label>
      <input value="0" id="rot" type ="text" name="rot"/>
        <textarea name="text"></textarea>
        <input type="submit"/>
      </from>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])

def encrypt():
    rots = int(request.form['rot'])
    rotated = request.form['text']
    return "<h1>" + rotate_string(rotated, rots) + "</h1>"
    #e_msg = rotate_string(msg, rots)
    return form.format(rotate_string(rotated, rots))


app.run()