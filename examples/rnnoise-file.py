import wave

import numpy as np
import numpy.typing as npt

from rnnoisepy import RNNoise

rnnoise: RNNoise = RNNoise()

with wave.open("output.wav", "wb") as output_wav:
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)
    output_wav.setframerate(48000)

    with wave.open("input.wav", "rb") as input_wav:
        buffer: bytes
        # RNNoiseでサポートされているフレーム数分だけファイルを読み込み、
        # NDArray形式に変換する。
        while buffer := input_wav.readframes(rnnoise.frame_size):
            frame: npt.NDArray[np.int16] = np.frombuffer(buffer, dtype=np.int16)
            # フレームサイズが足りない場合はゼロパディング
            if frame.size < rnnoise.frame_size:
                frame = np.pad(
                    frame, (0, rnnoise.frame_size - frame.size), mode="constant"
                )
            # リダクションしたフレームと音声っぽさの確率(0.0～1.0)を取得
            # 音声っぽさが高いと1.0に近づく。
            reducted_frame, voice_prob = rnnoise.process_frame(frame)
            print(f"Voice probability: {voice_prob:.3f}")
            output_wav.writeframes(reducted_frame.tobytes())
