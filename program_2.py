# Author: Joseph Kracht
# Last Modified: 9/22/2025
# Title: Movie Tix

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    # Initialize variables
    total_number_of_tickets = 0
    entering_movies = True

    while entering_movies:
        # Get movie name
        movie_name = input('Enter a movie name: ')

        # Get number of tickets
        number_of_tickets = int(input('How many tickets do you want for ' + movie_name + ': '))

        # Add tickets to the total number of tickets
        total_number_of_tickets += number_of_tickets

        # Check if the user wants to loop or end
        want_to_enter_another_movie = input("Enter 'y' to enter another move or enter 'n' to end: ")
        if (want_to_enter_another_movie != 'y'):
            entering_movies = False

    # Print the total number desired tickets
    print('The total number of desired movie tickets is', total_number_of_tickets)


if __name__ == '__main__':
    main()
