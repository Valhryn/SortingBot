file = open('dark.txt', 'r')
player_based_information = file.read().split("\n\n")


# Issues: Violent not in Casual Party with open slot, Xander not in Midcore party with open slot (based off length)? Eyre treated as selfish, Aminara for midcore as well
job_roles = {
    "WHM": "Regen Healer",
    "SCH": "Shield Healer",
    "AST": "Regen Healer",
    "SGE": "Shield Healer",
    "PLD": "Tank",
    "WAR": "Tank",
    "DRK": "Tank",
    "GNB": "Tank",
    "MNK": "Melee",
    "DRG": "Melee",
    "NIN": "Melee",
    "SAM": "Selfish",
    "RPR": "Melee",
    "BRD": "Ranged",
    "MCH": "Selfish",
    "DNC": "Ranged",
    "BLM": "Selfish",
    "SMN": "Caster",
    "RDM": "Caster"
}

days_of_players = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}

possible_times = {
    "Dead of Night": [],
    "Early Bird Morning": [],
    "Morning": [],
    "Afternoon": [],
    "Early Evening": [],
    "Evening": [],
    "Night": [],
}

clear_times = {
    "Casual": [],
    "Midcore": [],
    "Hardcore": [],
    "Hard": []
}
class Player:
    def __init__(self, informational_paragraph):
        lines = informational_paragraph.split("\n")
        lines = [info.split(": ")[1] for info in lines]

        self.name = lines[0]
        self.difficulty = lines[1].split(", ")[0]
        self.days = lines[2].split(", ")
        self.times = lines[3].split(", ")
        self.jobs = lines[4].split(", ")
        if self.days == ['All']:
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.job = None

    def __repr__(self):
        return str(self.name) + " (" + str(self.job) + ")"

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)

members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))

def create_party(day, time, difficulty):
    member_list = [member for member in members if (member.days.count(day) != 0 or member.times.count(time) != 0 or member.difficulty.count(difficulty) != 0)]
    member_list = sorted(member_list, key = lambda mem: len(mem.jobs))
    #print(member_list)

    most_jobs = len(max(member_list, key = lambda mem: len(mem.jobs)).jobs)
    party = [None] * 8
    length = 0
    #print(party)

    for i in range(most_jobs):
        for member in member_list:
            #print(member)
            if len(member.jobs) <= i:
                member_list.remove(member)
                break
            elif job_roles[member.jobs[i]] == "Tank" and party[0] == None and member.jobs[i] not in party:
                #print(member)
                party[0] = [member, member.jobs[i]]
                #print(party[0][0])
            elif job_roles[member.jobs[i]] == "Tank" and party[1] == None and member.jobs[i] not in party:
                party[1] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Regen Healer" and party[2] == None:
                party[2] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Shield Healer" and party[3] == None:
                party[3] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Melee" and party[4] == None and member.jobs[i] not in party:
                party[4] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Selfish" and party[5] == None:
                party[5] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Ranged" and party[6] == None:
                party[6] = [member, member.jobs[i]]
            elif job_roles[member.jobs[i]] == "Caster" and party[7] == None:
                party[7] = [member, member.jobs[i]]
    print(party)
    return [party, len([x for x in party if x is not None])]

def align():
    best_party, best_length = [0], 0
    for day in days_of_players:
        for time in possible_times:
            for difficulty in clear_times:
                new_party = create_party(day, time, difficulty)
                new_length = new_party[1]
                new_party = new_party[0]
                if new_length > best_length:
                    best_party = new_party
                    best_length = new_length

    set_party = best_party[0]
    for i in range(8):
        if set_party[i] is not None:
            #print(set_party[i])
            #print(isinstance(set_party[i], Player))
            set_party[i].job = best_party[i]
            members.remove(set_party[i])

    return set_party

party_list = []
while len(members) > 0:
    party_list.append(align())


create_party("Monday", "Evening", "Hard")
file.close()
file = open("results.txt", "w").close()
file = open("results.txt", "w")
file.write("\n".join(map(str, party_list)))
# parties_created = big_align([], members)
# for i in range(len(parties_created)):
#     party_str = [str(member) for member in parties_created[i]]
#     #print([str(member.actual_job) for member in parties_created[i] if member is not None])
#     #print([str(member.preferred_job) for member in parties_created[i] if member is not None])
#     reverse_party_list = reverse_party(parties_created[i])
#     reverse_party_string = "\nLength: " + str(reverse_party_list[0]) + "\nDays: " + str(reverse_party_list[1]) + "\nTimes: " + str(reverse_party_list[2])
#     #print(party_str)
#     file.write("\n\nParty " + str(i + 1) + ":" + reverse_party_string + "\n" + ("\n".join(party_str)))
file.close()