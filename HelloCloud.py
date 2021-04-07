from flask import Flask
server = Flask(_name_)

@server.route("/")
def hello():
  return "Hello 5906021632071 peeranut thadsup from Server"

if _name_ == "_main_":
  server.run(host='0.0.0.0',port=80)
