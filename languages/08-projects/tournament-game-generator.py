def main():
    # Step 1: Get number of teams
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams >= 2:
            break
        print("The minimum number of teams is 2, try again.")

    # Step 2: Get team names
    teams = {}
    for i in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{i+1}: ")
            if 1 < len(team_name.split()) <= 2 and len(team_name) > 1:
                teams[team_name] = {'games': 0, 'wins': 0}
                break
            print("Team names must have at least 2 characters and at most 2 words, try again.")

    # Step 3: Get number of games played by each team
    while True:
        games_played = int(input("Enter the number of games played by each team: "))
        if games_played >= num_teams - 1:
            for team in teams:
                teams[team]['games'] = games_played
            break
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    # Step 4: Get number of wins by each team
    for team in teams:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))
            if 0 <= wins <= teams[team]['games']:
                teams[team]['wins'] = wins
                break
            print("Invalid number of wins. A team can't have more wins than the games they played or less than 0 wins, try again.")

    # Step 5: Sort the teams by number of wins
    sorted_teams = sorted(teams.items(), key=lambda x: x[1]['wins'])

    # Step 6: Schedule the games
    print("Generating the games to be played in the first round of the tournament...")
    for i in range(num_teams // 2):
        print(f"Home: {sorted_teams[i][0]} VS Away: {sorted_teams[-(i+1)][0]}")

if __name__ == "__main__":
    main()
