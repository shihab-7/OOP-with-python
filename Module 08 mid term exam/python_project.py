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
        self.__seats[id] = seat_inf


    def book_seats(self, show_id, seat_list=[] ):
        if show_id not in self.__seats:
            print('Invalid Show ID')
        for row, col in seat_list:
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[show_id][row][col] !=1:
                    self.__seats[show_id][row][col]='1'
            else:
                print('Invalid seat')
        cinema_details = ()
        for i in self.__show_list:
            if i[0] == show_id:
                cinema_details = i
        ticket = {'Show ID' : show_id, 'Seat No. ': seat_list, 'Show_Details': cinema_details}
        return ticket
    
    
    def view_show_list(self):
        for i in self.__show_list:
            print(f'movie name : {i[1]} show id : {i[0]} time : {i[2]}')

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            for i in self.__seats[show_id]:
                for j in i:
                    print(j,end=' ')
                print('\n')
            print('\n')
        else:
            print('Invalid Show ID')
            

    def check(self, show_id):
        valid_show = True
        for i in self.__show_list:
            if i[0] != show_id:
                valid_show = False
            else:
                valid_show = True
                return valid_show
        return valid_show
    


movie_show = Star_cinema()
movie_show.entry_hall(6, 8, 'Hall no. 105')
movie_show.hall_list[0].entry_show('A0D2', 'Interstellar', '10:00 PM')
movie_show.hall_list[0].entry_show('B0C2', 'Spider Man', '9:00 AM')

while True:
    print('1. View All Shows Today')
    print('2. View Avaiable Seats')
    print('3. Book Tickets')
    print('4. Exit')
    
    option = int(input('Enter option : '))

    if option == 1:
        movie_show.hall_list[0].view_show_list()
    elif option == 2:
        show_id = input('Enter show ID : ')
        check_id =movie_show.hall_list[0].check(show_id)
        if check_id == True:
            movie_show.hall_list[0].view_available_seats(show_id)
        else:
            print('\nYour Given Show ID is invalid\n')
    elif option == 3:
        id = input('Enter show ID : ')
        check_show = movie_show.hall_list[0].check(id)
        if check_show == True:
            row = int(input('Enter row : '))
            col = int(input('Enter column : '))
            ticket = movie_show.hall_list[0].book_seats(id, [(row, col)])
            print(f'Your ticket is booked : {ticket}')
        else:
            print('invalid Show ID')
    elif option == 4:
        break
