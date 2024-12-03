def check_is_report_ok(report: list[int]) -> bool:
    if len(report) < 1:
        return True
    is_increasing = True if report[0] < report[1] else False
    previous_level = report[0]
    for level in report[1:]:
        if is_increasing:
            diff = level - previous_level
            if level < previous_level or diff < 1 or diff > 3:
                return False
        else:
            diff = previous_level - level
            if level > previous_level or diff < 1 or diff > 3:
                return False
        previous_level = level 
    return True


def check_is_report_ok_part_2(report: list[int]) -> bool:
    if len(report) < 1:
        return True
    is_increasing = True if report[0] < report[1] else False
    previous_level = report[0]
    i = 1
    while i < len(report):
        if is_increasing:
            diff = report[i] - previous_level
            cond = report[i] < previous_level
        else:
            diff = previous_level - report[i]
            cond = report[i] > previous_level
       
        if cond or diff < 1 or diff > 3:
            return False
        previous_level = report[i]
        i += 1
    return True

with open("day2/input.txt", "r") as f:
    data = f.read().splitlines()


outcome = 0
for row in data:
    report = [int(level) for level in row.split(" ")]
    if check_is_report_ok_part_2(report):
        outcome += 1
    else:
        is_any_good = []
        for i in range(len(report)):
            try_report = report[:i] + report[i+1:]
            is_any_good.append(check_is_report_ok_part_2(try_report))
        if any(is_any_good):
            outcome += 1
        

print(outcome)