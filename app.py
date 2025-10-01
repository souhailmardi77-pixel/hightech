<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, hightech!!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
for i in range(1,10):
	print ("bonjour tout le monde")
>>>>>>> d1894c5e221f39c30dd1d778ac1c1ec10c0b8777
