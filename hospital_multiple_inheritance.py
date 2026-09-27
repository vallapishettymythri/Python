#Hospital doctors and adminitrators. have dual roles. Create doctor, administrator. Treat patients90, manage departments()
class doctors:
    def __init__(self,specialization,patients):
        self.specialization=specialization
        self.patients=patients
    def treat_patient(self):
        print(self.specialization)
        print(self.patients)

class admin:
    def __init__(self,department,tasks):
        self.department=department
        self.tasks=tasks
    def manage_department(self):
        print(self.department)
        print(self.tasks)
class docadmin(doctors,admin):
    def __init__(self,specialization,patients,department,tasks):
        doctors.__init__(self,specialization,patients)
        admin.__init__(self,department,tasks)
    def display(self):
        self.treat_patient()
        self.manage_department()
doc=docadmin("neurology","Mayan","Admin","Rounds")