#! /usr/bin/env python
# The line above tells some systems (e.g. Linux/Apple shells) what program to
# use to execute this script.

##############################################################################
# You don't need to understand most of this yet- you can just skip to the    #
# large comment section below if this is all a bit daunting!                 #
##############################################################################

# Import the libraries we need
import sys
from music21 import (
    environment,
    metadata,
    note,
    stream,
    )

# Tell music21 what to use to play midi and display score
environment.set('midiPath', '/usr/bin/timidity')
environment.set('musicxmlPath', '/usr/bin/musescore')

##############################################################################
#                            LESSON 1 STARTS HERE                            #
#############################################################################

# This is our first lesson, so play a scale with our right hand

# Create the first bar, in the default 4/4 time
bar1_right = stream.Measure()
# Add each note we want to play in turn to the bar
bar1_right.append(note.Note('c4'))
bar1_right.append(note.Note('d4'))
bar1_right.append(note.Note('e4'))
bar1_right.append(note.Note('f4'))

# Create the second bar
bar2_right = stream.Measure()
# Add each note we want to play in turn to the bar
bar2_right.append(note.Note('g4'))
bar2_right.append(note.Note('a4'))
bar2_right.append(note.Note('b4'))
bar2_right.append(note.Note('c5'))

# You can try putting in the bars to play back down to middle C here.
# Don't forget to add them to the right hand's bars below!

# Add both of these bars to the right hand's part
right_hand = stream.Part()
right_hand.append(bar1_right)
right_hand.append(bar2_right)

# Add the right hand to the score
tune = stream.Score(right_hand)

# Add a title
tune.metadata = metadata.Metadata(title='Python TTTGLS: Lesson 1')

##########################################################################
#                        LESSON 1 ENDS HERE                              #
##########################################################################

# Only run this if the script is executed directly, not imported
if __name__ == '__main__':
    # Complain if there were no arguments passed by the user
    if len(sys.argv) == 1:
        # First, print a helpful message
        print('add a "score" argument to see the score.')
        print('add a "text" argument to see the python objects.')
        print('add a "midi" argument to hear it.')
        print('e.g. To hear the tune: {command} midi'.format(
            command=sys.argv[0],
            ))
        # Now exit without doing anything
        sys.exit()

    # See if the user put the word 'midi' in the arguments
    if 'midi' in sys.argv:
        # The stream.Score (tune) object knows how to play itself using the
        # environment set midi player and will do so when its show method is
        # called with a 'midi' argument.
        tune.show('midi')

    # See if the user put the word 'text' in the arguments
    if 'text' in sys.argv:
        # The stream.Score (tune) object knows how to display itself as python
        # objects in text, and will do so when its show method is called with
        # a 'text' argument.
        tune.show('text')

    # See if the user put the word 'score' in the arguments
    if 'score' in sys.argv:
        # The stream.Score (tune) object knows how to display itself as
        # musical score, and will do so by default when its show method is
        # called with no arguments.
        tune.show()
