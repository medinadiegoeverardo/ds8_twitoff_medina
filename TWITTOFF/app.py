""" Function for __init__, build app factory and create routes/config """

from decouple import config
from flask import Flask, render_template, request
from .model import DB, User
# add the . because it's in the same folder

# app works without this, but..?
# from dotenv import load_dotevn
# load_dotenv

def create_app():
    app = Flask(__name__) # template_folder='mytemplatepath'
    

    # IMPORTANT: Heroku knows your schema because config('DATABASE_URL') has
    # is linked to database and we have imported DB, User from model.py

    # add configuration to create sqlite3 database! (add config to database)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # instead of 'sqlite:///db.sqlite3' (more flexible; global variable)
    # or os.environ["DATABASE_URI"]
    
    # to remove umm, idk what this means
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # link database to app (have database "find out" about app)
    DB.init_app(app)

    @app.route("/")
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    # type /reset to reset database for you
    # from within the Flask app (without having to delete from flask shell)
    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        # delete, create then return template with same base template
        return render_template('base.html', title='Reset', users=[])
    return app

# FLASK_APP=TWITTOFF:APP flask shell to open interpreter
# instead of FLASK_APP=hello.py flask run for app on web



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
