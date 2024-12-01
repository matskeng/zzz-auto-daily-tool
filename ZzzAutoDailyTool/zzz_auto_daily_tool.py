from .lib import control_game
from datetime import datetime
import logging
from time import sleep

# デバッグ用定数(Falseにした項目を実行しない)
DO_START_GAME = False               # ゲームを起動する
DO_GET_EVENT_LOGIN_REWARDS = False  # イベントのログイン報酬を受け取る
DO_GET_INTERNOT_REWARDS = False     # インターノット会員報酬を受け取る
DO_DRINK_COFFEE = False             # コーヒーを飲む
DO_SCRATCH = False                  # スクラッチを行う
DO_BUSINESS_VIDEO_STORE = False     # ビデオ屋を営業する
DO_GET_ACTIVITY_REWARDS = False     # 活躍度報酬を受け取る
DO_CONSUME_BATTERY = True          # バッテリーを消化する

# ツールのメイン処理
def main():
    # ロガーを設定
    log_filename = "log\\" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
    logging.basicConfig(
        level=logging.DEBUG,                                # ログレベルを設定
        format='%(asctime)s - %(levelname)s - %(message)s', # フォーマットを指定
        filename=log_filename,                              # ログファイル名を指定
        filemode='w',                                       # ファイルモード（'a' は追記、'w' は上書き）
        encoding='shift_jis'                                # ファイルのエンコーディングを指定
    )
    
    # デバッグ用(5秒待つ)
    sleep(5)
    
    # ゲームを起動する
    if DO_START_GAME:
        control_game.start_game()
    
    # イベントのログイン報酬を受け取る
    if DO_GET_EVENT_LOGIN_REWARDS:
        control_game.get_event_login_rewards()
    
    # インターノット会員報酬を受け取る
    if DO_GET_INTERNOT_REWARDS:
        control_game.get_internot_rewards()
    
    # コーヒーを飲む
    if DO_DRINK_COFFEE:
        control_game.drink_coffee()
    
    # スクラッチを行う
    if DO_SCRATCH:
        control_game.scratch()
    
    # ビデオ屋を営業する
    if DO_BUSINESS_VIDEO_STORE:
        control_game.business_video_store()
    
    # 活躍度報酬を受け取る
    if DO_GET_ACTIVITY_REWARDS:
        control_game.get_activity_rewards()
    
    # バッテリーを消化する
    if DO_CONSUME_BATTERY:
        control_game.consume_battery()
    

if __name__ == "__main__":
    main()
