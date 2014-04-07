# Import
import sqlite3


# Function
class MovieReservationSystem():

    """docstring for MovieReservationSystem"""

    def __init__(self):

        self.conn = sqlite3.connect('cinemaDB.db')
        self.c = self.conn.cursor()

    def movies_in_cinema(self):

        print('')
        print("Current movies:")

        sql_to_read = "SELECT ID, Name, Rating FROM movies"
        for row in self.c.execute(sql_to_read):
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

        return ""

    def show_movies(self):

        print('')
        print("Current movies:")

        sql_to_read = "SELECT ID, Name, Rating FROM movies ORDER BY rating ASC"
        for row in self.c.execute(sql_to_read):
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

        return ""

    def show_movie_projections(self, movie_id):

        movie = self.c.execute("SELECT Name FROM movies where ID = ?", (movie_id,)).fetchone()[0]

        print("")
        print("Projections for movie '{}':".format(movie))

        sql_to_read = "SELECT ID, date, time, type FROM projection where movie_id = ?"

        for row in self.c.execute(sql_to_read, (movie_id,)):
            print("[{}] - {} ({})".format(row[0], row[1], row[2], row[3]))

        return ""

    def show_movie_projections_by_date(self, movie_id, date):

        movie = self.c.execute("SELECT Name FROM movies where ID = ?", (movie_id,)).fetchone()[0]

        date = self.c.execute("SELECT date FROM projection where date = ?", (date,)).fetchone()[0]

        print("")
        print("Projections for movie '{}' on date {}:".format(movie, date))

        sql_to_read = "SELECT ID, time, type FROM projection where date = ?"

        for row in self.c.execute(sql_to_read, (date,)):
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

        return ""

    def make_reservation(self):

        print('')
        print("Step 1")
        user_name = input("Choose name>")
        ticket_num = int(input("Choose number of tickets>"))
        self.movies_in_cinema()

        print('')
        print("Step 2 Choose a movie")
        choose_movie = input("Choose a movie>")
        self.show_movie_projections(choose_movie)

        print('')
        print("Step 3 - Choose a projection")
        choose_projection = input("Choose a projection> ")

        seats = [
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

        print('')
        print("Available seats marked with 0s")
        print(' ' + ' ' + '1 2 3 4 5 6 7 8 9 10')

        index = 1
        for i in seats:
            print("{} ".format(index) + " ".join(i))
            index += 1
        print("")

        seats_to_choose = 1
        choosen_seats = []

        while ticket_num != 0:
            print('Now choose seat for the {} person'.format(seats_to_choose))
            choose_seat_row = int(input('Choose row>'))
            choose_seat_num = int(input('Choose seat number>'))
            choosen_seats.append((choose_seat_row, choose_seat_num))
            if (choose_seat_row) < 11 or (choose_seat_num) < 11:

                if seats[(choose_seat_row) - 1][(choose_seat_num) - 1] == "X":
                    print('this seat sis already taken!')

                else:
                    seats[(choose_seat_row) - 1][(choose_seat_num) - 1] = "X"
            else:
                print('Lol Noo.. try again')

            ticket_num -= 1
            seats_to_choose += 1

        if ticket_num == 0:

            movie = self.c.execute("SELECT Name FROM movies where ID = ?", (choose_movie,)).fetchone()[0]

            projection = self.c.execute("SELECT date FROM projection WHERE ID = ?", (choose_projection,)).fetchone()[0]

            print('')
            print('This is your reservation: ')
            print('Reservation under the name of {}'.format(user_name))
            print('Movie: {}'.format(movie))
            print('Date & Time: {}'.format(projection))
            print('Seats: {}'.format(choosen_seats))
            return "THANKS"
