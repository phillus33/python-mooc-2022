import json

class HockeyStats:
    def __init__(self, players: list):
        self.players = players

    def search_player(self):
        name = input("name: ")
        for player in self.players:
            if player['name'] == name:
                self.nice_print(player)

    def list_teams(self):
        teams = []
        for player in self.players:
            if player['team'] not in teams:
                teams.append(player['team'])
        for team in sorted(teams):
            print(team)


    def list_countries(self):
        countries = []
        for player in self.players:
            if player['nationality'] not in countries:
                countries.append(player['nationality'])
        for country in sorted(countries):
            print(country)

    def players_team(self):
        team = input("team: ")
        filtered = [player for player in self.players if player['team'] == team]
        for p in sorted(filtered, key=self.player_score, reverse=True):
            self.nice_print(p)

    def players_nationality(self):
        nationality = input("country: ")
        filtered = [player for player in self.players if player['nationality'] == nationality]
        for p in sorted(filtered, key=self.player_score, reverse=True):
            self.nice_print(p)

    def most_points(self):
        num = int(input("how many: "))
        for p in sorted(self.players, key=self.player_score, reverse=True)[:num]:
            self.nice_print(p)

    def most_goals(self):
        num = int(input("how many: "))
        for p in sorted(self.players, key=lambda x: (x['goals'], -x['games']), reverse=True)[:num]:
            self.nice_print(p)

    # helper function
    def nice_print(self, player: dict):
        print(f"{player['name']:21}{player['team']:3} {player['goals']:3} + {player['assists']:2} = {self.player_score(player):3}")

    # helper function
    def player_score(self, player:dict):
        return player['assists']+ player['goals']

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename) as my_file:
            data = my_file.read()
        return json.loads(data)

class HockeyStatsApp:
    def __init__(self):
        filename = input("file name: ")
        # filename = "partial.json"
        self.filehandler = FileHandler(filename).load_file()
        self.hockeystats = HockeyStats(self.filehandler)
        print(f"read the data of {len(self.filehandler)} players")

    def help(self):
        print("")
        print("""commands: 
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
            """)

    def execute(self):
        self.help()
        
        while True:
            command = input("command: ")

            if command == "0":
                break

            elif command == "1":
                self.hockeystats.search_player()
            
            elif command == "2":
                self.hockeystats.list_teams()

            elif command == "3":
                self.hockeystats.list_countries()

            elif command == "4":
                self.hockeystats.players_team()

            elif command == "5":
                self.hockeystats.players_nationality()

            elif command == "6":
                self.hockeystats.most_points()

            elif command == "7":
                self.hockeystats.most_goals()



HockeyStatsApp().execute()
    
