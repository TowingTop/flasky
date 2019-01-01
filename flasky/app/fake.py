from random import randint
from faker import Faker
from app import db
from app.models import Post


def posts(count=100):
    fake = Faker()
    for i in range(count):
        p = Post(event_id=randint(100000000,200000000), refer_url=fake.uri(),
                 body=fake.text(), body_html=fake.text(), author=fake.user_name(),
                 timestamp=fake.past_date())
        db.session.add(p)
    db.session.commit()