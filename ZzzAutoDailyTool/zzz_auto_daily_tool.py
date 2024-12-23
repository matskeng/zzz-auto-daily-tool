from ZzzAutoDailyTool.lib import logger
from ZzzAutoDailyTool.lib import start

# デバッグ用定数(Falseにした項目を実行しない)
DO_START_GAME = True               # ゲームを起動する
DO_DRINK_COFFEE = True             # コーヒーを飲む
DO_SCRATCH = True                  # スクラッチを行う
DO_BUSINESS_VIDEO_STORE = True     # ビデオ屋を営業する
DO_GET_ACTIVITY_REWARDS = True     # 活躍度報酬を受け取る
DO_CONSUME_BATTERY = True          # バッテリーを消化する

# ツールのメイン処理
def main():
    # ロガーを設定
    logger.setting_logger()
    
    # ゲームを起動する
    if DO_START_GAME:
        start.start_game()
    
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
