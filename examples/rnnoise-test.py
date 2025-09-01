import wave

import numpy as np
import numpy.typing as npt

from rnnoisepy.rnnoise import RNNoise

rnnoise: RNNoise = RNNoise()
print(f"RNNoise supported frame size: {rnnoise.frame_size}")

rng = np.random.default_rng()
source: npt.NDArray[np.int16] = np.empty((0), dtype=np.int16)
result: npt.NDArray[np.int16] = np.empty((0), dtype=np.int16)

# 480frameのノイズを1000回生成(10秒分)し
# フレームごとにノイズリダクション処理を行う
for count in range(1000):
    audio_data: npt.NDArray[np.int16] = rng.integers(
        -1000, 1000, size=480, dtype=np.int16
    )
    reducted_audio: npt.NDArray[np.int16]
    voice_probs: float
    reducted_audio, voice_probs = rnnoise.process_frame(audio_data)

    print(f"Average voice probability: {voice_probs}")
    source = np.concatenate((source, audio_data))
    result = np.concatenate((result, reducted_audio))

# ノイズリダクション前の音声を保存
with wave.open("output_source.wav", "wb") as output_wav:
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)
    output_wav.setframerate(48000)
    output_wav.writeframes(result.tobytes())

# ノイズリダクション後の音声を保存
with wave.open("output_reducted.wav", "wb") as output_wav:
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)
    output_wav.setframerate(48000)
    output_wav.writeframes(result.tobytes())
