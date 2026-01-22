user_input = input().split()

player_count_A = 11
player_count_B = 11
team_a_players = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b_players = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

break_triger = False


for e in user_input:
    if e in team_a_players:
        player_count_A -= 1
        team_a_players.remove(e)
        if player_count_A < 7:
            break_triger = True
            break
    if e in team_b_players:
        player_count_B -= 1
        team_b_players.remove(e)
        if player_count_B < 7:
            break_triger = True
            break

if break_triger:
    print(f"Team A - {player_count_A}; Team B - {player_count_B}")
    print(f"Game was terminated")
else:
    print(f"Team A - {player_count_A}; Team B - {player_count_B}")


