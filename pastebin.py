from datetime import datetime
from flask import Flask, request, url_for, redirect, g, session, flash, \
     abort, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
db = SQLAlchemy(app)

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text)
    display_name = db.Column(db.String(120))
    languaje = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('paste.id'))
    parent = db.relationship('Paste', lazy=True, backref='children',
                             uselist=False, remote_side=[id])

    def __init__(self, user, display_name, languaje, code, parent=None):
        self.user = user
        self.display_name = display_name
        self.code = code
        self.languaje = languaje
        self.pub_date = datetime.utcnow()
        self.parent = parent

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(120))
    pastes = db.relationship(Paste, lazy='dynamic', backref='user')
"""
@app.before_request
def check_user_status():
    g.user = None
    if 'user_id' in session:
        g.user = request.form['display_name']

@app.route('/', methods=['GET', 'POST'])
def new_paste():
    parent = None
    data = db.engine.execute("SELECT name FROM languages order by name asc")
    langs = data.fetchall()
    reply_to = request.args.get('reply_to', type=int)
    if reply_to is not None:
        parent = Paste.query.get(reply_to)
    if request.method == 'POST' and request.form['code']:
        paste = Paste(g.user, request.form['display_name'], request.form['languaje'], request.form['code'], parent=parent)
        db.session.add(paste)
        db.session.commit()
        if parent is not None:
            send_new_paste_notifications(parent, paste)
        return redirect(url_for('show_paste', paste_id=paste.id))
    return render_template('new_paste.html', parent=parent, langs=langs)


@app.route('/<int:paste_id>')
def show_paste(paste_id):
    paste = Paste.query.options(db.eagerload('children')).get_or_404(paste_id)
    return render_template('show_paste.html', paste=paste)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/help')
def show_help():
    return render_template('help.html')
