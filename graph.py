from graphics import *
import time
from math import floor
from Track import Track

height = 600
width = 600

# number of tracks for each category
n_arr = 3
n_shun = 3
n_dept = 3

# lists in which the tracks will be saved
arr_tracks = []
shunt_tracks = []
dept_tracks = []

# messages for occupancy of each track
arr_messages = []
shunt_messages = []
dept_messages = []

Track('a','b')


# time string to show current time
t_message = []  # store in t_message[0] the displayed text


def change_color(track_list, track_n, win, color):
    '''Given a track, change the color on the UI'''
    time.sleep(1)

    track_list[track_n].rectangle.setFill(color)

    win.update()


def change_message(track_list, track_n, win, new_text):
    '''Given a track, change the text on the UI'''
    track_list[track_n].message.setMessage(new_text)

    win.update()


def change_t(new_t):
    '''Innput new time to update shown t in UI'''
    t_message[0].setText(str(new_t))


def get_middle_point_4_lines(n, track_height, spacing,initial_space):
    '''get position in the middle of tracks on y axis for nice viewing'''
    return floor(((n * track_height) + (
        (n - 1) * spacing)) / 2) + initial_space


def get_middle_track_y_coord(drawing_point, track_height):
    '''get the middle point of the hieght of a single 
    track in y axis to draw line'''
    return (drawing_point + track_height) - floor(track_height / 2)


def initialize(win):

    initial_space = 70  # upper-most space before drawing tracks
    spacing = 20  # space between tracks
    track_height = 25  # rectangle height
    line_width = 1 

    # x coords of points where dept, shunt and dept tracks join
    track_union_coords = [200, 400]

    middle_shunting_y_coord = get_middle_point_4_lines(n_shun, 
        track_height, spacing, initial_space)


    # Arrival tracks ======================

    # on x coords for blocks

    left_block_limit = 20
    right_block_limit = 180
    block_center = 100

    arr_text = Text(Point(100,50), "Arrival Tracks")
    arr_text.setSize(12)
    arr_text.draw(win)

    for arr in range(n_arr):

        drawing_point = (arr * track_height) + (arr * spacing) + initial_space

        track = Track(Rectangle(Point(left_block_limit,drawing_point), 
            Point(right_block_limit,drawing_point + track_height)), 
            Text(Point(block_center,drawing_point + (track_height / 2)), 
            "0"))

        arr_tracks.append(track)

        arr_tracks[arr].rectangle.setFill('green')
        arr_tracks[arr].rectangle.draw(win)

        arr_tracks[arr].message.draw(win)

        # lines
        line_start = (drawing_point + track_height) - floor(track_height / 2)  

        # lines to shunting
        line = Line(Point(right_block_limit, line_start), 
                    Point(track_union_coords[0], middle_shunting_y_coord))
        line.setWidth(line_width)
        line.draw(win) 


    # Shunting tracks ======================

    left_block_limit = 220
    right_block_limit = 380
    block_center = 300

    shunting_text = Text(Point(300,50), "Classification Tracks")
    shunting_text.setSize(12)
    shunting_text.draw(win)

    for shu in range(n_shun):

        drawing_point = (shu * track_height) + (shu * spacing) + initial_space


        track = Track(Rectangle(Point(left_block_limit,drawing_point), 
            Point(right_block_limit,drawing_point + track_height)), 
            Text(Point(block_center,drawing_point + (track_height / 2)), 
            "0"))

        shunt_tracks.append(track)

        shunt_tracks[shu].rectangle.setFill('green')
        shunt_tracks[shu].rectangle.draw(win)

        shunt_tracks[shu].message.draw(win)


        # lines
        middle_track_y_coord = get_middle_track_y_coord(drawing_point, 
                                                        track_height)

        # lines from arrival
        line = Line(Point(track_union_coords[0], middle_shunting_y_coord), 
                    Point(left_block_limit, middle_track_y_coord))
        line.setWidth(line_width)
        line.draw(win) 

        # lines to departure
        line = Line(Point(right_block_limit, middle_track_y_coord), 
                    Point(track_union_coords[1], middle_shunting_y_coord))
        line.setWidth(line_width)
        line.draw(win) 


    # Departure tracks ======================

    left_block_limit = 420
    right_block_limit = 580
    block_center = 500

    departure_text = Text(Point(500,50), "Departure Tracks")
    departure_text.setSize(12)
    departure_text.draw(win)

    for dep in range(n_dept):

        drawing_point = (dep * track_height) + (dep * spacing) + initial_space

        track = Track(Rectangle(Point(left_block_limit,drawing_point), 
            Point(right_block_limit,drawing_point + track_height)), 
            Text(Point(block_center,drawing_point + (track_height / 2)), 
            "0"))

        dept_tracks.append(track)

        dept_tracks[dep].rectangle.setFill('green')
        dept_tracks[dep].rectangle.draw(win)

        dept_tracks[dep].message.draw(win)

        # lines
        middle_track_y_coord = get_middle_track_y_coord(drawing_point, 
                                                        track_height)

        # lines from shunting
        line = Line(Point(track_union_coords[1], middle_shunting_y_coord), 
                    Point(left_block_limit, middle_track_y_coord))
        line.setWidth(line_width)
        line.draw(win) 

    # text messages 
    message = Text(Point(20,20), "t= ")
    message.setSize(12)
    message.draw(win)

    t_message.append(Text(Point(50,20), "0"))
    t_message[0].setSize(12)
    t_message[0].draw(win)

    win.update()


def main():
    win = GraphWin('Shunting Yard Simulation', width, height, autoflush=False)
    win.setCoords(0,height,width,0)

    # starting_points = [20, 180]

    # initialize the empty tracks
    initialize(win)



    # example on changing colors
    # input("Press Enter to continue...")

    change_t(200)
    change_color(arr_tracks,0, win, 'red')

    change_t(250)
    change_color(shunt_tracks,2, win, 'red')

    change_t("11:30")
    change_color(dept_tracks,1, win, 'red')


    # any code goes before this
    # (Dirty) stop the window form closing on click and stop the error message
    try: 
        while True: 
            win.getMouse()
    except GraphicsError:
        pass
    win.close()


main()




