import pandas as pd

# operational state matrix
operation_columns=['event','train_no',
    'block','start_time', 'end_time', 'EHT']

# Resource State Matrix
classification_columns=['event', 'track_no', 'wagon_no',
    'remaining_capacity', 'destination', 'start_time', 'end_time', 'state']

# Infrastructure state matrix
departure_columns=['event','track_no','block_no', 
    'destination', 'time']

# first exercise

cl_event = ['O', 'O', 'O', 'O', 'R', 'O', 'R', 'O', 'R', 'O', 'O', 'R', 'O', 
    'R', 'O', 'R', 'R']

cl_trackno = [1, 3, 5, 1, 1, 3, 3, 5, 5, 1, 5, 5, 3, 3, 3, 3, 1]

cl_wagon_no = [8, 9, 10, 38, 0, 14, 0, 12, 0, 30, 5, 0, 20, 0, 15, 0, 0]

cl_ramaining_cap = [42, 41, 40, 12, 50, 36, 50, 38, 50, 20, 45, 50, 30, 50, 
    35, 50, 30]

cl_destination = ['B1', 'B2', 'B5', 'B1', 'B1', 'B2', 'B2', 'B5', 'B5', 
    'B3', 'B5', 'B5', 'B1', 'B1', 'B2', 'B2', 'B3']

cl_start_time = ['9:00', '9:00', '9:00', '9:30', '9:45', '9:45', '9:50', 
    '9:50', '9:55', '9:55', '10:10', '10:15', '10:15', '10:20', '10:25', 
    '10:30', '11:00']

cl_end_time = ['9:00', '9:00', '9:00', '9:45', '9:50', '9:50', '9:55', 
    '9:55', '10:00', '10:10', '10:15', '10:20', '10:25', '10:25', '10:30', 
    '10:35', '11:05']

cl_state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


events = [cl_event, cl_trackno, cl_wagon_no, cl_ramaining_cap, cl_destination, 
cl_start_time, cl_end_time, cl_state]

classification_dict = {}

for count, e in enumerate(events):
    # print(len(e))
    classification_dict[classification_columns[count]] = e


# print(classification_dict.keys())

cl_matrix = pd.DataFrame(classification_dict)

print(cl_matrix.dtypes)


