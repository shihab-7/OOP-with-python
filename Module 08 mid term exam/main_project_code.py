class Star_cinema:
    hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        Star_cinema.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_inf = (id, movie_name, time)
        self.__show_list.append(show_inf)
        seat_inf = []
        for i in range(self.__rows):
            col_list = []
            for j in range(self.__cols):
                col_list.append('0')
            seat_inf.append(col_list)

        id_list = {id: seat_inf}
        self.__seats.update(id_list)

    def book_seats(self, show_id, seat_list=[]):
        if show_id in self.__seats:
            for i in seat_list:
                row, col = i
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    self.__seats[show_id][row][col] = 'X'
            cinema_details = ()
            for i in self.__show_list:
                if i[0] == show_id:
                    cinema_details = i
            ticket = {'show_id': show_id, 'seat_list': seat_list, 'cinema_details': cinema_details}
            return ticket
        else:
            return None

    def view_show_list(self):
        for i in self.__show_list:
            print(f'movie name: {i[1]} show id: {i[0]} time: {i[2]}')

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            for i in self.__seats[show_id]:
                for j in i:
                    print(j, end=' ')
                print('\n')
        else:
            print('Invalid show ID')

    def check(self, show_id):
        return show_id in self.__seats


movie_show = Star_cinema()
movie_show.entry_hall(6, 8, 'Hall no. 105')
movie_show.hall_list[0].entry_show('A0D2', 'Interstellar', '10:00 PM')
movie_show.hall_list[0].entry_show('B0C2', 'Spider Man', '9:00 AM')

while True:
    print('1. View All Shows Today')
    print('2. View Available Seats')
    print('3. Book Tickets')
    print('4. Exit')

    option = int(input('Enter option: '))

    if option == 1:
        movie_show.hall_list[0].view_show_list()
    elif option == 2:
        show_id = input('Enter show ID: ')
        check_id = movie_show.hall_list[0].check(show_id)
        if check_id:
            movie_show.hall_list[0].view_available_seats(show_id)
        else:
            print('\nYour Given Show ID is invalid\n')
    elif option == 3:
        show_id = input('Enter show ID: ')
        check_show = movie_show.hall_list[0].check(show_id)
        if check_show:
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            ticket = movie_show.hall_list[0].book_seats(show_id, [(row, col)])
            if ticket:
                print('Your ticket has been booked:', ticket)
            else:
                print('Invalid show ID')
        else:
            print('Invalid show ID')
    elif option == 4:
        break
