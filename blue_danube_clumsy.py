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
#                            LESSON 3 STARTS HERE                            #
#############################################################################
right_hand = stream.Part()
left_hand = stream.Part()

bar1_right = stream.Measure()
bar1_right.clef = clef.TrebleClef()
bar1_right.timeSignature = meter.TimeSignature('3/4')
bar1_right.append(note.Note('c4'))
right_hand.append(bar1_right)

bar1_left = stream.Measure()
bar1_left.clef = clef.BassClef()
bar1_left.timeSignature = meter.TimeSignature('3/4')
bar1_left.append(note.Rest(quarterLength=1))
left_hand.append(bar1_left)

bar2_right = stream.Measure()
tie_start = note.Note('c4')
tie_start.setTie(tie.Tie('start'))
bar2_right.append(tie_start)
tie_mid = note.Note('e4')
tie_mid.setTie(tie.Tie('continue'))
bar2_right.append(tie_mid)
tie_end = note.Note('g4')
tie_end.setTie(tie.Tie('stop'))
bar2_right.append(tie_end)
right_hand.append(bar2_right)

bar2_left = stream.Measure()
bar2_left.append(note.Rest(quarterLength=3))
left_hand.append(bar2_left)

bar3_right = stream.Measure()
bar3_right.append(note.Note('g4', quarterLength=2))
bar3_right.append(chord.Chord([
    note.Note('e5'),
    note.Note('g5'),
    ]))
right_hand.append(bar3_right)

bar3_left = stream.Measure()
bar3_left.append(note.Note('c3'))
bar3_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar3_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar3_left)

bar4_right = stream.Measure()
bar4_right.append(chord.Chord([
    note.Note('e5', quarterLength=2),
    note.Note('g5', quarterLength=2),
    ]))
bar4_right.append(chord.Chord([
    note.Note('c5'),
    note.Note('e5'),
    ]))
right_hand.append(bar4_right)

bar4_left = stream.Measure()
bar4_left.append(note.Note('c3'))
bar4_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar4_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar4_left)

bar5_right = stream.Measure()
bar5_right.append(chord.Chord([
    note.Note('c5', quarterLength=2),
    note.Note('e5', quarterLength=2),
    ]))
bar5_right.append(note.Note('c4'))
right_hand.append(bar5_right)

bar5_left = stream.Measure()
bar5_left.append(note.Note('c3'))
bar5_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar5_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar5_left)

bar6_right = stream.Measure()
bar6_right.append(note.Note('c4'))
bar6_right.append(note.Note('e4'))
bar6_right.append(note.Note('g4'))
right_hand.append(bar6_right)

bar6_left = stream.Measure()
bar6_left.append(note.Note('c3'))
bar6_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar6_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar6_left)

bar7_right = stream.Measure()
bar7_right.append(note.Note('g4', quarterLength=2))
bar7_right.append(chord.Chord([
    note.Note('f5'),
    note.Note('g5'),
    ]))
right_hand.append(bar7_right)

bar7_left = stream.Measure()
bar7_left.append(note.Note('d3'))
bar7_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar7_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar7_left)

bar8_right = stream.Measure()
bar8_right.append(chord.Chord([
    note.Note('f5', quarterLength=2),
    note.Note('g5', quarterLength=2),
    ]))
bar8_right.append(chord.Chord([
    note.Note('b4'),
    note.Note('f5'),
    ]))
right_hand.append(bar8_right)

bar8_left = stream.Measure()
bar8_left.append(note.Note('d3'))
bar8_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar8_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar8_left)

bar9_right = stream.Measure()
bar9_right.append(chord.Chord([
    note.Note('b4', quarterLength=2),
    note.Note('f5', quarterLength=2),
    ]))
bar9_right.append(note.Note('b3'))
right_hand.append(bar9_right)

bar9_left = stream.Measure()
bar9_left.append(note.Note('d3'))
bar9_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar9_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar9_left)

bar10_right = stream.Measure()
bar10_right.append(note.Note('b3'))
bar10_right.append(note.Note('d4'))
bar10_right.append(note.Note('a4'))
right_hand.append(bar10_right)

bar10_left = stream.Measure()
bar10_left.append(note.Note('d3'))
bar10_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar10_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar10_left)

bar11_right = stream.Measure()
bar11_right.append(note.Note('a4', quarterLength=2))
bar11_right.append(chord.Chord([
    note.Note('f5'),
    note.Note('a5'),
    ]))
right_hand.append(bar11_right)

bar11_left = stream.Measure()
bar11_left.append(note.Note('d3'))
bar11_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar11_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar11_left)

bar12_right = stream.Measure()
bar12_right.append(chord.Chord([
    note.Note('f5', quarterLength=2),
    note.Note('a5', quarterLength=2),
    ]))
bar12_right.append(chord.Chord([
    note.Note('b4'),
    note.Note('f5'),
    ]))
right_hand.append(bar12_right)

bar12_left = stream.Measure()
bar12_left.append(note.Note('d3'))
bar12_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar12_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar12_left)

bar13_right = stream.Measure()
bar13_right.append(chord.Chord([
    note.Note('b4', quarterLength=2),
    note.Note('f5', quarterLength=2),
    ]))
bar13_right.append(note.Note('b3'))
right_hand.append(bar13_right)

bar13_left = stream.Measure()
bar13_left.append(note.Note('d3'))
bar13_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar13_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar13_left)

bar14_right = stream.Measure()
bar14_right.append(note.Note('b3'))
bar14_right.append(note.Note('d4'))
bar14_right.append(note.Note('a4'))
right_hand.append(bar14_right)

bar14_left = stream.Measure()
bar14_left.append(note.Note('d3'))
bar14_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar14_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar14_left)

bar15_right = stream.Measure()
bar15_right.append(note.Note('a4', quarterLength=2))
bar15_right.append(chord.Chord([
    note.Note('e5'),
    note.Note('a5'),
    ]))
right_hand.append(bar15_right)

bar15_left = stream.Measure()
bar15_left.append(note.Note('c3'))
bar15_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar15_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar15_left)

bar16_right = stream.Measure()
bar16_right.append(chord.Chord([
    note.Note('e5', quarterLength=2),
    note.Note('a5', quarterLength=2),
    ]))
bar16_right.append(chord.Chord([
    note.Note('c5'),
    note.Note('e5'),
    ]))
right_hand.append(bar16_right)

bar16_left = stream.Measure()
bar16_left.append(note.Note('c3'))
bar16_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar16_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar16_left)

bar17_right = stream.Measure()
bar17_right.append(chord.Chord([
    note.Note('c5', quarterLength=2),
    note.Note('e5', quarterLength=2),
    ]))
bar17_right.append(note.Note('c4'))
right_hand.append(bar17_right)

bar17_left = stream.Measure()
bar17_left.append(note.Note('c3'))
bar17_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar17_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar17_left)

bar18_right = stream.Measure()
bar18_right.append(note.Note('c4'))
bar18_right.append(note.Note('e4'))
bar18_right.append(note.Note('g4'))
right_hand.append(bar18_right)

bar18_left = stream.Measure()
bar18_left.append(note.Note('c3'))
bar18_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar18_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar18_left)

bar19_right = stream.Measure()
bar19_right.append(note.Note('c5', quarterLength=2))
bar19_right.append(chord.Chord([
    note.Note('g5'),
    note.Note('c6'),
    ]))
right_hand.append(bar19_right)

bar19_left = stream.Measure()
bar19_left.append(note.Note('e3'))
bar19_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
bar19_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
left_hand.append(bar19_left)

bar20_right = stream.Measure()
bar20_right.append(chord.Chord([
    note.Note('g5', quarterLength=2),
    note.Note('c6', quarterLength=2),
    ]))
bar20_right.append(chord.Chord([
    note.Note('e5'),
    note.Note('g5'),
    ]))
right_hand.append(bar20_right)

bar20_left = stream.Measure()
bar20_left.append(note.Note('e3'))
bar20_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
bar20_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
left_hand.append(bar20_left)

bar21_right = stream.Measure()
bar21_right.append(chord.Chord([
    note.Note('e5', quarterLength=2),
    note.Note('g5', quarterLength=2),
    ]))
bar21_right.append(note.Note('c4'))
right_hand.append(bar21_right)

bar21_left = stream.Measure()
bar21_left.append(note.Note('e3'))
bar21_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
bar21_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
left_hand.append(bar21_left)

bar22_right = stream.Measure()
bar22_right.append(note.Note('c4'))
bar22_right.append(note.Note('e4'))
bar22_right.append(note.Note('g4'))
right_hand.append(bar22_right)

bar22_left = stream.Measure()
bar22_left.append(note.Note('e3'))
bar22_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
bar22_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
left_hand.append(bar22_left)

bar23_right = stream.Measure()
bar23_right.append(note.Note('c5', quarterLength=2))
bar23_right.append(chord.Chord([
    note.Note('a5'),
    note.Note('c6'),
    ]))
right_hand.append(bar23_right)

bar23_left = stream.Measure()
bar23_left.append(note.Note('f3'))
bar23_left.append(chord.Chord([
    note.Note('a3'),
    note.Note('d4'),
    ]))
bar23_left.append(chord.Chord([
    note.Note('a3'),
    note.Note('d4'),
    ]))
left_hand.append(bar23_left)

bar24_right = stream.Measure()
bar24_right.append(chord.Chord([
    note.Note('a5', quarterLength=2),
    note.Note('c6', quarterLength=2),
    ]))
bar24_right.append(chord.Chord([
    note.Note('f5'),
    note.Note('a5'),
    ]))
right_hand.append(bar24_right)

bar24_left = stream.Measure()
bar24_left.append(note.Note('f3'))
bar24_left.append(chord.Chord([
    note.Note('a3'),
    note.Note('d4'),
    ]))
bar24_left.append(chord.Chord([
    note.Note('a3'),
    note.Note('d4'),
    ]))
left_hand.append(bar24_left)

bar25_right = stream.Measure()
bar25_right.append(chord.Chord([
    note.Note('f5', quarterLength=2),
    note.Note('a5', quarterLength=2),
    ]))
bar25_right.append(note.Note('d4'))
right_hand.append(bar25_right)

bar25_left = stream.Measure()
bar25_left.append(chord.Chord([
    note.Note('f3', quarterLength=3),
    note.Note('a3', quarterLength=3),
    note.Note('d4', quarterLength=3),
    ]))
left_hand.append(bar25_left)

bar26_right = stream.Measure()
bar26_right.append(note.Note('d4'))
bar26_right.append(note.Note('f4'))
bar26_right.append(note.Note('a4'))
right_hand.append(bar26_right)

bar26_left = stream.Measure()
bar26_left.append(note.Note('a3'))
bar26_left.append(note.Note('f3'))
bar26_left.append(note.Note('d3'))
left_hand.append(bar26_left)

bar27_right = stream.Measure()
bar27_right.append(note.Note('a4', quarterLength=3))
right_hand.append(bar27_right)

bar27_left = stream.Measure()
bar27_left.append(note.Note('d3'))
bar27_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar27_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar27_left)

bar28_right = stream.Measure()
bar28_right.append(note.Note('a4'))
bar28_right.append(note.Note('f4#'))
bar28_right.append(note.Note('g4'))
right_hand.append(bar28_right)

bar28_left = stream.Measure()
bar28_left.append(note.Note('b2'))
bar28_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
bar28_left.append(chord.Chord([
    note.Note('f3'),
    note.Note('g3'),
    ]))
left_hand.append(bar28_left)

bar29_right = stream.Measure()
bar29_right.append(note.Note('e5', quarterLength=3))
right_hand.append(bar29_right)

bar29_left = stream.Measure()
bar29_left.append(note.Note('c3'))
bar29_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar29_left.append(chord.Chord([
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar29_left)

bar30_right = stream.Measure()
bar30_right.append(note.Note('e5'))
bar30_right.append(note.Note('c5'))
bar30_right.append(note.Note('e4'))
right_hand.append(bar30_right)

bar30_left = stream.Measure()
bar30_left.append(note.Note('e3'))
bar30_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
bar30_left.append(chord.Chord([
    note.Note('g3'),
    note.Note('c4'),
    ]))
left_hand.append(bar30_left)

bar31_right = stream.Measure()
bar31_right.append(note.Note('e4', quarterLength=2))
bar31_right.append(note.Note('d4'))
right_hand.append(bar31_right)

bar31_left = stream.Measure()
bar31_left.append(chord.Chord([
    note.Note('f3', quarterLength=3),
    note.Note('a3', quarterLength=3),
    note.Note('c4', quarterLength=3),
    ]))
left_hand.append(bar31_left)

bar32_right = stream.Measure()
bar32_right.append(note.Note('a4', quarterLength=2))
bar32_right.append(note.Note('g4'))
right_hand.append(bar32_right)

bar32_left = stream.Measure()
bar32_left.append(chord.Chord([
    note.Note('d3', quarterLength=3),
    note.Note('g3', quarterLength=3),
    note.Note('b3', quarterLength=3),
    ]))
left_hand.append(bar32_left)

bar33_right = stream.Measure()
bar33_right.append(note.Note('c4', quarterLength=1.5))
bar33_right.append(note.Note('c5', quarterLength=0.5))
bar33_right.append(note.Note('c5'))
right_hand.append(bar33_right)

bar33_left = stream.Measure()
bar33_left.append(chord.Chord([
    note.Note('c3', quarterLength=2),
    note.Note('e3', quarterLength=2),
    note.Note('g3', quarterLength=2),
    ]))
bar33_left.append(chord.Chord([
    note.Note('c3'),
    note.Note('e3'),
    note.Note('g3'),
    ]))
left_hand.append(bar33_left)

bar34_right = stream.Measure()
bar34_right.append(note.Note('c5'))
bar34_right.append(note.Rest(quarterLength=1))
right_hand.append(bar34_right)

bar34_left = stream.Measure()
bar34_left.append(chord.Chord([
    note.Note('c3'),
    note.Note('e3'),
    note.Note('g3'),
    ]))
bar34_left.append(note.Rest(quarterLength=1))
left_hand.append(bar34_left)

tune = stream.Score()
tune.insert(0, right_hand)
tune.insert(0, left_hand)

# Add a title
tune.metadata = metadata.Metadata(title='Python TTTGLS: Lesson 3 part 1')

##########################################################################
#                        LESSON 3 (PART 1)ENDS HERE                              #
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
