import logging
from . import util

logger = logging.getLogger(__name__)

# コーヒーを飲む
def _drink_coffee():
    logger.info("コーヒーを飲みます")
    
    # F2ボタンが表示されるまで待機
    util.wait_until_img_displayed("button_f2.png")
    # F2キーを押す
    util.press_key("f2")
    
    # コーヒーを飲むパネルの中のGOボタンをクリック
    util.click_img_in_img("task_drink_coffee.png", "button_go.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # 注文ボタンをクリック
    util.click_img("button_order.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")

# スクラッチを行う
def _scratch():
    logger.info("スクラッチを行います")
    
    # F2ボタンが表示されるまで待機
    util.wait_until_img_displayed("button_f2.png")
    # F2キーを押す
    util.press_key("f2")
    
    # スクラッチパネルの中のGOボタンをクリック
    util.click_img_in_img("task_scratch.png", "button_go.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # スクラッチカードをクリック
    util.click_img("scratch_card.png")
    # スクラッチを行う
    util.scratch_in_img("scratch_area.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # 戻るボタンをクリック
    util.click_img("button_return.png")
    # 戻るボタンをクリック
    util.click_img("button_return.png")

# ビデオ屋を営業する
def _operate_video_shop():
    logger.info("ビデオ屋を営業します")
    
    # F2ボタンが表示されるまで待機
    util.wait_until_img_displayed("button_f2.png")
    # F2キーを押す
    util.press_key("f2")
    
    # ビデオ屋のパネルの中のGOボタンをクリック
    util.click_img_in_img("task_video_shop.png", "button_go.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # 閉じるボタンをクリック
    util.click_img("button_close.png")
    # 販促担当設定ボタンをクリック
    util.click_img("promotion_staff.png")    
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # 品出しボタンをクリック
    util.click_img("display_videos.png")
    # おまかせボタンをクリック
    util.click_img("button_auto.png")
    # 営業開始ボタンをクリック
    util.click_img("button_start_business.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # OKボタンをクリック
    util.click_img("button_ok.png")
    # 戻るボタンをクリック
    util.click_img("button_return.png")

# 活躍度報酬を受け取る
def _receive_activity_reward():
    logger.info("活躍度報酬を受け取ります")
    
    # F2ボタンが表示されるまで待機
    util.wait_until_img_displayed("button_f2.png")
    # F2キーを押す
    util.press_key("f2")
    
    # 本日の最大活躍度パネルをクリック
    util.click_img("panel_max_activity.png")
    # F2キーを押す
    util.press_key("f2")

# デイリータスクを実行する
def do_daily_tasks():
    logger.info("デイリータスクを実行します")
    
    # コーヒーを飲む
    _drink_coffee()
    # スクラッチを行う
    _scratch()
    # ビデオ屋を営業する
    _operate_video_shop()
    # 活躍度報酬を受け取る
    _receive_activity_reward()