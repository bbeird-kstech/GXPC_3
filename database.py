from models import Base, EquipmentOwner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:Kstech070@localhost/ExploreDev'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

# Retrieve list of equipment owners
equipment_owners = session.query(EquipmentOwner).all()

for owner in equipment_owners:
    print(f"Owner ID: {owner.clientid}, Client: {owner.client_name}")
