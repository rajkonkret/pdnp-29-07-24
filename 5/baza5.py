# ORM - dostęp do bazy w sposób obiektowy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True - logi z bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
users = session.query(User).all()
for user in users:
    print(user.name)
# Jan Kowalski
# Jan Kowalski
