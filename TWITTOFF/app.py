""" Function for __init__, build app factory and do routes/config """

from flask import Flask
from .model import DB
# add the . because it's in the same folder

# app works without this, but..?
# from dotenv import load_dotevn
# load_dotenv

def create_app():
    app = Flask(__name__) # template_folder='mytemplatepath'
    
    # add configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    # link database to app
    DB.init_app(app)

    @app.route("/")
    def root():
        return 'Testing, testing'
        
    return app

# FLASK_APP=TWITTOFF:APP flask run / shell



# file that includes API
# from .twitter import
# from .predict import predict_user

# add route to add new users or get users
    # @app.route("/user", methods= ['POST'])
    # @app.route("/user/<name>", methods=['GET']) # both need param
    # def user(name=None, message=''):
    #     name = name or request.values['user_name']
    #     try:
    #         if request.method == 'POST':
    #             add_or_update_user(name)
    #             message = 'User {} has been successfully added!'.format(name)
    #         tweets = User.query.filter(User.name == name).one().tweets
        
    #     except Exception as e:
    #         message = 'Error adding {}: {}'.format(name, e)
    #         tweets = []

    #     return render_template('user.html', title=name, tweets=tweets, message=message)


    # @app.route('/compare', methods=['POST'])
    # def compare(message=''):
    #     user1, user2 = sorted([request.values['user1'],
    #     request.values['user2']])

    #     if user1 == user2:
    #         message 

    # def root():
    #     return 'Testing, testing'
    # return app


# for prediction.html

# {% extends "base.html" %}
# {% block content %}
# id="prediction">
# <h2> {{title}} </h2>
# <p> {{message }} </p>
