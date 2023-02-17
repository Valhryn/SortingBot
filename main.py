file = open('tester.txt', 'r')
player_based_information = file.read().split("\n\n")


class Player:
    def __init__(self, informational_paragraph):
        lines = informational_paragraph.split("\n")
        lines = [info.split(": ")[1] for info in lines]

        self.name = lines[0]
        self.content_length = lines[1].split(", ")
        self.days = lines[2].split(", ")
        self.times = lines[3].split(", ")
        self.jobs = lines[4].split(", ")
        self.preferred_job = self.jobs[0]
        self.jobs = self.jobs[1:]
        self.static_job = self.preferred_job

    def __repr__(self):
        return str(self.name) + " playing " + str(self.static_job) + " on " + str(self.days)


members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))

print(members)


def align_days_and_times():
    day_splits = [[]] * 7
    for member in members:
        if member.days == "All":
            for day in day_splits:
                day.append(member)
        else:
            if member.days.count("Monday") != 0:
                day_splits[0].append(member)
            if member.days.count("Tuesday") != 0:
                day_splits[1].append(member)
            if member.days.count("Wednesday") != 0:
                day_splits[2].append(member)
            if member.days.count("Thursday") != 0:
                day_splits[3].append(member)
            if member.days.count("Friday") != 0:
                day_splits[4].append(member)
            if member.days.count("Saturday") != 0:
                day_splits[5].append(member)
            if member.days.count("Sunday") != 0:
                day_splits[6].append(member)

        print(day_splits)

    return day_splits

print(align_days_and_times())