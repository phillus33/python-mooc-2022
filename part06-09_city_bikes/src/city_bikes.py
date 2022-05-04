import math

def get_station_data(filename: str): 
    stations = {}
    with open(filename) as new_file:

        for line in new_file:
            line = line.strip()
            parts = line.split(";")

            if parts[0] == "Longitude":
                continue

            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):

    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2

    return math.sqrt(x_km**2 + y_km**2)

# def list_of_stations(stations: dict):
#     result = []
#     for station in stations:
#         result.append(station)
#     return result

# def greatest_distance(stations: dict):
#     station_list = list_of_stations(stations)

#     greatest = ("","",0)

#     for i in range(len(station_list)-1):
#         for j in range(i+1, len(station_list)-1):
#             dist = distance(stations, station_list[i], station_list[j])
#             # print(f"dist: {dist}, station1: {station_list[index]}, station2: {station_list[index+1]}")
#             if dist > greatest[2]:
#                 greatest = station_list[i], station_list[j], dist
    
#     return greatest

def greatest_distance(stations: dict):
    longest = 0

    for start in stations:
        for end in stations:
            result = distance(stations, start, end)
            if result > longest:
                station1 = start
                station2 = end
                longest = result
    return station1, station2, longest




# stations = get_station_data("stations1.csv")
# res = greatest_distance(stations)
# print(res)


# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)