from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update

app = Flask(__name__)
password = input("Your database password: ")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://komlancz:{}@localhost/user-stories'.format(password)
db = SQLAlchemy(app)


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    story_text = db.Column(db.String)
    criteria = db.Column(db.String)
    business_value = db.Column(db.Integer)
    estimation = db.Column(db.Integer)
    status = db.Column(db.String)

    def __init__(self, title, story_text, criteria, business_value, estimation, status):
        self.title = title
        self.story_text = story_text
        self.criteria = criteria
        self.business_value = business_value
        self.estimation = estimation
        self.status = status


@app.route('/')
def index():
    title = 'User Story Manager'
    return render_template('form.html', title=title)


'''Make a new story and append the database with it'''
@app.route('/story', methods=['POST'])
def story():
    new_story = Story(request.form['story_title'], request.form['story'], request.form['criteria'], request.form['business_value'], float(request.form['estimation']), request.form['status'])
    db.session.add(new_story)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/story/<story_id>', methods=['POST'])
def edit_story(story_id):
    myID = Story.query.filter_by(id=story_id).first()
    myID.title = 'ez a proba'
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/and/list')
def list():
    title = 'User Story Manager'
    myStory = Story.query.all()
    return render_template('list.html', title=title, myStory=myStory)

if __name__ == '__main__':
    app.run(debug=True)