# VISION.md

# Project Name (仮)
VTuber AI Studio

# 目的
AIを使って、VTuber・3DCGキャラクターの動画制作を簡単にする。

特に以下を解決する：

- 画像から3Dキャラを生成
- 音声から自然な口パク・表情生成
- 動画制作の自動化・効率化

最終的には：

「誰でも、自分のキャラクターで動画を作れる世界」

を実現する。

# なぜこれを作るのか

理由：

- VTuber文化が好き
- 3DCG技術に興味がある
- AIと組み合わせることで大きな可能性がある
- 自分自身が使いたい

# 最初のスコープ（超小さく）

最初の目標：

音声ファイルを入力すると、
口パク用のmouth open/close値を出力するツール

input:
audio.wav

output:
[
  {time: 0.00, mouth: 0.1},
  {time: 0.03, mouth: 0.5},
  ...
]

# 技術候補

backend:
- Python
- FastAPI

frontend:
- Vue

AI:
- wav2vec
- existing lipsync models

# ルール

小さく作る
毎日少しずつ進める
完璧を目指さない

## Next step
- 空のbackend/main.pyを作る

# 作成日

2026-02-18
