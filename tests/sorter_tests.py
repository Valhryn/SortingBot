import pytest
from generalized_version.sorter import Player, set_members, create_party

sample_players = [("One", 101, "Monday, Tuesday", 4, 7, "Support"),
                  ("Two", 101, "Monday", 5, 8, "DPS, Tank"),
                  ("Three", 101, "All", 3, 6, "Support, DPS"),
                  ("Four", 101, "All", 20, 4, "Tank, DPS")]

player_one = Player(sample_players[0])
player_two = Player(sample_players[1])
player_three = Player(sample_players[2])
player_four = Player(sample_players[3])


def test_create_player():
    assert player_one.name == sample_players[0][0]
    assert player_one.days == ["Monday", "Tuesday"]
    assert player_one.roles == ["Support"]
    assert player_one.role == None
    assert player_one.times == [4, 7]

    assert player_two.name == "Two"
    assert player_two.days == ["Monday"]
    assert player_two.roles == ["DPS", "Tank"]
    assert player_two.role == None
    assert player_two.times == [5, 8]

    assert player_three.name == "Three"
    assert player_three.days == ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assert player_three.roles == ["Support", "DPS"]
    assert player_three.role == None
    assert player_three.times == [3, 6]


def test_player_between():
    for i in range(4):
        assert not player_one.between(i)
    for i in range(8, 25):
        assert not player_one.between(i)
    for i in range(4, 8):
        assert player_one.between(i)

    for i in range(20):
        assert not player_four.between(i)
    for i in range(20, 29):
        assert player_four.between(i)
    for i in range(29, 49):
        assert not player_four.between(i)


def test_get_members():
    assert set_members(sample_players) == [player_one, player_two, player_three, player_four]

    sample_players_two = [("Five", 102, "Tuesday, Wednesday", 13, 17, "DPS"),
                          ("Six", 102, "Wednesday, Thursday", 15, 23, "DPS")]

    player_five = Player(sample_players_two[0])
    player_six = Player(sample_players_two[1])

    assert set_members(sample_players_two) == [player_five, player_six]

def test_create_party():
    player_list = set_members(sample_players)

    assert create_party("Monday", 5, player_list) == [[None, player_one, player_two, player_three], 3]
    assert create_party("Tuesday", 4, player_list) == [[player_four, player_one, None, None], 2]
    assert create_party("Wednesday", 16, player_list) == [[None, None, None, None], 0]