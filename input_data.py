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
            intervals = []
            tokenized_line = line.split("=")
            tokenized_worked_hours = list(tokenized_line[1].split(","))

            for tokenized_worked_hour in tokenized_worked_hours:
                day = tokenized_worked_hour[0:2]
                start_time = int(tokenized_worked_hour[2:4])
                end_time = int(tokenized_worked_hour[8:10])
                for i in range(start_time,end_time):
                    interval = f"{day}{i}:00-{i+1}:00"
                    intervals.append(interval)
            self.employee_worked_hours[tokenized_line[0]] = intervals
