# coding:utf-8
from flask import Flask
from flask.ext.mongoengine import MongoEngine 

app = Flask(__name__)
app.config['MONGODB_SETTING'] = {'DB': 'my_blog'}
app.config['SECRET_KEY'] = 'KeepThisS3cr3t'
db = MongoEngine(app)

if __name__ == '__main__':
	app.run()