# Create a class:
class Employee:  # class
    # State
    def __init__(self, ename, eid, esys_num, enum , eaddress):
        self.ename = ename
        self.eid = eid
        self.esys_num = esys_num     # Fields
        self.enum = enum
        self.eaddress = eaddress

        # Behaviour:

    def get_emp_det(self):   # Methods
        print("Employee detail are".ljust(40, '.'), ':',self.ename, self.eid, self.esys_num,
              self.eaddress  )


emp = Employee("Karthi", "Mcs-0038", "101", "7904134297", "Bangalore" )
# object
emp.get_emp_det()



