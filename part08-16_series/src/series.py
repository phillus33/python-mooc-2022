from multiprocessing.sharedctypes import Value


class Series():

    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        if not self.ratings:
            return f"{self.title} ({self.seasons} seasons) \ngenres: {', '.join(self.genres)} \nno ratings"
        return f"{self.title} ({self.seasons} seasons) \ngenres: {', '.join(self.genres)} \n{len(self.ratings)} ratings, average {self.get_rating():.1f} points"

    def rate(self, rating: int):
        if rating < 0:
            raise ValueError()
        self.ratings.append(rating)
    
    def get_rating(self):
        return sum(self.ratings)/len(self.ratings)
        

def minimum_grade(grade: float, series_list: list):
    result = []
    for item in series_list:
        if item.get_rating() >= grade:
            result.append(item)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for item in series_list:
        if genre in item.genres:
            result.append(item)

    return result
    
if __name__ == "__main__":

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)
    
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)