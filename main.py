from app import app, db

def create_table():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
