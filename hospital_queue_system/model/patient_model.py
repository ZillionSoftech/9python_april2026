class PatientModel:
    FILE_PATH = "data/patients.txt"

    def add_patient(self, token, name, mobile, test):
        with open(self.FILE_PATH, "a") as f:
            f.write(f"{token},{name},{mobile},{test},NotCalled\n")

    def get_all_patients(self):
        patients = []
        try:
            with open(self.FILE_PATH, "r") as f:
                for line in f:
                    patients.append(line.strip().split(","))
        except FileNotFoundError:
            pass
        return patients

    def update_call_status(self, token_to_update):
        updated_data = []
        with open(self.FILE_PATH, "r") as f:
            for line in f:
                token, name, mobile, test, status = line.strip().split(",")

                if int(token) == token_to_update:
                    status = "Called"

                updated_data.append(f"{token},{name},{mobile},{test},{status}\n")

        with open(self.FILE_PATH, "w") as f:
            f.writelines(updated_data)