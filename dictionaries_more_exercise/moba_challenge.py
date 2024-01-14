players = {}

while True:
    line = input()
    if line == "Season end":
        break

    if "->" in line:
        player, position, skill = line.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position not in players[player] or skill > players[player][position]:
            players[player][position] = skill
    elif "vs" in line:
        player1, player2 = line.split(" vs ")

        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()) & set(players[player2].keys())

            if common_positions:
                total_skill1 = sum(players[player1][pos] for pos in common_positions)
                total_skill2 = sum(players[player2][pos] for pos in common_positions)

                if total_skill1 > total_skill2:
                    del players[player2]
                elif total_skill1 < total_skill2:
                    del players[player1]

# Sort and print players and their positions.
sorted_players = sorted(players.keys(), key=lambda x: (-sum(players[x].values()), x))
for player in sorted_players:
    total_skill = sum(players[player].values())
    print(f"{player}: {total_skill} skill")
    for position, skill in sorted(players[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
