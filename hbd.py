import winsound as ws
import time
lst = """a1 a1 b1 - a1 - d1 - c#1 - - - -
a1 a1 b1 - a1 - e1 - d1 - - - -
a1 a1 b1 - f#1 - d1 - c#1 - b1 - - -
a1 a1 f#1 - d1 - e1 - d1
"""

##lst = """D#1 F1 F1 F1 F1 D#1 F1 D#1 C#1
##D#1 F1 F1 F1 D#1 F1 D#1 C#1
##C#1 A#1 C#1 C#1 C#1 D#1  D#1 F1  F#1
##F1   D#1  D#1  D#1 D#1 - - D#2 D#2 F2 F2 D#2 D#2 F2 D#2 C2
##D#2 D#2 F2 F2 F2 D#2 D#2 F2 D#2 C#2
##A#2 A#2 C#2 C#2 D#2 D#2 D#2 F2 F#2
##F2 D#2 D#2 D#2 D#2"""


lst = lst.split()
def play(note):
    ws.PlaySound(r"%s.wav"%note, ws.SND_ASYNC)

for i in lst:
    if i is not "-":
        time.sleep(0.16)
        play(i)
        
    else :
        time.sleep(0.16)
    print(i)
