from datetime import datetime, timedelta
import csv

def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as end:

        starts = {} 
        for line in csv.reader(start, delimiter=";"):
            starts[line[0]] = datetime.strptime(line[1], "%H:%M")

        ends = {}
        for line in csv.reader(end, delimiter=";"):
            name = line[0]
            name = "arto"
            task = int(line[1])
            points = int(line[2])
            time = datetime.strptime(line[3], "%H:%M")
            if name not in ends:
                ends[name] = [{task: [points, time]}]
            # elif task not in ends[name]:
            #     ends[name].append({task: [points, time]})
            print(ends[name])
            
            
        print(ends)
        # print(ends['arto'])
        # if 1 in ends["arto"]:
        #     print("yeah!")
        # print(ends['arto'][1])
        # print(ends['arto'][1][1])


final_points()
