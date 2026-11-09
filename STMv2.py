import oracledb 

connection = oracledb.connect(
    user="system",
    password="*****",
    host="localhost",
    port=1522,
    service_name="FREEPDB1"
)

cursor = connection.cursor()

class Team:
    def __init__(self, team_name):
        self.team_name = team_name

    def show_players(self, selected_team_id):
            cursor.execute("SELECT * FROM Players WHERE Team_id = :team_id",
            team_id = selected_team_id
            )
            players = cursor.fetchall()
    
            for player in players:
                    print("Name: ", player[1])
                    print("Position: ", player[2])
                    print("Goals: ", player[3])
                    print("Assists: ", player[4])
                    print("Appearances: ", player[5])
                    print("Yellow cards: ", player[6])
                    print("Red cards: ", player[7])
                    print()

    def add_player(self, selected_team_id):
        player_name = input("Enter player name: ")
        position = input("Enter player position: ")

        cursor.execute(
            "INSERT INTO Players (Player_name, Position, Team_id) "
            "VALUES (:player_name, :position, :team_id)",
            player_name=player_name,
            position=position,
            team_id=selected_team_id
    )

        connection.commit()

        print(f"{player_name} was added successfully.")

    def get_player(self, selected_team_id, team_name):
        player_name = input("Please enter a player name: ").title()

        cursor.execute("SELECT * FROM Players WHERE Team_id = :team_id AND Player_name = :player_name",
        team_id = selected_team_id,
        player_name = player_name
        )    
        player_row = cursor.fetchone()

        if player_row is None:
            print(f"This player was not found on {team_name}")
            return None
        else: 
            return player_row
    
    def update_stats(self, selected_team_id, team_name):
        player_update = self.get_player(selected_team_id, team_name)
        if player_update is None:
            return
        stat_update = input("Which stat do you want to update?: \n 1. Goals\n 2. Assists\n 3. Appearances\n 4. Yellow_cards\n 5. Red_cards\n").lower()
        if stat_update == "1" or stat_update == "goals":
            stat_number = int(input("How much would you like to add?: "))
            cursor.execute("UPDATE Players SET Goals = Goals + :stat_number WHERE Team_id = :team_id AND Player_name = :player_name",
                team_id = selected_team_id,
                player_name = player_update[1],
                stat_number = stat_number
                ) 
        elif stat_update == "2" or stat_update == "assists":
            stat_number = int(input("How much would you like to add?: "))
            cursor.execute("UPDATE Players SET Assists = Assists + :stat_number WHERE Team_id = :team_id AND Player_name = :player_name",
                team_id = selected_team_id,
                player_name = player_update[1],
                stat_number = stat_number
                ) 
        elif stat_update == "3" or stat_update == "appearances":
            stat_number = int(input("How much would you like to add?: "))
            cursor.execute("UPDATE Players SET Appearances = Appearances + :stat_number WHERE Team_id = :team_id AND Player_name = :player_name",
                team_id = selected_team_id,
                player_name = player_update[1],
                stat_number = stat_number
                )
        elif stat_update == "4" or stat_update == "yellow cards":
            stat_number = int(input("How much would you like to add?: "))
            cursor.execute("UPDATE Players SET Yellow_cards = Yellow_cards + :stat_number WHERE Team_id = :team_id AND Player_name = :player_name",
                team_id = selected_team_id,
                player_name = player_update[1],
                stat_number = stat_number
                )
        elif stat_update == "5" or stat_update == "red cards":
            stat_number = int(input("How much would you like to add?: "))
            cursor.execute("UPDATE Players SET Red_cards = Red_cards + :stat_number WHERE Team_id = :team_id AND Player_name = :player_name",
                team_id = selected_team_id,
                player_name = player_update[1],
                stat_number = stat_number
                )
        else:
            print("Invalid stat selection.")
            return

        connection.commit()
        print("Player statistics updated successfully.")

    def remove_player(self, selected_team_id, team_name):
        player = self.get_player(selected_team_id, team_name)
        if player is None:
            return

        cursor.execute("DELETE FROM Players WHERE Player_name = :player_name AND Team_id = :team_id",
        player_name = player[1],
        team_id = selected_team_id
        )
        connection.commit()
        print("Player removed successfully")

    def top_scorer(self, selected_team_id): 
        top_player = "" 
        top_goals = -1 
        cursor.execute( "SELECT Player_name, Goals FROM Players WHERE Team_id = :team_id", 
        team_id=selected_team_id 
        ) 
        players = cursor.fetchall() 
        for player_name, goals in players: 
            if goals > top_goals: 
                top_goals = goals 
                top_player = player_name
             
        print(f"Top Scorer: {top_player} ({top_goals} goals)")


    def top_assister(self, selected_team_id):
        top_player = ""
        top_assists = -1
        cursor.execute( "SELECT Player_name, Assists FROM Players WHERE Team_id = :team_id", 
        team_id=selected_team_id 
        ) 
        players = cursor.fetchall() 
        for player_name, assists in players: 
            if assists > top_assists: 
                top_assists = assists 
                top_player = player_name
                     
        print(f"Top Assister: {top_player} ({top_assists} assists)")

    def team_statistics(self, selected_team_id):
        total_goals = 0
        total_assists = 0
        total_appearances = 0
        total_yellowcards = 0
        total_redcards = 0

        cursor.execute("SELECT Goals, Assists, Appearances, Yellow_cards, Red_cards FROM Players WHERE Team_id = :team_id",
        team_id = selected_team_id
        )

        team_totals = cursor.fetchall()

        for player in team_totals:
            total_goals += (player[0])
            total_assists += (player[1])
            total_appearances += (player[2])
            total_yellowcards += (player[3])
            total_redcards += (player[4])
        print(f"Total goals: {total_goals}\nTotal assists: {total_assists}\nTotal appearances: {total_appearances}\nTotal yellow cards: {total_yellowcards}\nTotal red cards: {total_redcards}")

    def show_teams(self):
        cursor.execute("SELECT Team_name, Manager, Stadium FROM Teams")
        all_teams = cursor.fetchall()

        print("Premier League Teams:")

        for team in all_teams:
            print(team[0])
            print("Manager:", team[1])
            print("Stadium:", team[2])
            print()


print("Welcome to Soccer Team Manager!")

while True:
    team_name = input("Enter your team name: ").title()

    cursor.execute(
        "SELECT Team_id FROM Teams WHERE Team_name = :team_name",
        team_name=team_name
    )

    team_row = cursor.fetchone()

    if team_row is not None:
        break

    print("Error: Please enter a Premier League team.")

selected_team_id = team_row[0]

team = Team(team_name)

while True:
    print(f"""
===== {team_name.upper()} =====

1. Show Players
2. Add Player
3. Update Player Stats
4. Remove Player
5. Top Scorer
6. Top Assister
7. Team Statistics
8. Show Teams
9. Exit
""")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        team.show_players(selected_team_id)

    elif choice == "2":
        team.add_player(selected_team_id)

    elif choice == "3":
        team.update_stats(selected_team_id, team_name)

    elif choice == "4":
        team.remove_player(selected_team_id, team_name)

    elif choice == "5":
        team.top_scorer(selected_team_id)

    elif choice == "6":
        team.top_assister(selected_team_id)

    elif choice == "7":
        team.team_statistics(selected_team_id)

    elif choice == "8":
        team.show_teams()

    elif choice == "9":
        print("Exiting Soccer Team Manager.")
        cursor.close()
        connection.close()
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")

    print()