import datetime
import logging

# ログを設定する関数
def setting_logger():
    # ロガーを設定
    log_filename = "log\\" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
    logging.basicConfig(
        level=logging.DEBUG,                                # ログレベルを設定
        format='%(asctime)s - %(levelname)s - %(message)s', # フォーマットを指定
        filename=log_filename,                              # ログファイル名を指定
        filemode='w',                                       # ファイルモード（'a' は追記、'w' は上書き）
        encoding='shift_jis'                                # ファイルのエンコーディングを指定
    )