from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.equipment_owner import EquipmentOwner
# from models.unit import Unit
# from models.calibration_tolerance import CalibrationTolerance
# from models.process_tolerance import ProcessTolerance
# from models.frequency import Frequency
# from models.criticality import Criticality
# from models.client import Client

DATABASE_URL = 'postgresql://postgres:Kstech070@localhost/GXPC_Dev'


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_client_names(self):
        session = self.get_session()
        clients = session.query(EquipmentOwner.client_name).all()
        session.close()
        return [client.client_name for client in clients]