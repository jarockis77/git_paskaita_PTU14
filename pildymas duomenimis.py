from model import User, Product, sessionmaker, engine

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    session.delete(user)
    session.commit()