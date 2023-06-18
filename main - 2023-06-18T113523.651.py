class Cow:
    def __init__(self, tag_number, birth_date):
        self.tag_number = tag_number
        self.birth_date = birth_date
        self.calves = []

    def add_calf(self, calf):
        self.calves.append(calf)

    def get_number_of_calves(self):
        return len(self.calves)


class Calf:
    def __init__(self, tag_number, birth_date, sex):
        self.tag_number = tag_number
        self.birth_date = birth_date
        self.sex = sex


class CalvingSeasonTracker:
    def __init__(self):
        self.cows = []

    def add_cow(self, cow):
        self.cows.append(cow)

    def get_number_of_cows(self):
        return len(self.cows)

    def get_number_of_calves(self):
        total_calves = sum(cow.get_number_of_calves() for cow in self.cows)
        return total_calves


# Create calving season tracker instance
tracker = CalvingSeasonTracker()

# Create cows
cow1 = Cow("C001", "2021-01-01")
cow2 = Cow("C002", "2021-02-15")
cow3 = Cow("C003", "2021-03-20")

# Add cows to the tracker
tracker.add_cow(cow1)
tracker.add_cow(cow2)
tracker.add_cow(cow3)

# Create calves
calf1 = Calf("C001-Calf1", "2022-01-10", "Male")
calf2 = Calf("C001-Calf2", "2022-01-12", "Female")
calf3 = Calf("C002-Calf1", "2022-02-20", "Male")
calf4 = Calf("C003-Calf1", "2022-03-25", "Female")

# Add calves to cows
cow1.add_calf(calf1)
cow1.add_calf(calf2)
cow2.add_calf(calf3)
cow3.add_calf(calf4)

# Get number of cows and calves
num_cows = tracker.get_number_of_cows()
num_calves = tracker.get_number_of_calves()

print("Calving Season Tracker:")
print(f"Number of Cows: {num_cows}")
print(f"Number of Calves: {num_calves}")
