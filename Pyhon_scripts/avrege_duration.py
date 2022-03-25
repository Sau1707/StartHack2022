import datetime

with open("data.csv","r") as file:
    data = file.readlines()

durations = []
for el in data[1:]:
    id, start, end, type = el.strip().split(";")
    ds_y, ds_m = start.split("-")
    d_start = datetime.datetime(int(ds_y), int(ds_m), 1)
    if end:
        de_y, de_m = end.split("-")
    else:
        de_y, de_m = 2022, 3
    d_end = datetime.datetime(int(de_y), int(de_m), 1)
    durations.append(d_end - d_start)

print(sum(durations, datetime.timedelta()) / len(durations))