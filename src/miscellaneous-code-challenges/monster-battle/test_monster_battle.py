from monster_battle import Game, Setup, TYPES


def test_fight():
    """Has two groups of monsters fight each other"""
    one = [
        Setup(
            10,
            5,
            "poison",
            "fire",
        ),
        Setup(4, 5, "sleep", "water"),
        Setup(9, 9, "burn", "earth"),
    ]
    two = [
        Setup(5, 6, "paralysis", "water"),
        Setup(10, 10, "freeze", "fire"),
        Setup(5, 5, "sleep", "air"),
    ]
    game = Game(one, two)

    logs = []
    while game.can_fight():
        logs.extend(game.fight())

    logs.extend(game.fight())

    expected = [
        "First monster attacks for 1 damage with burn type. Second monster has 0 health left.",
        "Second monster attacks for 5 damage with sleep type. First monster has 1 health left.",
        "Second monster died.",
        "First monster attacks for 4 damage with sleep type. Second monster has 3 health left.",
        "Second monster missed. First monster has 0 health left.",
        "First monster died.",
        "First monster attacks for 5 damage with poison type. Second monster has 0 health left.",
        "Second monster attacks for 3 damage with paralysis type. First monster has 0 health left.",
        "First monster died.",
        "Second monster died.",
        "No monsters left alive. It's a draw.",
    ]

    assert logs == expected


if __name__ == "__main__":
    test_fight()
