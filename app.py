from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@127.0.0.1:3306/movie_db"
app.config['SECRET_KEY'] = 'my_project'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
#axtarış yoluna "/admin" yazaraq AdminPanelə çata bilərsiniz
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
from extension import *
from controllers import *
from models import *



admin.add_view(ModelView(Movie, db.session))
admin.add_view(ModelView(Producer, db.session))

if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=5000,debug=True)