from app import app
from models import db, Pet

db.drop_all()
db.create_all()

p1 = Pet(
    name="Hugo",
    species="English Cocker Spaniel",
    photo_url="https://images.squarespace-cdn.com/content/v1/568988da0e4c11c934a13f25/1577993141495-ADYWYU6OQO9L94PXAN99/8f49a415-9aec-4de0-a885-3977e951100e.JPG",
    age=3,
    notes="Loves long walks by the beach and dog parks for small dogs.",
)

p2 = Pet(
    name="Cherry",
    species="Brown Lab",
    age=9,
    notes="Needs diaper changed every other day. Good with children. House trained."
)

p3 = Pet(
    name="Dash",
    species="Boxer-German Shepherd Mix",
    photo_url="https://www.alphapaw.com/wp-content/uploads/2021/01/50068000_357531191643365_1129142352511023180_n-917x1024-1.jpg",
    age=1,
    notes="Loves long walks by the beach and dog parks for small dogs.",
    available=False
)


db.session.add_all([p1, p2, p3])
db.session.commit()