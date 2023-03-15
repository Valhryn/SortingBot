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
class Player:
    def __init__(self, informational_paragraph):
        lines = informational_paragraph.split("\n")
        lines = [info.split(": ")[1] for info in lines]

        self.name = lines[0]
        self.content_length = lines[1].split(", ")[0]
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

days_of_players = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}

file.close()
file = open("results.txt", "w").close()
file = open("results.txt", "w")
file.write("\n".join(members))
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