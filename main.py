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
        return str(self.name)

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)


members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))


def align_days(member_list):
    days_of_players = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    for member in member_list:
        if member.days == "All":
            for value in days_of_players.values():
                value.append(member)
        else:
            if member.days.count("Monday") != 0:
                days_of_players["Monday"].append(member)
            if member.days.count("Tuesday") != 0:
                days_of_players["Tuesday"].append(member)
            if member.days.count("Wednesday") != 0:
                days_of_players["Wednesday"].append(member)
            if member.days.count("Thursday") != 0:
                days_of_players["Thursday"].append(member)
            if member.days.count("Friday") != 0:
                days_of_players["Friday"].append(member)
            if member.days.count("Saturday") != 0:
                days_of_players["Saturday"].append(member)
            if member.days.count("Sunday") != 0:
                days_of_players["Sunday"].append(member)

        # print(days_of_players)

    return days_of_players


print(align_days(members))
