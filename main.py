from replit import audio
import os,time

def play():
  source=audio.play_file('audio.wav')
  source.paused=False

  while True:
    song=int(input("Press 2 to stop and go to main menu"))
    if song==2:
      source.paused= True
      return
    else:
      continue
while True:
  os.system("clear")
  time.sleep(1)
  print("press 1 to Play")
  time.sleep(1)
  print("press 2 to exit")
  time.sleep(1)
  print("press anything else to go back to menu.")
  playuserinput=int(input())
  if playuserinput==1:
    print("Playing song")
    play()
  elif playuserinput==2:
    exit()
  else:
    continue