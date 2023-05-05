

# a class for patient
class Patient:
    

    def __init__(self,id, first_name, last_name, nic, date_of_birth, blood_group, mobile_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nic = nic
        self.date_of_birth = date_of_birth
        self.blood_group = blood_group
        self.mobile_number = mobile_number

        self.month_data = {}
        self.predicted_result = {}

    def add_month_data(self, month, systolicBP, diastolicBP, blood_sugar, body_temp, heart_rate):
        self.month_data[month] = {
            "systolicBP": systolicBP,
            "diastolicBP": diastolicBP,
            "blood_sugar": blood_sugar,
            "body_temp": body_temp,
            "heart_rate": heart_rate
        }

    def predicted_result(self, predicted_result, month):

        self.predicted_result[month] = predicted_result


    # function to convert data to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "nic": self.nic,
            "date_of_birth": self.date_of_birth,
            "blood_group": self.blood_group,
            "mobile_number": self.mobile_number,
           }

    