**!!NOTICE!!:** This project is no longer developed or maintained.

# PyMSWPR

A version of Minesweeper written in Python for the CASIO fx-9750GIII.

## Controls

- 8   - Move up.
- 2   - Move down.
- 4   - Move left.
- 6   - Move right.
- 7   - Toggle flag on current cell.
- 9   - Reveal current cell (only if not flagged.)
- EXE - Submit moves.

You can queue up the moves you would like to make by entering them one after
another. They will appear on the bottom row of the screen. Press EXE (or enter
or whatever you want to call it) to submit your moves, after which they will be
processed one by one and the screen will update when finished. Press AC at any
time to quit.

If you uncover all empty cells, "You win!" will be displayed. If you uncover a
bomb, "BOOM!" will be displayed. After finishing a game the entire board will be
revealed. If you wish to play again, press EXE, and a new board will be
generated.

Due to the random number generator given by the calculator not working
what-so-ever, and there being no source of randomness other than you, the user,
you should first wildly move about the board to initialize the generator so that
it generates a new board. This is only neccessary right after you start the
program, as the game continues accumulating randomness from you and uses it when
you play again (not saved.)

## Installation

Connect the calculator to a computer via USB. Open the main menu and select link
(E). Hit F2 for RECV and wait for it to finish. Then you should be able to open
it as a folder on the computer. Simply place `PyMSWPR.py` into the calculator's
folder, eject it, and unplug.

In the event that it does not give you the option to open the folder, you may
need to install drivers for it
(https://edu.casio.com/support/en/agreement.html#2) Hit Accept (only if you
accept lol) and download fx-9860GII series > Support Software > PC Link Software
\> FA-124. The installer will install the drivers you need along with FA-124.

## Links

Video demonstration:<br>
https://odysee.com/@ona-li-toki-e-jan-Epiphany-tawa-mi:9/A-Minesweeper-clone-on-a-shitty-%28programming-wise%29-calculator.:e?r=HYroMZaqrVN4gL5oSJ35gcTgt3K56r39
