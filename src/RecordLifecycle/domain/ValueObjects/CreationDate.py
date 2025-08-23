from datetime import datetime

class CreationDate:
    def __init__(self, date):
        try:
            datetime.strptime(date, "%d/%m/%Y")
            self._date = date
            
        except ValueError:
            raise ValueError("Date's format is incorrect (dd/mm/yyyy)")

    
    def __repr__(self):
        return str(self._date)
    
    def __eq__(self, value):
        return isinstance(value, CreationDate) and self._date == value._date
    
    def __str__(self):
        return str(self._date)