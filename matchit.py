# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Nahal Bagheri and Dasom Lee
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} [image_folder]
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            fast or slow game?
"""

import tkinter
import os
import random
import argparse


class MatchGame(object):

    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    delay (integer): how many milliseconds to wait before flipping a
        tile
    player_color (string): the color to be used for the matched tiles
    selected_tile_coords (tuple or None): the coordinates of the
        currently selected tile or None if no tile is currently selected
    canvas (Tkinter.Canvas object): the canvas widget used to display
        the game board
    score_label (Tkinter.Label object): the label widget used to
        display the player's score
    points (integer): the current number of points the player has
    tries (integer): the current number of tries the player has made
    images_dict (dictionary): a dictionary that maps the names of the
        image files to Tkinter PhotoImage objects
    images_names (list): a list of image file names used in the game
        (each name appears twice, since each image is used in a pair)
    """

    # Add your class variables if needed here - square size, etc...)
    SQUARE_SIZE = 150

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        self.delay = delay
        self.player_color = player_color
        self.selected_tile_coords = None

        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART',
                                        command=self.restart)
        restart_button.grid()

        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=600, height=600)

        for row in range(0, 600, self.SQUARE_SIZE):
            for column in range(0, 600, self.SQUARE_SIZE):
                self.canvas.create_rectangle(row, column,
                                             row + self.SQUARE_SIZE,
                                             column + self.SQUARE_SIZE,
                                             fill="yellow",
                                             outline="black")
        self.canvas.bind("<Button-1>", self.flip)
        self.canvas.grid()

        # Create a label widget for the score and end of game messages
        self.score_label = tkinter.Label(parent, text='Score: 100')
        self.score_label.grid()

        # Create any additional instance variable you need for the game
        self.points = 100
        self.tries = 0

        images_dict = {}
        for file in os.listdir(folder):
            if os.path.splitext(file)[1] == '.gif':
                image = tkinter.PhotoImage(file=folder + "/" + file)
                images_dict[file] = image

        self.images_names = 2 * list(images_dict.values())

        # Call the restart method to finish the initialization
        self.restart()

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It should also be called from __init__ to initialize the game.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        self.hide()
        for img in self.canvas.find_all()[0:16]:
            self.canvas.itemconfigure(img, fill='yellow', tag='',
                                      outline='black')
        self.tries = 0
        self.points = 100
        self.score_label.configure(text='Score: 100')

        random.shuffle(self.images_names)

    def flip(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        tiles = self.canvas.find_withtag(tkinter.CURRENT)
        if tiles:
            tile = tiles[0]
            if 'image' in self.canvas.gettags(tile):
                return
            if tile not in self.canvas.find_withtag('matched') and \
                    len(self.canvas.find_withtag('selected')) <= 2:
                if len(self.canvas.find_withtag('selected')) == 0:
                    self.canvas.itemconfigure(tile, tag='selected')
                    selected_image = self.appear(tile, event)
                    self.selected_tile_coords = self.canvas.coords(tile)
                    self.first_image = selected_image
                elif len(self.canvas.find_withtag('selected')) == 1:
                    first_tile = self.canvas.find_withtag('selected')[0]
                    if tile != first_tile:
                        self.canvas.itemconfigure(tile, tag='selected')
                        second_image = self.appear(tile, event)
                        x, y = self.get_tile_coordinates(tile)
                        if self.first_image == second_image and \
                                (x,y) != self.selected_tile_coords:
                            self.tries += 1
                            self.canvas.after(self.delay, self.hide,
                                              tile,
                                              first_tile)


                        else:
                            self.canvas.after(self.delay, self.hide)
                            self.canvas.after(self.delay,
                                              lambda: self.canvas.
                                              itemconfigure(first_tile,
                                                            tag=''))
                            self.canvas.after(self.delay,
                                              lambda: self.canvas.
                                              itemconfigure(tile,
                                                            tag=''))

                            self.update_score()
                self.canvas.after(self.delay, self.end_game)

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.

    def hide(self, tile=None, first_tile=None):
        """
        This method is called after a delay to hide the two tiles that
        were flipped.  The method will also change the tile color to the
        user specified color if there is a match.
        :param tile: (optional) the second tile that was flipped
        :param first_tile: (optional) the first tile that was flipped
        :return: None
        """
        p_color = self.player_color
        tile_config = self.canvas.itemconfigure(tile, fill=p_color,
                                                outline=p_color, )
        first_tile_config = self.canvas.itemconfigure(first_tile,
                                                      fill=p_color,
                                                      outline=p_color)
        matched_tile = self.canvas.itemconfigure(tile, tag='matched')
        first_matched_tile = self.canvas.itemconfigure(first_tile,
                                                       tag='matched')

        self.canvas.delete('image')
        self.canvas.after(self.delay, lambda: tile_config)
        self.canvas.after(self.delay, lambda: first_tile_config)
        self.canvas.after(self.delay, lambda: matched_tile)
        self.canvas.after(self.delay, lambda: first_matched_tile)

    def get_tile_coordinates(self, tile_id):
        """
        Get the x,y coordinates of a tile on the canvas.
        :param tile_id: the id of the tile on the canvas.
        :return: tuple of the x,y coordinates
        """
        x1, y1, x2, y2 = self.canvas.coords(tile_id)
        x = (x2 - x1) / 2
        y = (y2 - y1) / 2
        return x1 + x, y1 + y

    def appear(self, tile, event):
        """
        Shows the image of a selected tile
        :param tile: the tile on which the image is to be displayed
        :param event: event (Event object) describing the click event
        :return: image (tkinter.PhotoImage)
        """
        x, y = self.get_tile_coordinates(tile)
        image_index = self.canvas.find_withtag(tile)[0] - 1
        image = self.images_names[image_index]
        self.canvas.create_image(x, y, image=image, tag='image')
        return image

    def update_score(self):
        """
        This method updates the score based on the number of tries.
        :return: None
        """
        self.tries += 1
        if self.tries > 13:
            self.points -= 10
            self.score_label.configure(text=f"Score: {self.points}")

    def end_game(self):
        """
        This method is called after each flip to check if the game
            has ended.
        If all tiles are matched, the method displays a message box
            with the final score and number of tries.
        :return: None
        """
        if len(self.canvas.find_withtag('matched')) == 16:
            self.score_label.configure(text=f'Game over!\nScore: '
                                       f'{self.points}\nNumber '
                                            f'of tries: {self.tries}')

# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.


def valid_images(image_folder):
    """
    This function takes a folder path as input and returns a list of
    valid image files in the folder.
    A valid image file is defined as a file with a '.gif' extension.
    :param image_folder: (str)The path to the folder containing image
    files.
    :return: A list of valid image files in the folder.
    """
    if not os.path.exists(image_folder):
        raise argparse.ArgumentTypeError(f"{image_folder} is not a "
                                         f"valid folder")
    else:
        if len([img_file for img_file in os.listdir(image_folder) if
                img_file.endswith('.gif')]) < 8:
            raise argparse.ArgumentTypeError(f"{image_folder} must "
                                             f"contain at least 8 gif "
                                             f"images")
    return image_folder


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the player color (string), the image
    folder (string) and the fast option (boolean)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color', help='What color would you like for '
                                      'the player?'
                        , choices=['blue', 'green', 'magenta'])
    parser.add_argument('image_folder', help='What folder contains the'
                                             ' game images?',
                        nargs='?', type=valid_images,
                        default="images")
    parser.add_argument('-f', '--fast', help='Fast or slow game?',
                        action='store_true')

    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast

    return color, image_folder, fast


def main():
    # Retrieve and validate the command line arguments using argparse
    color, folder, fast = get_arguments()
    delay = 1000 if fast else 3000

    # Instantiate a root window
    root = tkinter.Tk()

    # Instantiate a MatchGame object with the correct arguments
    MatchGame(root, color, folder, delay)

    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()