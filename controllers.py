from app import app
from flask import render_template
from models import Movie
@app.route('/movies/')
def movies():
    active_movies = Movie.query.filter_by(status=True).all()
    return render_template('movies.html', movies=active_movies)



if __name__ == '__main__':
    app.run(debug=True)