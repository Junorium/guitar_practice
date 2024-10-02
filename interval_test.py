import numpy as np
scales_sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def main():
  while True:
    game_mode = input('Type of Game Mode: for scale, Random or Given?')
    if game_mode.lower().strip() == 'random':
      scale = scales_sharp[np.random.randint(0, 12)]
      play(scale)
    elif game_mode.lower().strip() == 'given':
      scale = input('Scale?')
      try:
        play(scales_sharp[])
      except:
        play(scales_flat[])
