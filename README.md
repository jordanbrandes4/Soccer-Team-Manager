# Soccer Team Manager

A Python and Oracle SQL application that manages Premier League teams, players, and statistics through a relational database.

The application allows users to retrieve player information, manage team rosters, update individual player statistics, and analyze player and team performance using Python and SQL.

## Features

### Team Management
- Stores Premier League teams and their information
- Retrieves team rosters from the Oracle database
- Displays players associated with individual teams
- Organizes player information by team

### Player Management
- Retrieves player information from the database
- Adds new players to teams
- Removes players from teams
- Updates individual player statistics
- Maintains player records using SQL queries

### Player Statistics
- Displays individual player statistics
- Tracks goals and assists
- Identifies top goal scorers
- Identifies top assist providers

### Team Statistics
- Calculates team totals based on player statistics
- Retrieves team-level performance information
- Uses SQL queries to summarize player contributions

### Database Operations
- Uses Python to interact with an Oracle SQL database
- Retrieves information using SQL SELECT queries
- Adds new records using INSERT statements
- Updates existing records using UPDATE statements
- Removes records using DELETE statements
- Uses SQL queries to calculate and retrieve statistics

## Technologies

- Python
- Oracle SQL
- Oracle Database
- Python-oracledb

## Database

The application uses a relational Oracle database containing two main tables:

- **TEAMS** — Stores Premier League team information
- **PLAYERS** — Stores player information, team associations, and individual statistics

SQL queries are used to manage player records, retrieve team information, and calculate individual and team statistics.

## How It Works

1. The user runs the Python application.
2. The application connects to the Oracle database.
3. The user selects an available team, player, or statistics operation.
4. Python executes the appropriate SQL query.
5. The database retrieves, inserts, updates, or deletes the requested information.
6. The application displays the results to the user.

## Future Development

Potential improvements include:

- A graphical user interface for managing teams and players
- Additional player performance statistics
- More detailed team comparisons
- Player rankings across multiple statistical categories
- Historical season statistics and performance tracking
