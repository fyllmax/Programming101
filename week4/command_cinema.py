from cinema import MovieReservationSystem


class CinemaConsole():
    """docstring for CinemaConsole"""
    def __init__(self, parser):

        self.parser = parser

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def movie_in_cinema(self):
        return self.parser.movies_in_cinema()

    def movie_by_rating(self):
        return self.parser.show_movies()

    def projections(self, projection_id):
        return self.parser.show_movie_projections(projection_id)

    def projections_by_date(self, movie_id, date):
        return self.parser.show_movie_projections_by_date(movie_id, date)

    def make_reservation(self):
        return self.parser.make_reservation()

    def create_menu(self):
        menu = [
            '',
            'Welcome to Our Cinema',
            'you can check our programe',
            'and even make reservations',
            'for instructions, just type "help"']

        return('\n'.join(menu))

    def create_help(self):

        help_menu = [
            '',
            'Here is full list of commands: ',
            '*movie_offers - will give you list of movies in the theatre',
            '*box_office - will show the movies ordered by rating',
            '*projecions <ID> - time and date of movie projections',
            '*projectios_by_date <ID, Date>- upcoming projections in near time',
            '*make_reservation - place to book a ticket for given movie']

        return('\n'.join(help_menu))

    def unknown_command(self):
        return("Unknown Command, try again!")
