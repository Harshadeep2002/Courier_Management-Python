class InvalidEmployeeIdException(Exception):
    def __init__(self,employee_id):
        super() .__init__(f'EmployeeID {employee_id} is not found in the system') 
