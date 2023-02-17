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


new_player = Player(player_based_information[0])
