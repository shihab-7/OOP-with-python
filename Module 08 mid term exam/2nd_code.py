class Star_Cinema:
    hall_list = []
    def entry_hall(self, rows, cols, hall_no):
        new_hall = Hall(rows, cols, hall_no)
        Star_Cinema.hall_list.append(new_hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id='', movie_name='', time=''):
        showInfo = (id, movie_name, time)
        self.__show_list.append(showInfo)
        seatInfo = []
        rowChar = 65
        for i in range(self.__rows):
            colList = []
            # rowChar = char
            for j in range(self.__cols):
                colList.append(f'{chr(rowChar)}{j}')
            seatInfo.append(colList)
            rowChar += 1
        makeKey = {id: seatInfo}
        self.__seats.update(makeKey)

    def isTicketValid(self, show_id, seatList=[()]):
        validOrBooked = 0
        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    if i[0] > self.__rows or i[1] > self.__cols or i[0] < 0 or i[1] < 0:
                        validOrBooked = 2
                        return validOrBooked
                    elif self.__seats[get_id][i[0]][i[1]] == 'X':
                        validOrBooked = 1
                        print('afljds')
                        return validOrBooked
        return validOrBooked

    def book_seats(self, customer_name, phone_num, show_id, seatList=[()]):

        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    self.__seats[get_id][i[0]][i[1]] = 'X'
        movieDetails = ()
        for i in self.__show_list:
            if i[0] == show_id:
                movieDetails = i
        customer_details = {'name': customer_name, 'phone': phone_num,
                            'show_id': show_id, 'seatList': seatList, 'movieDetails': movieDetails}
        return customer_details

    def view_show_list(self):
        for i in self.__show_list:
            print('\t\tMovie Name: ',
                  i[1], '\t\tShow Id: ', i[0], '\t\tTime: ', i[2])

    def view_available_seats(self, show_id):
        for k in self.__seats[show_id]:
            for j in k:
                print('\t', j, end=' ')
            print('\n')

    def isValidId(self, show_id):
        isValid = True
        for i in self.__show_list:
            if i[0] != show_id:
                isValid = False
            else:
                isValid = True
                return isValid
        return isValid


phitronCinema = Star_Cinema()
phitronCinema.entry_hall(3, 5, 'hall24')
phitronCinema.hall_list[0].entry_show('abcd', 'diwale', 'Oct 31 2022 11:00 PM')
phitronCinema.hall_list[0].entry_show(
    'cdea', 'diwale mr', 'Oct 31 2022 11:00 PM')

# print(dir(phitronCinema.hall_list[0]))
while (1):
    print('1.VIEW ALL SHOWS TODAY\n2.VIEW AVAILABLE SEATS\n3.BOOK TICKET')
    option = input('ENTER OPTION: ')
    if int(option) == 1:
        print('\n')
        print('\t\t-------------------------------------------------------------------------------------')
        phitronCinema.hall_list[0].view_show_list()
        print('\t\t-------------------------------------------------------------------------------------')
        print('\n')
    elif int(option) == 2:
        input_id = input('ENTER SHOW ID: ')
        check_id_validation = phitronCinema.hall_list[0].isValidId(input_id)
        if check_id_validation == True:
            ln = len(phitronCinema.hall_list[0]._Hall__seats[input_id][0])
            print(ln)
            print('\t', end='')
            for i in range(ln):
                print('-------', end='')
            print('\n')
            phitronCinema.hall_list[0].view_available_seats(input_id)
            print('\t', end='')
            for i in range(ln):
                print('-------', end='')
            print('\n')
        else:
            print('\nGiven Show Id is not exists.\nPlease try again in correct one\n')
    elif int(option) == 3:
        name = input('ENTER CUSTOMER NAME : ')
        phone_num = input('ENTER CUSTOMER PHONE NUMBER : ')
        show_id = input('ENTER SHOW ID : ')
        ticketQuantity = input('ENTER NUMBER OF TICKET : ')
        ticketList = []
        useTicket = []
        for i in range(int(ticketQuantity)):
            seatNo = input('ENTER SEAT NO : ')
            useTicket.append(seatNo)
            row = ord(seatNo[0])-65
            col = int(seatNo[1])
            seat = (row, col)
            ticketList.append(seat)
        check_id_validation = phitronCinema.hall_list[0].isValidId(show_id)
        
        if check_id_validation == True:
            ticket_valid_booked = phitronCinema.hall_list[0].isTicketValid(show_id, ticketList)
            if ticket_valid_booked == 0:
                customerBooking = phitronCinema.hall_list[0].book_seats(
                    name, phone_num, show_id, ticketList)
                print('\n')
                print('#### TICKET BOOKED SUCCESSFULLY!! ####')
                print(
                    '-------------------------------------------------------------------------------------')
                print('NAME : ', name)
                print('PHONE NUMBER : ', phone_num)
                print('\n')
                print('MOVIE NAME : ', customerBooking['movieDetails'][1],
                      '\tMOVIE TIME : ', customerBooking['movieDetails'][2])

                print('TICKETS : ', end=' ')
                for i in useTicket:
                    print(i, end=' ')
                print('')
                print('HALL : Hall24')
                print('\n')
                print(
                    '-------------------------------------------------------------------------------------')
                print('\n')
            elif ticket_valid_booked == 1:
                print('\nThis ticket is already booked.\nPlease try another\n')
            elif ticket_valid_booked == 2:
                print('\nThis is not a valid ticket.\nPlease try again\n')
        else:
            print('\nGiven Show Id is not exists.\nPlease try again in correct one\n')
    else:
        print('Your input is not valid.\nPlease try again')


        