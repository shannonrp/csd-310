#Shannon Russell-Phipps
#Module 8.3 pysports queries
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    #Get team info
    teams = cursor.fetchall()
    print("--Displaying Team Records--")

    for team in teams:

        print("Team ID: {} \n Team Name: {} \n Mascot: {}".format(team[0], team[1], team[2]))

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    #Get player info
    players = cursor.fetchall()

    print ("\n --Displaying Player Records--")

    for player in players:
        print("Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()