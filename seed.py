from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    # ====== Heroes ======
    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    db.session.add_all([h1, h2, h3])

    # ====== Powers ======
    p1 = Power(name="Super Strength", description="Gives the wielder super-human strength")
    p2 = Power(name="Flight", description="Allows the wielder to fly at supersonic speed")
    p3 = Power(name="Elasticity", description="Can stretch the human body to extreme lengths")
    db.session.add_all([p1, p2, p3])

    db.session.commit()

    # ====== Hero Powers ======
    hp1 = HeroPower(hero_id=h1.id, power_id=p2.id, strength="Strong")
    hp2 = HeroPower(hero_id=h3.id, power_id=p1.id, strength="Average")
    db.session.add_all([hp1, hp2])

    db.session.commit()
    print("Seed data added!")
