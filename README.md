# ゼンレスゾーンゼロ自動日課ツール

## 概要

このツールは、**ゼンレスゾーンゼロ (Zenless Zone Zero)** の日課を自動化するPythonツールです。  
mihoyoランチャーからゲームを起動し、以下のタスクを自動的に実行します：

1. スタミナの消化  
2. デイリー任務の遂行  
3. 報酬の受け取り  

ゲームを効率的にプレイしたい方向けに設計されています。

---

## 特徴

- 完全自動化：一連の操作を完全自動化し、時間を節約します。
- ログ機能：実行結果をログに記録します。

---

## 必要環境

- OS: Windows 10 以上  
- Python: 3.10 以上  
- 必要なライブラリ:
  - pyautogui ^0.9.54
  - opencv-python ^4.7.0
  - Pillow ^9.5.0
  - numpy = "^1.24.0"
  - keyboard = "^0.13.5"
  - random = "^1.2"
  - pytesseract = "^0.3.8"
---

## インストール

1. 本リポジトリをクローンまたはダウンロードします。  
   ```
   git clone https://github.com/matskeng/zzz-auto-daily-tool
   cd zzz-auto-daily-tool
   ```

2. Tesseractをインストールします。
   下記リンクをクリックして、インストーラを実行します。
   https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe

3. 必要なライブラリをインストールします。  
   ```
   pip install -r requirements.txt
   ```
   
   または Poetry を使用する場合：
   ```
   poetry install
   ```

---

## 使い方

1. HoYoPlayランチャーを起動します。

2. ツールを起動します。  
   ```
   python -m ZzzAutoDailyTool
   ```

3. ゲームが起動され、日課が自動的に実行されます。

4. ログを確認する場合、`logs`フォルダ内のファイルを参照してください。

---

## 注意事項

1. **利用規約の遵守**  
   本ツールを使用する際は、ゼンレスゾーンゼロおよびmihoyoの利用規約を必ず確認してください。アカウントが停止されるリスクがあるため、自己責任でご利用ください。

2. **非公式ツール**  
   本ツールはmihoyo公式のツールではありません。

---s

## ライセンス

本プロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルをご覧ください。

---

## 貢献

バグ報告や機能リクエストは、GitHubの[Issue](https://github.com/matskeng/zzz-auto-daily-tool/issues)をご利用ください。
