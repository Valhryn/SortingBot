file = open('dark.txt', 'r')
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
        if self.days == ['All']:
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __repr__(self):
        return str(self.name)

    def player_tester(self):
        return str(self.name) + " on days " + str(self.days)

job_roles = {
    "WHM": "Healer",
    "SCH": "Healer",
    "AST": "Healer",
    "SGE": "Healer",
    "PLD": "Tank",
    "WAR": "Tank",
    "DRK": "Tank",
    "GNB": "Tank",
    "MNK": "Melee",
    "DRG": "Melee",
    "NIN": "Melee",
    "SAM": "Melee",
    "RPR": "Melee",
    "BRD": "Ranged",
    "MCH": "Ranged",
    "DNC": "Ranged",
    "BLM": "Caster",
    "SMN": "Caster",
    "RDM": "Caster"
}
members = []
for paragraphs in player_based_information:
    members.append(Player(paragraphs))
print(members)

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
    "Hard": [],
    "Hardcore": [],
    "Midcore": [],
    "Casual": [],
}
def align_clear_times(member_list):
    for member in member_list:
        if member.days == "All":
            for value in clear_times.values():
                value.append(member)
        else:
            if member.content_length.count("Hard") != 0:
                clear_times["Hard"].append(member)
            if member.content_length.count("Hardcore") != 0:
                clear_times["Hardcore"].append(member)
            if member.content_length.count("Midcore") != 0:
                clear_times["Midcore"].append(member)
            if member.content_length.count("Casual") != 0:
                clear_times["Casual"].append(member)

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
    party = [None] * 8
    for member in members_that_fit:
        #print("Checking",member)
        if job_roles[member.preferred_job] == "Tank" and party[0] == None:
            party[0] = member
        elif job_roles[member.preferred_job] == "Tank" and party[1] == None:
            party[1] = member
        elif job_roles[member.preferred_job] == "Healer" and party[2] == None:
            party[2] = member
        elif job_roles[member.preferred_job] == "Healer" and party[3] == None:
            party[3] = member
        elif job_roles[member.preferred_job] == "Melee" and party[4] == None:
            party[4] = member
        elif job_roles[member.preferred_job] == "Melee" and party[5] == None:
            party[5] = member
        elif job_roles[member.preferred_job] == "Ranged" and party[6] == None:
            party[6] = member
        elif job_roles[member.preferred_job] == "Caster" and party[7] == None:
            party[7] = member
        else:
            i = 0
            while member not in party and i < len(member.jobs):
                if job_roles[member.jobs[i]] == "Tank" and party[0] == None:
                    party[0] = member
                elif job_roles[member.jobs[i]] == "Tank" and party[1] == None:
                    party[1] = member
                elif job_roles[member.jobs[i]] == "Healer" and party[2] == None:
                    party[2] = member
                elif job_roles[member.jobs[i]] == "Healer" and party[3] == None:
                    party[3] = member
                elif job_roles[member.jobs[i]] == "Melee" and party[4] == None:
                    party[4] = member
                elif job_roles[member.jobs[i]] == "Melee" and party[5] == None:
                    party[5] = member
                elif job_roles[member.jobs[i]] == "Ranged" and party[6] == None:
                    party[6] = member
                elif job_roles[member.jobs[i]] == "Caster" and party[7] == None:
                    party[7] = member
                i += 1

    return party

def big_align(made_parties, member_list):
    if len(member_list) != 0:
        parties, longest_length, longest_party = [], 0, []
        for time in clear_times:
            for day in days_of_players:
                for day_time in possible_times:
                    parties.append(create_party(day, day_time, time, member_list))
        for party in parties:
            test_party = [member for member in party if member is not None]
            if len(test_party) > longest_length:
                longest_party, longest_length = party, len(test_party)
        for member in longest_party:
            member_list.remove(member)
        made_parties.append(longest_party)
        big_align(made_parties, member_list)
    return made_parties

print(create_party("Friday", "Afternoon", "Hard", members))