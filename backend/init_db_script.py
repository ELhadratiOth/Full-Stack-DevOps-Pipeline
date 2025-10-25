"""
Database Initialization Script
Creates tables and seeds sample data into PostgreSQL
"""
from app.database import init_db, SessionLocal
from app.models.models import User, Product
from datetime import datetime

def seed_sample_data():
    """Create sample data in database"""
    session = SessionLocal()
    
    try:
        # Check if data already exists
        user_count = session.query(User).count()
        if user_count > 0:
            print("Sample data already exists. Skipping seed.")
            return
        
        # Create sample users
        users = [
            User(
                name="John Doe",
                email="john@example.com",
                active=True,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            User(
                name="Jane Smith",
                email="jane@example.com",
                active=True,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            User(
                name="Bob Johnson",
                email="bob@example.com",
                active=False,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
        ]
        
        # Create sample products
        products = [
            Product(
                name="Laptop",
                description="High-performance laptop for development",
                price=1299.99,
                in_stock=True,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            Product(
                name="Monitor",
                description="4K Ultra HD Monitor",
                price=499.99,
                in_stock=True,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            Product(
                name="Keyboard",
                description="Mechanical RGB Keyboard",
                price=149.99,
                in_stock=False,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            Product(
                name="Mouse",
                description="Wireless Mouse with ergonomic design",
                price=79.99,
                in_stock=True,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
        ]
        
        # Add to session and commit
        session.add_all(users)
        session.add_all(products)
        session.commit()
        
        print("✓ Sample data created successfully!")
        print(f"  - Created {len(users)} users")
        print(f"  - Created {len(products)} products")
        
    except Exception as e:
        print(f"✗ Error seeding data: {e}")
        session.rollback()
    finally:
        session.close()

def main():
    """Initialize database"""
    print("🗄️  Initializing database...")
    
    try:
        # Create tables
        print("Creating tables...")
        init_db()
        print("✓ Tables created successfully!")
        
        # Seed sample data
        print("Seeding sample data...")
        seed_sample_data()
        
        print("\n✓ Database initialization complete!")
        
    except Exception as e:
        print(f"✗ Database initialization failed: {e}")
        raise

if __name__ == "__main__":
    main()
