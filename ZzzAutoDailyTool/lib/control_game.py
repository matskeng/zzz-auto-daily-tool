import keyboard
import time
import pyautogui
import json
from logging import getLogger
from . import screen_recog as sr

logger = getLogger(__name__)
user_setting_path = "config/user_setting.json"

# コーヒーを飲む関数
def drink_coffee():
    logger.info("コーヒーを飲みます")
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # コーヒーを飲むパネルが表示されるか確認
    top_left, bottom_right = sr.rcg_and_return_coords_while_loop("task_drink_coffee.png", 2)
    
    # コーヒーを飲むパネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("コーヒーを飲むパネルが表示されませんでした")
        
        # F2キーを押す
        keyboard.press('f2')
        time.sleep(0.1)
        keyboard.release('f2')
        
        # 1秒待つ
        time.sleep(1)
        
        return
    
    # パネル内のgoボタンをクリック
    sr.rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 注文ボタンをクリック
    sr.rcg_and_click("button_order.png")
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 3秒待つ
    time.sleep(3)


# スクラッチを行う関数
def scratch():
    logger.info("スクラッチを行います")
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # スクラッチパネルが表示されるか確認
    top_left, bottom_right = sr.rcg_and_return_coords_while_loop("task_scratch.png", 2)
    
    # スクラッチパネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("スクラッチパネルが表示されませんでした")
        
        # F2キーを押す
        keyboard.press('f2')
        time.sleep(0.1)
        keyboard.release('f2')
        
        # 1秒待つ
        time.sleep(1)
        
        return
    
    # パネル内のgoボタンをクリック
    sr.rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # スクラッチカードをクリック
    sr.rcg_and_click("scratch_card.png")
    
    # スクラッチを行う
    sr.rcg_and_scratch("scratch_area.png")
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 戻るボタンをクリック
    sr.rcg_and_click("button_return.png")
    
    # 1秒待つ
    time.sleep(1)

    # 戻るボタンをクリック
    sr.rcg_and_click("button_return.png")
    
    # 3秒待つ
    time.sleep(3)


# ビデオ屋を営業する関数
def business_video_store():
    logger.info("ビデオ屋を営業します")
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # ビデオ屋パネルが表示されるか確認
    top_left, bottom_right = sr.rcg_and_return_coords_while_loop("task_business_video_store.png", 2)
    
    # ビデオ屋パネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("ビデオ屋パネルが表示されませんでした")
        
        # F2キーを押す
        keyboard.press('f2')
        time.sleep(0.1)
        keyboard.release('f2')
        
        # 1秒待つ
        time.sleep(1)
        
        return
    
    # パネル内のgoボタンをクリック
    sr.rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 閉じるボタンをクリック
    res = sr.rcg_and_click_while_loop("button_close.png", 5)
    if res is False:
        logger.info("ビデオ屋の報酬は受け取り済みでした")
    
    # 販促担当設定ボタンをクリック
    res = sr.rcg_and_click_while_loop("promotion_staff.png", 5)
    if res is False:
        logger.info("ビデオ屋の販促担当設定ボタンが見つかりませんでした")
        return
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 品出しボタンをクリック
    sr.rcg_and_click("display_videos.png")
    
    # おまかせボタンをクリック
    sr.rcg_and_click("button_auto.png")
    
    # 営業開始ボタンをクリック
    sr.rcg_and_click("button_start_business.png")
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 1秒待つ
    time.sleep(1)
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 戻るボタンをクリック
    sr.rcg_and_click("button_return.png")
    
    # 3秒待つ
    time.sleep(3)


# 活躍度報酬を受け取る関数
def get_activity_rewards():
    logger.info("活躍度報酬を受け取ります")
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # 活躍度ゲージをクリックする
    # 本日の最大活躍度パネルの座標を取得
    top_left, bottom_right = sr.rcg_and_return_coords_while_loop("panel_max_activity.png", 2)
    # 本日の最大活躍度パネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("本日の最大活躍度パネルが表示されませんでした")
    else:
        # 右辺の中点の座標を計算
        mid_x = bottom_right[0]
        mid_y = (top_left[1] + bottom_right[1]) // 2
        # 右辺の中点から右に10ピクセル移動した座標をクリック
        pyautogui.click(mid_x + 10, mid_y)
        
        # OKボタンをクリック
        res = sr.rcg_and_click_while_loop("button_ok.png", 2)
        if res is False:
            logger.info("活躍度報酬を受け取れませんでした")
        
        # 1秒待つ
        time.sleep(1)
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # 3秒待つ
    time.sleep(3)


# バッテリーを消化する関数
def consume_battery():
    logger.info("バッテリーを消化します")
    
    # user_config.jsonを読み込む
    with open(user_setting_path, "r", encoding="utf-8") as f:
        setting = json.load(f)
    
    # バッテリーを消化する種目の設定
    category1 = setting["category1"]
    category2 = setting["category2"]
    category3 = setting["category3"]
    
    # F2キーを押す
    keyboard.press('f2')
    time.sleep(0.1)
    keyboard.release('f2')
    
    # 「現在のバッテリー」の座標を取得
    top_left, bottom_right = sr.rcg_and_return_coords_while_loop("current_battery.png", 2)
    # 「現在のバッテリー」が表示されなかった場合は関数を抜ける
    if top_left is None:
        logger.info("現在のバッテリー値が表示されませんでした")
        return
    
    # 現在のバッテリー値を取得
    current_battery = sr.get_battery_value(top_left, bottom_right)
    logger.info(f"現在のバッテリー値: {current_battery}")
    
    # カテゴリ1の選択
    if category1 != "mock_practice":
        sr.rcg_and_click(f"category1_{category1}.png")
     
    
    # # 基本素材でバッテリーを消化する
    # # 基本素材パネルの座標を取得
    # top_left, bottom_right = sr.rcg_and_return_coords_while_loop("panel_basic_material.png", 2)
    # if top_left is None:
    #     logger.info("基本素材パネルが見つかりませんでした")
    #     return

    # パネル内のgoボタンをクリック
    sr.rcg_and_click_in_area("button_go_in_panel.png", top_left, bottom_right)
    
    # OKボタンをクリック
    sr.rcg_and_click("button_ok.png")
    
    # 次へボタンをクリック
    sr.rcg_and_click("button_next.png")
    
    # 出撃ボタンをクリック
    sr.rcg_and_click("button_sortie.png")
    
    # キャラ切り替えボタンが表示されるまで待つ
    sr.wait_until_img_displayed("button_change_chara.png")
    
    # 完了ボタンが表示されるまでクリックし続ける
    sr.click_until_img_displayed("button_complete.png")
    
    # 完了ボタンをクリック
    sr.rcg_and_click("button_complete.png")