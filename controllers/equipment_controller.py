from models.unit import Unit
from models.calibration_tolerance import CalibrationTolerance
from models.process_tolerance import ProcessTolerance
from models.frequency import Frequency
from models.criticality import Criticality
from models.client import Client


class EquipmentController:
    def __init__(self, database, view):
        self.database = database
        self.view = view
        self.view.set_controller(self)

    def populate_dropdowns(self):
        dropdown_models = {
            "Units": Unit,
            "Cal Tol.": CalibrationTolerance,
            "Proc Tol": ProcessTolerance,
            "Frequency": Frequency,
            "Criticality": Criticality,
            "Client": Client
        }

        for label, model in dropdown_models.items():
            options = self.get_dropdown_options(model)
            self.view.update_dropdown_options(label, options)

    def get_dropdown_options(self, model):
        session = self.database.get_session()
        results = session.query(model).all()
        session.close()
        return [getattr(row, row.__table__.columns.keys()[1]) for row in results]

    def get_equipment_owners(self):
        return self.database.get_equipment_owners()