from flask import Flask
from flaskr import apis

if __name__ == '__main__':
    apis.run(debug=True)