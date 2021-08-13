from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Myclass(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Myclass(content = task_content)

        try:    
            db.session(new_task)
            db.session.commit()
            return redirect('/')
        except:
            tasks = Myclass.query.order_by(Myclass.date_created).all()
            return 'There was an issue adding your task'
    else:
        return render_template('index.html')
   

if __name__ == "__main__":
    app.run(debug= True)