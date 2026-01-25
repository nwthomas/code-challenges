from monster_battle import Game, Setup


def test_fight():
    """Has two groups of monsters fight each other"""
    one = [Setup(10, 5), Setup(4, 5), Setup(9, 9)]
    two = [Setup(5, 6), Setup(10, 10), Setup(5, 5)]
    game = Game(one, two)

    logs = []
    while game.can_fight():
        logs.extend(game.fight())

    logs.extend(game.fight())

    expected = [
        "First monster attacks for 5 damage. Second monster has 0 health left.",
        "Second monster attacks for 5 damage. First monster has 4 health left.",
        "The second monster died.",
        "First monster attacks for 4 damage. Second monster has 6 health left.",
        "Second monster attacks for 5 damage. First monster has 0 health left.",
        "The first monster died.",
        "First monster attacks for 6 damage. Second monster has 0 health left.",
        "Second monster attacks for 5 damage. First monster has 0 health left.",
        "The first monster died.",
        "The second monster died.",
        "No monsters left alive. It's a draw.",
    ]

    assert logs == expected
