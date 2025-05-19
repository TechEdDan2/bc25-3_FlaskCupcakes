from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

db.session.add_all([c1, c2])
db.session.commit()

# Use this photo for testing? 
# Photo by <a href="https://unsplash.com/@matosalbers?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Cristina Matos-Albers</a> on <a href="https://unsplash.com/photos/cupcake-top-with-cream-in-yellow-cupcake-holder-Ltv7a5m8i4c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      