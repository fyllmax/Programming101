# Import
from cinema import MovieReservationSystem
from command_cinema import CinemaConsole


def main():

    Arena = MovieReservationSystem()
    arena_console = CinemaConsole(Arena)

    print(arena_console.create_menu())

    while True:

        command = arena_console.parse_command(input("Enter command>"))

        if arena_console.is_command(command, "help"):
            print(arena_console.create_help())

        elif arena_console.is_command(command, "movie_offers"):
            print(arena_console.movie_in_cinema())

        elif arena_console.is_command(command, "box_office"):
            print(arena_console.movie_by_rating())

        elif arena_console.is_command(command, "projections"):
            print(arena_console.projections(command[1]))

        elif arena_console.is_command(command, "projections_by_date"):
            print(arena_console.projections_by_date(command[1], command[2]))

        elif arena_console.is_command(command, "make_reservation"):
            print(arena_console.make_reservation())

        elif arena_console.is_command(command, "exit"):
            break

        else:
            print(arena_console.unknown_command())


if __name__ == '__main__':
    main()
