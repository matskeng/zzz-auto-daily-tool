import logging
import time
from . import util

logger = logging.getLogger(__name__)

# HoYoPlayランチャーからゲームを起動する
def _launch():
    logger.info("HoYoPlayランチャーからゲームを起動します")
    
    # ZZZのアイコンをクリック
    util.click_img("launcher_zzz.png")

# ゲームにログインする
def _login():
    logger.info("ゲームにログインします")
    
    # ゲーム開始のボタンをクリック
    util.click_img("launcher_start_game.png")
    # ゲーム内でゲーム開始が表示されたらクリック
    util.click_img("zzz_start_game.png")
    # ゲーム内でコンフィグデータロード中が表示されるまで待機
    util.wait_until_img_displayed("loading_config_data.png")
    # ゲーム内でゲーム開始が表示されたらクリック(2回目)
    util.click_img("zzz_start_game.png")

# ログインイベントの報酬を受け取る
def _get_login_event_rewards():
    logger.info("ログインイベントの報酬を受け取ります")
    
    # イベントのログイン報酬を受け取るボタンが表示されるか確認
    ret = util.which_img_displayed(["event_login_reward.png", "button_f2.png", "internot_reward.png"])
    if ret == 0:
        # イベントのログイン報酬を受け取るボタンをクリック
        util.click_img("event_login_reward.png")
        # OKボタンをクリック
        util.click_img("button_ok.png")
        # 戻るボタンをクリック
        util.click_img("button_return.png")
        time.sleep(0.2)
    else:
        logger.info("ログインイベント期間外のようです")

# インターノット会員報酬を受け取る
def _get_internot_rewards():
    logger.info("インターノット会員報酬を受け取ります")
    
    # インターノット会員報酬を受け取るボタンが表示されるか確認
    ret = util.which_img_displayed(["internot_reward.png", "button_f2.png"])
    if ret == 0:
        # インターノット会員報酬を受け取るボタンをクリック
        util.click_img("internot_reward.png")
    else:
        logger.info("インターノット会員ではないようです")

# ゲームを開始する
def start_game():
    logger.info("ゲームを開始します")
    
    # HoYoPlayランチャーからゲームを起動する
    _launch()
    # ゲームにログインする
    _login()
    # ログインイベントの報酬を受け取る
    _get_login_event_rewards()
    # インターノット会員報酬を受け取る
    _get_internot_rewards()
    
    logger.info("ゲームの起動が完了しました")
