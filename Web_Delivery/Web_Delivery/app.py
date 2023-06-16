from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import os
# from flask_login import current_user, login_user, logout_user, login_required, LoginManager, UserMixin

# base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)


ENV = 'dev'

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:policewomen@localhost/Que'
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
    # os.path.join(base_dir, 'database.db')
    app.config["SECRET_KEY"] = 'policewomen'
    



else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']= ''



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# login_manager = LoginManager(app)

# def create_tables():
   


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating= db.Column(db.Integer)
    comments = db.Column(db.Text(1000))


    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

        # print(customer, dealer, rating, comments)
        if customer== '' or dealer == '':
            return render_template('index.html', message = 'Please enter required fields')
        

        with app.app_context():
            # Access the database or perform database-related operations here
            feedback = Feedback(customer, dealer, rating, comments)
            db.session.add(feedback)
            db.session.commit()

        return render_template('success.html')


        



if __name__ == '__main__':
    app.run()