"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Model for Cupcake 


def connect_db(app):
    """ Connect to the Database"""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """ Cupcake Model"""

    __tablename__= "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    flavor = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    size = db.Column(
        db.String(50),
        nullable=False,
        default="Medium"
    )

    rating = db.Column(
        db.Float,
        nullable=False
    )
    image = db.Column(
        db.String(500),
        nullable=False,
        default="https://tinyurl.com/demo-cupcake"
    )

    def serialize(self):
        """Serialize cupcake to dictionary"""

        c = self
        return {
            "id": c.id,
            "flavor": c.flavor,
            "size": c.size,
            "rating": c.rating,
            "image": c.image
        }
    

    def __repr__(self):
        """Show info about cupcake"""

        c = self
        return f"<Cupcake {c.id} {c.flavor} {c.size} {c.rating} {c.image}>"
    

