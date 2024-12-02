import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

reports = []

for line in f:
    reports.append([int(x) for x in line.split()])

safe_reports = 0


def get_direction(one, two):
    if one > two:
        return 1
    if two > one:
        return -1
    return 0


for report in reports:
   
    this_report_safe = 0

    for idx_to_remove in range(len(report)):
        this_subreport = list(report)
        del this_subreport[idx_to_remove]
        this_subreport_safe = 1
        direction = 0

        for idx, level in enumerate(this_subreport):
            if idx == 0:
                continue

            if direction == 0:
                direction = get_direction(this_subreport[idx], this_subreport[idx - 1])

            if not 0 < abs(this_subreport[idx] - this_subreport[idx - 1]) < 4:
                this_subreport_safe = 0
                break
            if this_subreport[idx] - this_subreport[idx - 1] > 0 and direction != 1:
                this_subreport_safe = 0
                break
            if this_subreport[idx] - this_subreport[idx - 1] < 0 and direction != -1:
                this_subreport_safe = 0
                break
            
        if this_subreport_safe == 1: 
            this_report_safe = 1
            break

    safe_reports += this_report_safe

print(f"The total number of safe reports is: ", safe_reports)
