from src.utils import generate_worked_intervals


class InputData:
    def __init__(self):
        self.lines = []
        self.employee_worked_hours = {}

    def read_data(self,filepath):
        with open(filepath) as f:
            lines = f.readlines()
        for line in lines:
            self.lines.append(line.strip())

    def parse_lines(self):
        for line in self.lines:
            tokenized_line = line.split("=")
            tokenized_worked_hours = list(tokenized_line[1].split(","))
            intervals = generate_worked_intervals(tokenized_worked_hours)
            self.employee_worked_hours[tokenized_line[0]] = intervals
