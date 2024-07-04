from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.equipment_owner import EquipmentOwner
from models.unit import Unit
from models.calibration_tolerance import CalibrationTolerance
from models.process_tolerance import ProcessTolerance
from models.frequency import Frequency
from models.criticality import Criticality
from models.client import Client

DATABASE_URL = 'postgresql://postgres:Kstech070@localhost/ExploreDev'


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_equipment_owners(self):
        session = self.get_session()
        equipment_owners = session.query(EquipmentOwner).all()
        session.close()
        return equipment_owners