class WeatherStation:

    def __init__(self, name: str):
        if name != "":
            self.__name = name
        else: 
            raise ValueError("name can't be empty!")
        self.__observations = []
        self.__count = 0

    def add_observation(self, observation: str):
        self.__count += 1
        self.__observations.append(observation)
            

    def latest_observation(self):
        if len(self.__observations) == 0:
            return ""
        else:
            return self.__observations[-1]
    
    def number_of_observations(self):
        return self.__count

    def __str__(self):
        return f"{self.__name}, {self.__count} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)