from .lib import control_game
from datetime import datetime
import logging

# ツールのメイン処理
def main():
    # ロガーを設定
    log_filename = "log\\" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
    logging.basicConfig(filename=log_filename, level=logging.INFO)
    
    # # ゲームを起動する
    # control_game.start_game()
    
    # インターノット会員報酬を受け取る
    control_game.get_internot_rewards()
    
    # コーヒーを飲む
    control_game.drink_coffee()
    
    # スクラッチを行う
    control_game.scratch()
    
    # ビデオ屋を営業する
    control_game.business_video_store()    

if __name__ == "__main__":
    main()
