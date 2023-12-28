# import sqlite3
# from datetime import datetime

# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()

new_user = 'INSERT INTO Employees (id, name, second_name) VALUES (?, ?, ?)'
entex = 'INSERT INTO Logs (operation_id, user_id, type, time, is_guest, parking_place) VALUES (?, ?, ?, ?, ?, ?)'
add_guest = 'INSERT INTO Guests (id, name, second_name, time_left) VALUES (?, ?, ?, ?)'
delete_guest = 'DELETE FROM Guests WHERE id = ?'
add_park = 'INSERT INTO Parking (id, type, user_id) VALUES (?, ?, ?)'
delete_table = 'DROP TABLE Logs'
get_last_user = 'SELECT * FROM Employees ORDER BY id DESC LIMIT 1 OFFSET 0'
get_last_guest = 'SELECT * FROM Guests ORDER BY id DESC LIMIT 1 OFFSET 0'
get_last_entex = 'SELECT * FROM Logs ORDER BY operation_id DESC LIMIT 1 OFFSET 0'
get_last_entex_by_user = 'SELECT * FROM Logs WHERE is_guest = False AND user_id = ? ORDER BY operation_id DESC LIMIT 1 OFFSET 0'
get_last_guestentex_by_user = 'SELECT * FROM Logs WHERE is_guest = True AND user_id = ? ORDER BY operation_id DESC LIMIT 1 OFFSET 0'
get_all_users = 'SELECT * FROM Employees'
get_user_by_id = 'SELECT * FROM Employees WHERE id = ?'
get_all_guests = 'SELECT * FROM Guests'
get_all_guests_by_id = 'SELECT * FROM Guests WHERE id = ?'
get_parking_by_id = 'SELECT * FROM Parking WHERE id = ?'
get_all_parking_by_type = 'SELECT * FROM Parking WHERE type = ? and user_id = 0'
update_parking = 'UPDATE Parking SET user_id = ? WHERE id = ?'


#cursor.execute(delete_table)
# print(cursor.fetchall())

# connection.commit()
# connection.close()