from .lib import logger, start, tasks, battery

# デバッグ用定数(Falseにした項目を実行しない)
DO_START_GAME = False               # ゲームを起動する
DO_TASKS = False                    # デイリータスクを実行する
DO_CONSUME_BATTERY = True          # バッテリーを消化する

# ツールのメイン処理
def main():
    # ロガーを設定
    logger.setting_logger()
    
    # ゲームを起動する
    if DO_START_GAME:
        start.start_game()
    
    # デイリータスクを消化する
    if DO_TASKS:
        tasks.do_daily_tasks()
    
    # バッテリーを消化する
    if DO_CONSUME_BATTERY:
       battery.use_battery()
