from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  #return 'Hey its Python Web application!'
  return 'Sugans test python service!'

if __name__ == '__main__':
  app.run()
