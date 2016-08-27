from flask import Flask, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)


def connect_db():
    try:
        conn = psycopg2.connect("dbname='user-stories' user='komlancz' host='localhost' password='bator992'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute("""DROP TABLE story;""")
    print("deleted...")
    cur.execute("""CREATE TABLE story (id serial PRIMARY KEY, key integer, data varchar);""")
    conn.commit()
    print("Created...")


@app.route('/')
def index():
    title = 'User Story Manager'
    return render_template('form.html', title=title)


@app.route('/story')
def add_new_story():
    connect_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')