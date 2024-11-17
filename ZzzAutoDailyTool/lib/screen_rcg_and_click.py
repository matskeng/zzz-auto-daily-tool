import cv2
import numpy as np
import pyautogui
import time

# 画面認識を行い、指定した画像ファイルに一致するボタンをクリックする
# img_file: 画像ファイル名
def screen_rcg_and_click(img_file: str):
    img_file_path = "assets/images/" + img_file
    
    # ボタンを認識するまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # ボタンの画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            raise FileNotFoundError(f"画像ファイルが読み込めません: {img_file_path}")
        
        # ボタンの画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:            
            # ボタンの中心座標を計算
            button_width = img.shape[1]
            button_height = img.shape[0]
            center_x = max_loc[0] + (button_width // 2)
            center_y = max_loc[1] + (button_height // 2)
            
            # マウスを移動してからクリック
            pyautogui.moveTo(center_x, center_y, duration=0.2)
            time.sleep(1)
            pyautogui.click()
            
            return
        
        # 1秒待つ
        time.sleep(1)

# 画面認識を行い、指定した画像ファイルに一致するボタンをクリックする
# 一定時間画像ファイルに一致するボタンが見つからない場合は関数を抜ける
# wait_loop: 関数が抜けるまでのループ回数
# img_file: 画像ファイル名
def screen_rcg_and_click(img_file: str, wait_loop: int):
    img_file_path = "assets/images/" + img_file
    loop_cnt = 0
    
    # ボタンを認識するまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # ボタンの画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            raise FileNotFoundError(f"画像ファイルが読み込めません: {img_file_path}")
        
        # ボタンの画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:            
            # ボタンの中心座標を計算
            button_width = img.shape[1]
            button_height = img.shape[0]
            center_x = max_loc[0] + (button_width // 2)
            center_y = max_loc[1] + (button_height // 2)
            
            # マウスを移動してからクリック
            pyautogui.moveTo(center_x, center_y, duration=0.2)
            time.sleep(1)
            pyautogui.click()
            
            return
        
        # 1秒待つ
        time.sleep(1)
        
        # ループ回数が指定回数に達したら関数を抜ける
        loop_cnt += 1
        if loop_cnt >= wait_loop:
            return