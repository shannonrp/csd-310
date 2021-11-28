#Shannon Russell-Phipps
#Module 9.3 pysports update and delete
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n --{}--".format(title))
    for player in players:
        print("Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    #Insert player
    add_player = ("INSERT INTO player (first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
    
    player_data = ("Smeagol", "Shire Folk", 1 )

    #insert player
    cursor.execute(add_player, player_data)
    #commit insert to database
    db.commit()

    #Select player info and print
    show_players(cursor, "Displaying players after insert")

    #Update player
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)
        
     #Get player info
    show_players(cursor, "Displaying players after update")

    #Delete player
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    show_players(cursor, "Displaying players after delete")

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