import sys

import numpy as np

from rnnoisepy.rnnoise import RNNoise

rnnoise: RNNoise = RNNoise()

while buffer := sys.stdin.buffer.read(rnnoise.frame_size * 2):
    frame = np.frombuffer(buffer, dtype=np.int16)
    reducted_frame, voice_prob = rnnoise.process_frame(frame)
    print(f"Voice probability: {voice_prob:.3f}")
