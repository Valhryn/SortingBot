file = open('dark.txt', 'r')
player_based_information = file.read().split("\n\n")

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
class Player:
    def __init__(self, informational_paragraph):
        lines = informational_paragraph.split("\n")
        lines = [info.split(": ")[1] for info in lines]

        self.name = lines[0]
        self.content_length = lines[1].split(", ")
        self.days = lines[2].split(", ")
        self.times = lines[3].split(", ")
        self.jobs = lines[4].split(", ")
        if self.days == ['All']:
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.actual_job = None

    def __repr__(self):
        return str(self.name) + " (" + str(self.actual_job) + ")"

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)


members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))

days_of_players = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}
def align_days(member_list):
    for member in member_list:
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

clear_times = {
    "Casual": [],
    "Midcore": [],
    "Hardcore": [],
    "Hard": []
}
def align_clear_times(member_list):
    for member in member_list:
        if member.days == "All":
            for value in clear_times.values():
                value.append(member)
        else:
            if member.content_length.count("Casual") != 0:
                clear_times["Casual"].append(member)
            if member.content_length.count("Midcore") != 0:
                clear_times["Midcore"].append(member)
            if member.content_length.count("Hardcore") != 0:
                clear_times["Hardcore"].append(member)
            if member.content_length.count("Hard") != 0:
                clear_times["Hard"].append(member)

        # print(clear_times)

    return clear_times

possible_times = {
    "Dead of Night": [],
    "Early Bird Morning": [],
    "Morning": [],
    "Afternoon": [],
    "Early Evening": [],
    "Evening": [],
    "Night": [],
}
def align_times(member_list):
    for member in member_list:
        if member.times == "All":
            for value in possible_times.values():
                value.append(member)
        else:
            if member.times.count("Dead of Night") != 0:
                possible_times["Dead of Night"].append(member)
            if member.times.count("Early Bird Morning") != 0:
                possible_times["Early Bird Morning"].append(member)
            if member.times.count("Morning") != 0:
                possible_times["Morning"].append(member)
            if member.times.count("Afternoon") != 0:
                possible_times["Afternoon"].append(member)
            if member.times.count("Early Evening") != 0:
                possible_times["Early Evening"].append(member)
            if member.times.count("Evening") != 0:
                possible_times["Evening"].append(member)
            if member.times.count("Night") != 0:
                possible_times["Night"].append(member)

        # print(possible_times)

    return possible_times

def create_party(day, time, clear_time, member_list):
    members_that_fit = [member for member in member_list if (member.days.count(day) != 0 and member.times.count(time) != 0 and member.content_length.count(clear_time) != 0)]
    members_that_fit.sort(key=lambda member: len(member.jobs))
    #print(members_that_fit)
    party = [None] * 8
    used_jobs = [None] * 8
    for member in members_that_fit:
        i = 0
        while member not in party and i < len(member.jobs):
            if job_roles[member.jobs[i]] == "Tank" and party[0] == None and member.jobs[i] not in used_jobs:
                party[0] = member
                used_jobs[0] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Tank" and party[1] == None and member.jobs[i] not in used_jobs:
                party[1] = member
                used_jobs[1] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Regen Healer" and party[2] == None:
                party[2] = member
                used_jobs[2] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Shield Healer" and party[3] == None:
                party[3] = member
                used_jobs[3] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Melee" and party[4] == None and member.jobs[i] not in used_jobs:
                party[4] = member
                used_jobs[4] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Selfish" and party[5] == None:
                party[5] = member
                used_jobs[5] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Ranged" and party[6] == None:
                party[6] = member
                used_jobs[6] = (member.jobs[i])
            elif job_roles[member.jobs[i]] == "Caster" and party[7] == None:
                party[7] = member
                used_jobs[7] = (member.jobs[i])
            i += 1

    remaining_members = [member for member in members_that_fit if member not in party]
    if party[5] is None and len(remaining_members) > 0:
        for member_remain in remaining_members:
            for i in range(len(member_remain.jobs)):
                if job_roles[member_remain.jobs[i]] == "Melee" or job_roles[member_remain.jobs[i]] == "Ranged" or job_roles[member_remain.jobs[i]] == "Caster":
                    party[5] = member
                    used_jobs[5] = (member.jobs[i])
                    break
            if party[5] is not None:
                break
    return [party, used_jobs]

def reverse_party(member_list):
    days = list(days_of_players.keys())
    clears = list(clear_times.keys())
    times = list(possible_times.keys())
    #print(days,"\n",clears,"\n",times)
    for member in member_list:
        if member is not None:
            for day in days:
                if day not in member.days:
                    days.pop(days.index(day))
            for clear in clears:
                if clear not in member.content_length:
                    clears.pop(clears.index(clear))
            for time in times:
                if time not in member.times:
                    times.pop(times.index(time))
    return [clears[0], days, times]
def big_align(made_parties, member_list):
    if len(member_list) != 0:
        parties, long_roles, longest_length, longest_party, probably_roles = [], [], 0, [], []
        for time in clear_times:
            for day in days_of_players:
                for day_time in possible_times:
                    created_party = create_party(day, day_time, time, member_list)
                    parties.append(created_party[0])
                    long_roles.append(created_party[1])
        for i in range(len(parties)):
            test_party = [member for member in parties[i] if member is not None]
            if len(test_party) > longest_length:
                longest_party, longest_length, probably_roles = parties[i], len(test_party), long_roles[i]
        for i in range(len(longest_party)):
            if longest_party[i] is not None:
                member_list.remove(longest_party[i])
                longest_party[i].actual_job = probably_roles[i]
        made_parties.append(longest_party)
        big_align(made_parties, member_list)
    return made_parties

file.close()
file = open("results.txt", "w").close()
file = open("results.txt", "w")
parties_created = big_align([], members)
for i in range(len(parties_created)):
    party_str = [str(member) for member in parties_created[i]]
    #print([str(member.actual_job) for member in parties_created[i] if member is not None])
    #print([str(member.preferred_job) for member in parties_created[i] if member is not None])
    reverse_party_list = reverse_party(parties_created[i])
    reverse_party_string = "\nLength: " + str(reverse_party_list[0]) + "\nDays: " + str(reverse_party_list[1]) + "\nTimes: " + str(reverse_party_list[2])
    #print(party_str)
    file.write("\n\nParty " + str(i + 1) + ":" + reverse_party_string + "\n" + ("\n".join(party_str)))
file.close()