# RNNoisePy

ノイズリダクション用ライブラリ[RNNoise](https://gitlab.xiph.org/xiph/rnnoise)を、
Pythonから簡単に使えるようにするためのシンプルなライブラリです。
ノイズリダクションに加え、音声フレームごとの音声っぽさを評価できます。


## インストール

ライブラリのインストールには[uv](https://github.com/astral-sh/uv)を用います。

```sh
$ git clone https://github.com/Sincromisor/RNNoisePy.git
$ cd RNNoisePy
$ uv sync
```

これに加え、`librnnoise.so`が必要です。
[RNNoiseのソースコード](https://gitlab.xiph.org/xiph/rnnoise)からビルドしてください。


## つかいかた
先ほどビルドしたライブラリのパスを環境変数で渡し、実行してください。

```sh
$ RNNOISE_LIB_PATH="/home/sincromisor/apps/lib/librnnoise.so" uv run examples/rnnoise-test.py
```

```python
import numpy as np
import numpy.typing as npt

from rnnoisepy.rnnoise import RNNoise

rnnoise: RNNoise = RNNoise()

# 1ch 48000Hz int16leのサンプルを480個持つ音声フレームを
# NDArray形式で用意
audio_data

# ノイズリダクションの音声フレームと音声っぽさを得る
reducted_audio: npt.NDArray[np.int16]
voice_probs: float
reducted_audio, voice_probs = rnnoise.process_frame(audio_data)
```

詳しくは [`examples/rnnoise-file.py`](examples/rnnoise-test.py)などを参照してください。


## 制約
* サンプリングレートは48000Hzで固定されています。
* フレームのサンプル数は480以上です。
  多くするとうまく機能しない場合がありますので、デフォルトの480のままがよさそうです。
* 人間の音声っぽさは0.0～1.0で評価されます。1.0に近いほど、人間の音声っぽいとされます。
