file = open('player.txt', 'r')
player_based_information = file.read().split("\n\n")

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
    def __init__(self, informational_paragraph):
        lines = informational_paragraph.split("\n")
        lines = [info.split(": ")[1] for info in lines]

        self.name = lines[0]
        self.days = lines[1].split(", ")
        self.times = [int(lines[2].split(", ")[0]), int(lines[3].split(", ")[0])]
        print(self.times)
        self.roles = lines[4].split(", ")
        if self.days == ['All']:
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.role = None

    def __repr__(self):
        return str(self.name) + " (" + str(self.role) + ")"

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)

    def between(self, value):
        return self.times[0] <= value <= self.times[1]


members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))

def create_party(day, time):
    member_list = [member for member in members if (day in member.days and member.between(time))]
    member_list = sorted(member_list, key = lambda mem: len(mem.roles))
    print(member_list)
    #print(member_list)

    if len(member_list) == 0:
        return []

    most_roles = len(max(member_list, key = lambda mem: len(mem.roles)).roles)
    party = [None] * 4
    length = 0
    #print(party)

    for i in range(most_roles):
        for member in member_list:
            #print(member)
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
    #print(party)
    return [party, len([x for x in party if x is not None])]

def align():
    best_party, best_length = [0], 0
    for day in days_of_players:
        for time in range(24):
            new_party = create_party(day, time + 1)
            if new_party != []:
                new_length = new_party[1]
                new_party = new_party[0]
                if new_length > best_length:
                    best_party = new_party
                    best_length = new_length

    set_party = [member[0] for member in best_party if member is not None]
    roles = [member[1] for member in best_party if member is not None]
    # for i in range(4):
    #     if set_party[i] is not None:
    #         #print(set_party[i])
    #         #print(isinstance(set_party[i], Player))
    #         set_party[i].role = best_party[i]
    #         members.remove(set_party[i])
    for i in range(len(set_party)):
        set_party[i].role = roles[i]
        members.remove(set_party[i])

    return set_party

party_list = []
while len(members) > 0:
    party_list.append(align())

def reverse_party(party):
    days = [set(person.days) for person in party]
    set_of_days = set(days_of_players.keys())
    day_set = None
    for day in days:
        if day_set is not None:
            set_of_days = set_of_days.intersection(day_set)
        day_set = day

    times = [set(person.times) for person in party]
    set_of_times = set(possible_times.keys())
    time_set = None
    for day in days:
        if time_set is not None:
            set_of_times = set_of_times.intersection(time_set)
        time_set = day

    return [day_set, time_set]

file.close()
file = open("results.txt", "w").close()
file = open("results.txt", "w")

for party in party_list:
    party_details = reverse_party(party)

    file.write("Days: " + str(party_details[0]))
    file.write("\nTimes: " + str(party_details[1]))
    file.write("\n\t")

    file.write("\n\t".join(map(str, party)))

    file.write("\n\n")
file.close()