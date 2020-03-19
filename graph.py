from graphics import *
import time
from math import floor

height = 600
width = 600

# number of tracks for each category
n_arr = 6
n_shun = 8
n_dept = 2

# lists in which the tracks will be saved
arr_tracks = []
shunt_tracks = []
dept_tracks = []

# time string to show current time
t_message = []  # store in t_message[0] the displayed text


def change_color(track, win, color):
    '''Given a track, change the color on the UI'''
    time.sleep(1)

    track = Rectangle(track.getP1(), track.getP2())

    track.setFill(color)
    track.draw(win)
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

    middle_shunting_y_coord = get_middle_point_4_lines(n_shun, 
        track_height, spacing, initial_space)

    # Arrival tracks

    arr_text = Text(Point(100,50), "Arrival Tracks")
    arr_text.setSize(12)
    arr_text.draw(win)

    for arr in range(n_arr):

        drawing_point = (arr * track_height) + (arr * spacing) + initial_space

        arr_tracks.append(Rectangle(Point(20,drawing_point), 
            Point(180,drawing_point + track_height)))

        arr_tracks[arr].setFill('green')
        arr_tracks[arr].draw(win)


        # lines
        line_start = (drawing_point + track_height) - floor(track_height / 2)  

        # lines to shunting
        line = Line(Point(180, line_start), 
                    Point(200, middle_shunting_y_coord))
        line.setWidth(line_width)
        line.draw(win) 


    # Shunting tracks

    shunting_text = Text(Point(300,50), "Classification Tracks")
    shunting_text.setSize(12)
    shunting_text.draw(win)

    for shu in range(n_shun):

        drawing_point = (shu * track_height) + (shu * spacing) + initial_space

        shunt_tracks.append(Rectangle(Point(220,drawing_point), 
            Point(380,drawing_point + track_height)))

        shunt_tracks[shu].setFill('green')
        shunt_tracks[shu].draw(win)


        # lines
        middle_track_y_coord = get_middle_track_y_coord(drawing_point, 
                                                        track_height)

        # lines from arrival
        line = Line(Point(200, middle_shunting_y_coord), 
                    Point(220, middle_track_y_coord))
        line.setWidth(line_width)
        line.draw(win) 

        # lines to departure
        line = Line(Point(380, middle_track_y_coord), 
                    Point(400, middle_shunting_y_coord))
        line.setWidth(line_width)
        line.draw(win) 


    # Departure tracks

    departure_text = Text(Point(500,50), "Departure Tracks")
    departure_text.setSize(12)
    departure_text.draw(win)

    for dep in range(n_dept):

        drawing_point = (dep * track_height) + (dep * spacing) + initial_space

        dept_tracks.append(Rectangle(Point(420,drawing_point), 
            Point(580,drawing_point + track_height)))

        dept_tracks[dep].setFill('green')
        dept_tracks[dep].draw(win)

        # lines
        middle_track_y_coord = get_middle_track_y_coord(drawing_point, 
                                                        track_height)

        # lines from shunting
        line = Line(Point(400, middle_shunting_y_coord), 
                    Point(420, middle_track_y_coord))
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

    # TODO: control the movement in time

    # TODO: create log... maybe this is a part for the matrixes

    # TODO: be able to move forward-backards in time

    # TODO: be able to add delay to matrix


    # example on changing colors
    # input("Press Enter to continue...")

    change_t(200)
    change_color(arr_tracks[0], win, 'red')

    change_t(250)
    change_color(shunt_tracks[2], win, 'red')

    change_t("11:30")
    change_color(dept_tracks[1], win, 'red')


    # any code goes before this
    # (Dirty) stop the window form closing on click and stop the error message
    try: 
        while True: 
            win.getMouse()
    except GraphicsError:
        pass
    win.close()


main()




