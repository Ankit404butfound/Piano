import winsound as ws
import time
import keyboard


def play(note):
    ws.PlaySound(r"%s.wav"%note, ws.SND_ASYNC)

notes1 = {"a" : "c1",
         "s" : "d1",
         "d" : "e1",
         "f" : "f1",
         "g" : "g1",
         "h" : "a1",
         "j" : "b1",
         "k" : "c2",
         "z" : "c#1",
         "x" : "d#1",
         "v" : "f#1",
         "b" : "g#1",
         "n" : "a#1"
         }
notes2 = {"a" : "c2",
         "s" : "d2",
         "d" : "e2",
         "f" : "f2",
         "g" : "g2",
         "h" : "a2",
         "j" : "b2",
         "k" : "c3",
         "z" : "c#2",
         "x" : "d#2",
         "v" : "f#2",
         "b" : "g#2",
         "n" : "a#2"
         }
note = notes1
while True:
    try:
        key = keyboard.read_key()
        if key == "right":
            note = notes2
            
        if key == "left":
            note = notes1
        
        tone = note[key]
        print(tone)
        play(tone)
    except Exception as e:
        print(e)
        pass
    time.sleep(0.2)

