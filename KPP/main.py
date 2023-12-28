from PyQt6.QtWidgets import QApplication, QMainWindow
from datetime import datetime, timedelta
import sys, sqlite3

main_win = 0
ent_ex = 0
notif = 0
regist = 0

def main():
    setup()
    app = QApplication(sys.argv)
    import main_window, entry_exit, notification, registration
    global main_win, ent_ex, notif, regist

    main_win = QMainWindow()
    main_win.setCentralWidget(main_window.centralwidget)
    main_win.resize(861, 697)

    ent_ex = QMainWindow()
    ent_ex.setCentralWidget(entry_exit.centralwidget)
    ent_ex.resize(580, 433)

    notif = QMainWindow()
    notif.setCentralWidget(notification.centralwidget)
    notif.resize(679, 246)

    regist = QMainWindow()
    regist.setCentralWidget(registration.centralwidget)
    regist.resize(554, 237)

    #signals
    main_window.ExitEntryBtn.clicked.connect(ent_winStart)
    main_window.NewEmployeeBtn.clicked.connect(registWin)
    registration.Submit.clicked.connect(registrate)
    entry_exit.Submit.clicked.connect(enrty)

    main_win.show()
    update()
    # ent_ex.show()
    # notif.show()
    # regist.show()
    
    sys.exit(app.exec())


def setup():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
                    id INTEGER,
                    name TEXT,
                    second_name TEXT          
)
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Logs (
                    operation_id INTEGER,
                    user_id INTEGER,
                    type TEXT,
                    time TEXT,
                    is_guest BLOB,
                    parking_place INTEGER
)
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Guests (
                    id INTEGER,
                    name TEXT,
                    second_name TEXT,
                    time_left INTEGER
)
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Parking (
                    id INTEGER,
                    type TEXT,
                    user_id INTEGER
)
''')
    connection.commit()
    connection.close()


def ent_winStart():
    global ent_ex
    import entry_exit
    entry_exit.Error1.setVisible(False)
    entry_exit.Error2.setVisible(False)
    entry_exit.Error3.setVisible(False)
    entry_exit.Error4.setVisible(False)
    entry_exit.PlacesLeft.setVisible(False)
    entry_exit.IfEntry.setChecked(True)
    entry_exit.GuestTime.setText('')
    entry_exit.Name.setText('')
    entry_exit.SecondName.setText('')
    entry_exit.ID.setText('')
    entry_exit.IfGuest.setChecked(False)
    entry_exit.IfParking.setChecked(False)
    entry_exit.Confirm.setChecked(False)
    ent_ex.show()


def registWin():
    global regist
    import registration
    registration.NameEntry.setText('')
    registration.SecondNameEntry.setText('')
    registration.Confirm.setChecked(False)
    registration.Error1.setVisible(False)
    registration.Error2.setVisible(False)
    regist.show()


def notifWin(label1, label2):
    global notif
    import notification
    notification.MainLabel.setText(label1)
    notification.SecondLabel.setText(label2)
    notification.AdminKeyEdit.setVisible(False)
    notification.AdminKEyLAbel.setVisible(False)
    notification.Submit.setVisible(False)
    notif.show()


def registrate():
    global regist
    import registration, db_works
    name = registration.NameEntry.text()
    second_name = registration.SecondNameEntry.text()
    confirm = registration.Confirm.isChecked()
    error = False
    if name == '':
        error = True
        registration.Error1.setVisible(True)
    if second_name == '':
        error = True
        registration.Error2.setVisible(True)
    if error:
        return False
    else:
        registration.Error1.setVisible(False)
        registration.Error2.setVisible(False)

    if confirm == True:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Employees ORDER BY id DESC LIMIT 1 OFFSET 0')
        last_id = cursor.fetchall()
        if len(last_id) > 0:
            last_id = last_id[0][0]
        else:
            last_id = 0
        cursor.execute(db_works.new_user, (int(last_id)+1, name, second_name))
        connection.commit()
        connection.close()
        update()
        regist.hide()


def enrty():
    import entry_exit
    global ent_ex
    error = False
    second_name = entry_exit.SecondName.text()
    name = entry_exit.Name.text()
    id = entry_exit.ID.text()
    ifentry = entry_exit.IfEntry.isChecked()
    ifparking = entry_exit.IfParking.isChecked()
    ifguest = entry_exit.IfGuest.isChecked()
    guest_time = entry_exit.GuestTime.text()
    confirm = entry_exit.Confirm.isChecked()
    if (id.isdigit() != True or id == '') and ifguest != True:
        entry_exit.Error4.setVisible(True)
        error = True
    if name == '':
        entry_exit.Error3.setVisible(True)
        error = True
    if second_name == '':
        entry_exit.Error2.setVisible(True)
        error = True
    if ifguest == True and (guest_time.isdigit() != True or guest_time == '') and ifentry != False:
        entry_exit.Error1.setVisible(True)
        error = True
    if error:
        return False
    else:
        entry_exit.Error1.setVisible(False)
        entry_exit.Error2.setVisible(False)
        entry_exit.Error3.setVisible(False)
        entry_exit.Error4.setVisible(False)
    
    if confirm:
        import db_works
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(db_works.get_all_parking_by_type, ('employee', ))
        employee_parking = cursor.fetchall()
        print(employee_parking)
        cursor.execute(db_works.get_all_parking_by_type, ('guest', ) )
        guest_parking = cursor.fetchall()
        cursor.execute(db_works.get_last_entex)
        last_id = cursor.fetchall()
        cursor.execute(db_works.get_all_users)
        all_users = cursor.fetchall()
        if ifguest != True:
            cursor.execute(db_works.get_user_by_id, (int(id),))
        user_data = cursor.fetchall()
        cursor.execute(db_works.get_last_guest)
        last_guest_id = cursor.fetchall()
        if len(last_guest_id) > 0:
            last_guest_id = last_guest_id[0][0]
        else:
            last_guest_id = 0
        if len(last_id) > 0:
            last_id = last_id[0][0]
        else:
            last_id = 0
        if ifentry:
            if not(ifguest):
                if len(user_data) != 0:
                    if user_data[0][1] == name and user_data[0][2] == second_name:
                        cursor.execute(db_works.get_last_entex_by_user, (int(id), ))
                        last_entry = cursor.fetchall()
                        if len(last_entry) > 0:
                            if last_entry[0][2] == "exit":
                                if ifparking:
                                    if len(employee_parking) > 0:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, employee_parking[0][0]))
                                        cursor.execute(db_works.update_parking, (int(user_data[0][0]), employee_parking[0][0]))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    elif len(guest_parking) > 0:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, guest_parking[0][0]))
                                        cursor.execute(db_works.update_parking, (int(user_data[0][0]), guest_parking[0][0]))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    else:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, 0))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                        notifWin('Извините!', 'На данный момент свободных парковочных мест, \nдоступных для вас, нет!')
                                else:
                                    cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, 0))
                                    connection.commit()
                                    connection.close()
                                    update()
                                    ent_ex.hide()
                        else:
                            if ifparking:
                                    if len(employee_parking) > 0:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, employee_parking[0][0]))
                                        cursor.execute(db_works.update_parking, (int(user_data[0][0]), employee_parking[0][0]))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    elif len(guest_parking) > 0:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, guest_parking[0][0]))
                                        cursor.execute(db_works.update_parking, (int(user_data[0][0]), guest_parking[0][0]))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    else:
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, 0))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                        notifWin('Извините!', 'На данный момент свободных парковочных мест, \nдоступных для вас, нет!')
                            else:
                                cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "entry", datetime.now(), False, 0))
                                connection.commit()
                                connection.close()
                                update()
                                ent_ex.hide()
                    else:
                        notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте авторизоваться как гость.')
                else:
                    notifWin('Извините!', 'Вас нет в базе данных, попробуйте авторизоваться как гость.')
            else:
                if ifparking:
                        if len(guest_parking) > 0:
                            cursor.execute(db_works.entex, (int(last_id)+1, int(last_guest_id)+1, "entry", datetime.now(), True, guest_parking[0][0]))
                            cursor.execute(db_works.update_parking, (int(last_guest_id)+1, guest_parking[0][0]))
                            cursor.execute(db_works.add_guest, (int(last_guest_id)+1, name, second_name, int(guest_time)))
                            connection.commit()
                            connection.close()
                            update()
                            ent_ex.hide()
                            notifWin('Добро пожаловать!', f'Ваш гостевой ID: {int(last_guest_id)+1}.')
                        else:
                            cursor.execute(db_works.entex, (int(last_id)+1, int(last_guest_id)+1, "entry", datetime.now(), True, 0))
                            cursor.execute(db_works.add_guest, (int(last_guest_id)+1, name, second_name, int(guest_time)))
                            connection.commit()
                            connection.close()
                            update()
                            ent_ex.hide()
                            notifWin('Извините!', f'На данный момент свободных парковочных мест, доступных для вас, нет! \nВаш гостевой ID: {int(last_guest_id)+1}.')
                else:
                    cursor.execute(db_works.entex, (int(last_id)+1, int(last_guest_id), "entry", datetime.now(), True, 0))
                    cursor.execute(db_works.add_guest, (int(last_guest_id)+1, name, second_name, int(guest_time)))
                    connection.commit()
                    connection.close()
                    update()
                    ent_ex.hide()
                    notifWin('Добро пожаловать!', f'Ваш гостевой ID: {int(last_guest_id)+1}.')
        else:
            if not(ifguest):
                if len(user_data) != 0:
                    if user_data[0][1] == name and user_data[0][2] == second_name:
                        cursor.execute(db_works.get_last_entex_by_user, (int(id), ))
                        last_entry = cursor.fetchall()
                        if len(last_entry) > 0:
                            if last_entry[0][2] == "entry":
                                if last_entry[0][5] != 0:
                                    cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "exit", datetime.now(), False, last_entry[0][5]))
                                    cursor.execute(db_works.update_parking, (0, last_entry[0][5]))
                                    connection.commit()
                                    connection.close()
                                    update()
                                    ent_ex.hide()
                                else:
                                    cursor.execute(db_works.entex, (int(last_id)+1, int(user_data[0][0]), "exit", datetime.now(), False, last_entry[0][5]))
                                    connection.commit()
                                    connection.close()
                                    update()
                                    ent_ex.hide()
                            else:
                                notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.')
                        else:
                            notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.')
                    else:
                        notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.')
                else:
                    notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.')
            else:
                cursor.execute(db_works.get_all_guests_by_id, (int(id), ))
                last_guest = cursor.fetchall()
                if len(last_guest) != 0:
                    if last_guest[0][1] == name and last_guest[0][2] == second_name:
                        cursor.execute(db_works.get_last_guestentex_by_user, (int(id), ))
                        guest_time = last_guest[0][3]
                        last_entry = cursor.fetchall()
                        if len(last_entry) > 0:
                            if last_entry[0][2] == "entry":
                                if last_entry[0][5] != 0:
                                    enrty_time = last_entry[0][3].split()[1]
                                    current_time = str(datetime.now())
                                    current_time = current_time.split()[1]
                                    enrty_time = timedelta(hours=int(enrty_time.split(":")[0]), minutes=int(enrty_time.split(":")[1]), seconds=float(enrty_time.split(":")[2])) + timedelta(hours=int(guest_time))
                                    if enrty_time != (timedelta(hours=int(current_time.split(':')[0])) + timedelta(minutes=int(current_time.split(':')[1])) + timedelta(seconds=float(current_time.split(':')[2]))):
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(id), "exit", datetime.now(), True, last_entry[0][5]))
                                        cursor.execute(db_works.update_parking, (0, last_entry[0][5]))
                                        cursor.execute(db_works.delete_guest, (int(id), ))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    else:
                                        notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.1')
                                else:
                                    enrty_time = last_entry[0][3].split()[1]
                                    current_time = str(datetime.now())
                                    current_time = current_time.split()[1]
                                    enrty_time = timedelta(hours=int(enrty_time.split(":")[0]), minutes=int(enrty_time.split(":")[1]), seconds=float(enrty_time.split(":")[2])) + timedelta(hours=int(guest_time))
                                    if enrty_time != (timedelta(hours=int(current_time.split(':')[0])) + timedelta(minutes=int(current_time.split(':')[1])) + timedelta(seconds=float(current_time.split(':')[2]))):
                                        cursor.execute(db_works.entex, (int(last_id)+1, int(id), "exit", datetime.now(), True, 0))
                                        cursor.execute(db_works.delete_guest, (int(id), ))
                                        connection.commit()
                                        connection.close()
                                        update()
                                        ent_ex.hide()
                                    else:
                                        notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.2')
                            else:
                                notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.3')
                        else:
                            notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.4')
                    else:
                        notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.5')
                else:
                    notifWin('Извините!', 'Похоже ваши данные указаны неправильно или вас нет в базе данных. \nПоробуйте вызвать сотрудника.6')



                                    

                    


def update():
    import main_window
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Logs')
    logs = cursor.fetchall()
    cursor.execute('SELECT * FROM Guests')
    guests = cursor.fetchall()
    cursor.execute('SELECT * FROM Parking')
    parking = cursor.fetchall()
    cursor.execute('SELECT * FROM Employees')
    users = cursor.fetchall()

    text1 = ''
    for i in logs:
        text1 += str(i) + '\n'
    main_window.History.setText(text1)
    text2 = ''
    for i in guests:
        text2 += str(i) + '\n'
    main_window.GuestsList.setText(text2)
    text3 = ''
    for i in parking:
        text3 += str(i) + '\n'
    main_window.Parking.setText(text3)
    text4 = ''
    for i in users:
        text4 += str(i) + '\n'
    main_window.EmployeeList.setText(text4)


if __name__ == "__main__":
    main()