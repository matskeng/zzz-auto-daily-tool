import keyboard
import time
from logging import getLogger
from .screen_recog import rcg_and_click
from .screen_recog import rcg_and_click_while_loop
from .screen_recog import rcg_and_return_coords_while_loop
from .screen_recog import rcg_and_click_in_area
from .screen_recog import rcg_and_scratch

logger = getLogger(__name__)

# HoYoPlayランチャーからゲームを起動する関数
def start_game():
    logger.info("ゲームを起動します")
    
    # ZZZのアイコンをクリック
    rcg_and_click("launcher_zzz.png")
    
    # ゲーム開始のボタンをクリック
    rcg_and_click("launcher_start_game.png")
    
    # ゲーム内でゲーム開始が表示されたらクリック
    rcg_and_click("zzz_start_game.png")
    
    # ゲーム内でコンフィグデータロード中が表示されたらクリック
    # (クリックする必要はないが、画面が切り替わるのを待つために挟む)
    rcg_and_click("loading_config_data.png")
    
    # ゲーム内でゲーム開始が表示されたらクリック(2回目)
    rcg_and_click("zzz_start_game.png")

# インターノット会員報酬を受け取る関数
def get_internot_rewards():
    logger.info("インターノット会員報酬を受け取ります")
    
    # インターノット会員報酬を受け取るボタンをクリック
    rcg_and_click_while_loop("internot_reward.png", 10)
    
    # 1秒待つ
    time.sleep(1)

# コーヒーを飲む関数
def drink_coffee():
    logger.info("コーヒーを飲みます")
    
    # F2キーを押す
    keyboard.press('f2')
    
    # コーヒーを飲むパネルが表示されるか確認
    top_left, bottom_right = rcg_and_return_coords_while_loop("task_drink_coffee.png", 3)
    
    # コーヒーを飲むパネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("コーヒーを飲むパネルが表示されませんでした")
        return
    
    # パネル内のgoボタンをクリック
    rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 注文ボタンをクリック
    rcg_and_click("button_order.png")
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 1秒待つ
    time.sleep(1)

# スクラッチを行う関数
def scratch():
    logger.info("スクラッチを行います")
    
    # F2キーを押す
    keyboard.press('f2')
    
    # スクラッチパネルが表示されるか確認
    top_left, bottom_right = rcg_and_return_coords_while_loop("task_scratch.png", 3)
    
    # スクラッチパネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("スクラッチパネルが表示されませんでした")
        return
    
    # パネル内のgoボタンをクリック
    rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # スクラッチカードをクリック
    rcg_and_click("scratch_card.png")
    
    # スクラッチを行う
    rcg_and_scratch("scratch_area.png")
    
    # 1秒待つ
    time.sleep(1)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 1秒待つ
    time.sleep(1)
    
    # 戻るボタンをクリック
    rcg_and_click("button_return.png")
    
    # 1秒待つ
    time.sleep(1)

    # 戻るボタンをクリック
    rcg_and_click("button_return.png")
    
    # 1秒待つ
    time.sleep(1)

# ビデオ屋を営業する関数
def business_video_store():
    logger.info("ビデオ屋を営業します")
    
    # 5秒待つ
    time.sleep(5)
    
    # F2キーを押す
    keyboard.press('f2')
    
    # ビデオ屋パネルが表示されるか確認
    top_left, bottom_right = rcg_and_return_coords_while_loop("task_business_video_store.png", 3)
    
    # ビデオ屋パネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("ビデオ屋パネルが表示されませんでした")
        return
    
    # パネル内のgoボタンをクリック
    rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 販促担当設定ボタンをクリック
    rcg_and_click("promotion_staff.png")
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 品出しボタンをクリック
    rcg_and_click("display_videos.png")
    
    # おまかせボタンをクリック
    rcg_and_click("button_auto.png")
    
    # 営業開始ボタンをクリック
    rcg_and_click("button_start_business.png")
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 1秒待つ
    time.sleep(1)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 1秒待つ
    time.sleep(1)
    
    # 戻るボタンをクリック
    rcg_and_click("button_return.png")
    
    # 1秒待つ
    time.sleep(1)
