import sys
from datetime import date
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from server.app import create_app
from server.models import db, User, Guest, Episode, Appearance

def seed_data():
    app = create_app()
    
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables...")
        db.create_all()
        
        print("Seeding data...")
        # Create users
        user1 = User(username='admin')
        user1.set_password('password123')
        db.session.add(user1)

        # Create guests
        guest1 = Guest(name='John Doe', occupation='Actor')
        guest2 = Guest(name='Jane Smith', occupation='Musician')
        db.session.add_all([guest1, guest2])

        # Create episodes
        episode1 = Episode(date=date(2023, 1, 1), number=101)
        episode2 = Episode(date=date(2023, 1, 2), number=102)
        db.session.add_all([episode1, episode2])

        # Create appearances
        appearance1 = Appearance(rating=5, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=4, guest_id=2, episode_id=1)
        appearance3 = Appearance(rating=3, guest_id=1, episode_id=2)
        db.session.add_all([appearance1, appearance2, appearance3])

        db.session.commit()
        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()