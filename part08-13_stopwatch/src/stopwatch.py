# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0
            
        

    def __str__(self):
        # if self.seconds < 10:
        #     secs = "0" + str(self.seconds)
        # else:
        #     secs = str(self.seconds)
        
        # if self.minutes < 10:
        #     mins = "0" + str(self.minutes)
        # else:
        #     mins = self.minutes
        
        return f"{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(62):
        print(watch)
        watch.tick()