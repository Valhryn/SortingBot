days_of_players = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}


class Player:
    def __init__(self, player_information):
        self.name = player_information[0]
        self.guild = player_information[1]
        self.days = player_information[2].split(", ")
        self.times = [player_information[3], player_information[4]]
        self.roles = player_information[5].split(", ")
        if self.days == ['All']:
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.role = None

    def __repr__(self):
        return str(self.name) + " (" + str(self.role) + ")"

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)

    def between(self, value):
        return self.times[0] <= value <= self.max_time()

    def max_time(self):
        max_time = self.times[1]
        if self.times[1] < self.times[0]:
            max_time += 24
        return max_time

    def __eq__(self, other):
        return self.name == other.name and self.times == other.times and self.days == other.days and self.roles == other.roles and self.guild == other.guild


def set_members(file):
    members = []
    for player in file:
        members.append(Player(player))
    return members


def create_party(day, time, members) -> list[list[Player], int]:
    member_list = [member for member in members if (day in member.days and member.between(time))]
    member_list = sorted(member_list, key=lambda mem: len(mem.roles))

    if len(member_list) == 0:
        return []

    most_roles = len(max(member_list, key=lambda mem: len(mem.roles)).roles)
    party = [None] * 4

    for i in range(most_roles):
        for member in member_list:
            if len(member.roles) <= i:
                member_list.remove(member)
                break
            elif member.roles[i] == "Tank" and party[0] is None and member.roles[i] not in party:
                party[0] = [member, member.roles[i]]
            elif member.roles[i] == "Support" and party[1] is None and member.roles[i] not in party:
                party[1] = [member, member.roles[i]]
            elif member.roles[i] == "DPS" and party[2] is None and member.roles[i] not in party:
                party[2] = [member, member.roles[i]]
            elif member.roles[i] == "DPS" and party[3] is None and member.roles[i] not in party:
                party[3] = [member, member.roles[i]]
    return [party, len([x for x in party if x is not None])]


def align(members):
    best_party, best_length = [0], 0
    for day in days_of_players:
        for time in range(24):
            new_party = create_party(day, time + 1, members)
            if new_party != []:
                new_length = new_party[1]
                new_party = new_party[0]
                if new_length > best_length:
                    best_party = new_party
                    best_length = new_length

    set_party = [member[0] for member in best_party if member is not None]
    roles = [member[1] for member in best_party if member is not None]
    for i in range(len(set_party)):
        set_party[i].role = roles[i]
        members.remove(set_party[i])

    return set_party


def create_parties(members):
    party_list = []
    while len(members) > 0:
        newParty = align(members)
        party_list.append(newParty)

    return party_list


def reverse_party(party):
    days = [set(person.days) for person in party]
    set_of_days = set(days_of_players.keys())
    day_set = None
    for day in days:
        if day_set is not None:
            set_of_days = set_of_days.intersection(day_set)
        day_set = day

    min_hour = -1
    max_hour = 1000
    for person in party:
        player_max = person.max_time()
        if person.times[0] > min_hour:
            min_hour = person.times[0]
        if player_max < max_hour:
            max_hour = person.max_time()
    time_set = [min_hour, max_hour]

    return [day_set, time_set]
# maya was here
# momo's sister hey i sunck on this compyter to play games \
#      ''
def end_file(party_list):
    file = ""

    for i in range(len(party_list)):
        party_details = reverse_party(party_list[i])
        file += "Party " + str(i + 1)
        days = list(party_details[0])
        file += "\nDays: " + str(days).replace("'", "")[1:-1]
        if party_details[1][1] > 24:
            party_details[1][1] += -24
        file += "\nTimes: " + str(party_details[1][0]) + " -> " + str(party_details[1][1])
        file += "\n\t"

        file += "\n\t".join(map(str, party_list[i]))

        file += "\n\n"
    return file
