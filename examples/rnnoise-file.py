import wave

import numpy as np
import numpy.typing as npt

from rnnoisepy.rnnoise import RNNoise

rnnoise: RNNoise = RNNoise()

with wave.open("output.wav", "wb") as output_wav:
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)
    output_wav.setframerate(48000)

    with wave.open("sample.wav", "rb") as wf:
        buffer: bytes
        while buffer := wf.readframes(rnnoise.frame_size):
            frame: npt.NDArray[np.int16] = np.frombuffer(buffer, dtype=np.int16)
            # フレームサイズが足りない場合はゼロパディング
            if frame.size < rnnoise.frame_size:
                frame = np.pad(
                    frame, (0, rnnoise.frame_size - frame.size), mode="constant"
                )
            denoised_frame, voice_prob = rnnoise.process_frame(frame)
            print(f"Voice probability: {voice_prob:.3f}")
            output_wav.writeframes(denoised_frame.tobytes())
