from app import db, app

# Create an application context
with app.app_context():
    db.create_all()

print("Database tables created successfully!")
