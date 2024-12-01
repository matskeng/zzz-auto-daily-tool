import cv2
import numpy as np
import pyautogui
import time
import random
from logging import getLogger
import pytesseract
import keyboard

logger = getLogger(__name__)

# 画面認識を行い、指定した画像ファイルに一致するボタンをクリックする
# img_file: 画像ファイル名
def rcg_and_click(img_file: str):
    logger.info(f"{img_file}をクリックします")
    
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
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
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
# img_file: 画像ファイル名
# wait_loop: 関数が抜けるまでのループ回数
# 戻り値: True(ボタンをクリックした場合)、False(ボタンが見つからなかった場合)
def rcg_and_click_while_loop(img_file: str, wait_loop: int):
    logger.info(f"{img_file}をクリックします")
    
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
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
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
            return True
            
        else:
            logger.info(f"{img_file}が見つかりませんでした")
        
        # 1秒待つ
        time.sleep(1)
        
        # ループ回数が指定回数に達したら関数を抜ける
        loop_cnt += 1
        if loop_cnt >= wait_loop:
            return False

# 画面認識を行い、指定した画像ファイルに一致する範囲の座標を返す
# 一定時間画像ファイルに一致するボタンが見つからない場合は関数を抜ける
# img_file: 画像ファイル名
# wait_loop: 関数が抜けるまでのループ回数
def rcg_and_return_coords_while_loop(img_file: str, wait_loop: int):
    logger.info(f"{img_file}の座標を取得します")        
    
    img_file_path = "assets/images/" + img_file
    loop = 0
    
    # ボタンを認識するまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # ボタンの画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
        # ボタンの画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.95)以上かどうかを確認する
        logger.debug(f"max_val: {max_val}")
        if max_val >= 0.95:            
            # ボタンの範囲の座標を返す
            button_width = img.shape[1]
            button_height = img.shape[0]
            top_left = max_loc
            bottom_right = (top_left[0] + button_width, top_left[1] + button_height)
            return top_left, bottom_right
        
        # 1秒待つ
        time.sleep(1)
        
        # ループ回数が指定回数に達したら関数を抜ける
        loop += 1
        if loop >= wait_loop:
            return None, None

# 指定された範囲内で画面認識を行い、指定した画像ファイルに一致するボタンをクリックする
# img_file: 画像ファイル名
# top_left: 調査する範囲の左上座標
# bottom_right: 調査する範囲の右下座標
def rcg_and_click_in_area(img_file: str, top_left: tuple, bottom_right: tuple):
    logger.info(f"{img_file}をクリックします")
    
    img_file_path = "assets/images/" + img_file
    
    # ボタンを認識するまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # 調査する範囲の画像を切り出す
        area = screenshot_bgr[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        
        # ボタンの画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
        # ボタンの画像を調査する範囲の画像にマッチングさせる
        res = cv2.matchTemplate(area, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:            
            # ボタンの中心座標を計算
            button_width = img.shape[1]
            button_height = img.shape[0]
            center_x = top_left[0] + max_loc[0] + (button_width // 2)
            center_y = top_left[1] + max_loc[1] + (button_height // 2)
            
            # マウスを移動してからクリック
            pyautogui.moveTo(center_x, center_y, duration=0.2)
            time.sleep(1)
            pyautogui.click()
            
            return
        
        # 1秒待つ
        time.sleep(1)

# 指定した範囲内をスクラッチする関数
# img_file: 画像ファイル名
def rcg_and_scratch(img_file: str):
    logger.info(f"{img_file}をスクラッチします")
    
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
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
        # ボタンの画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:            
            # ボタンの四隅の座標を求める
            button_width = img.shape[1]
            button_height = img.shape[0]
            top_left = max_loc
            top_right = (top_left[0] + button_width, top_left[1])
            mid_left = (top_left[0], top_left[1] + (button_height // 2))
            mid_right = (top_left[0] + button_width, top_left[1] + (button_height // 2))
            bottom_left = (top_left[0], top_left[1] + button_height)
            bottom_right = (top_left[0] + button_width, top_left[1] + button_height)

            # スクラッチを行う
            pyautogui.moveTo(top_left[0], top_left[1], duration=0.2)
            time.sleep(1)
            # クリックしたままでマウスを移動させる
            # 移動時間は乱数で設定
            pyautogui.dragTo(top_right[0], top_right[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(mid_left[0], mid_left[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(mid_right[0], mid_right[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(bottom_left[0], bottom_left[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(bottom_right[0], bottom_right[1], random.uniform(0.2, 0.5))
            
            return
        
        # 1秒待つ
        time.sleep(1)

# バッテリー値を取得する関数
# top_left: 「現在のバッテリー」の左上座標
# bottom_right: 「現在のバッテリー」の右下座標
def get_battery_value(top_left, bottom_right):
    logger.info("バッテリー値を取得します")        
    
    # スクリーンショットを取得する
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    # 現在のバッテリー値が表示されている範囲の画像を切り出す
    area = screenshot_bgr[top_left[1]:bottom_right[1], bottom_right[0]:bottom_right[0]+65]
    
    # 切り出した画像を保存(デバッグ用)
    cv2.imwrite("tmp\\current_battery_area.png", area)
    
    # areaをグレースケールに変換
    area_gray = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
    
    # pytesseractで数字を認識
    recognized_text = pytesseract.image_to_string(area_gray, config='--psm 6')
    
    # 認識されたテキストを数値に変換
    try:
        battery_value = int(recognized_text.strip())
    except ValueError:
        battery_value = None
    
    return battery_value  

# 画像が表示されるまで待機する関数
# img_file: 画像ファイル名
def wait_until_img_displayed(img_file: str):
    logger.info(f"{img_file}が表示されるまで待機します")
    
    img_file_path = "assets/images/" + img_file
    
    # 画像が表示されるまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # 画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
        # 画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:
            return
        
        # 1秒待つ
        time.sleep(1)


# 画像が表示されるまで任意の場所をクリックし続ける関数
# img_file: 画像ファイル名
def click_until_img_displayed(img_file: str):
    logger.info(f"{img_file}が表示されるまでクリックし続けます")
    
    img_file_path = "assets/images/" + img_file
    
    # 画像が表示されるまでループ
    while True:
        # スクリーンショットを取得する
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # 画像を読み込む
        img = cv2.imread(img_file_path)
        if img is None:
            logger.error(f"画像ファイルが読み込めません: {img_file_path}")
        
        # 画像を画面の画像にマッチングさせる
        res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

        # 最大値とその位置を取得
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # マッチング度が閾値(0.8)以上かどうかを確認する
        if max_val >= 0.8:
            return
        
        # Iキーを押して離す
        keyboard.press('i')
        time.sleep(0.1)
        keyboard.release('i')
        
        # 0.1 ~ 0.5秒待つ
        time.sleep(random.uniform(0.1, 0.5))