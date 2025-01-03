import cv2
import numpy
import pyautogui
import time
import random
import pytesseract
import keyboard
import logging

logger = logging.getLogger(__name__)
image_dir = "assets\\images\\"
threshold = 0.8

# 指定された座標をクリックする
def click(x: int, y: int):
    # マウスを移動してからクリック
    pyautogui.moveTo(x, y, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()

# 指定された範囲内のスクリーンショットを取得し、指定された画像ファイルが画面に表示されるかどうかを確認する
# 表示されていた場合は、画像の大きさと座標を返す
def _find_img(img_file: str, top_left: tuple = None, bottom_right: tuple = None) -> tuple:
    # スクリーンショットを取得する
    screenshot = pyautogui.screenshot()
    screenshot_numpy = numpy.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_numpy, cv2.COLOR_RGB2BGR)
    
    # 指定された範囲の画像を切り出す
    if top_left is not None and bottom_right is not None:
        screenshot_bgr = screenshot_bgr[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    # 画像を読み込む
    img_file_path = image_dir + img_file
    try:
        img = cv2.imread(img_file_path)
    except:
        logger.error(f"画像ファイルが読み込めません: {img_file}")
        return None, None, None

    # ボタンの画像を画面の画像にマッチングさせる
    res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

    # 最大値とその位置を取得
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # マッチング度が閾値(0.8)以上かどうかを確認する
    if max_val >= threshold:
        # 画像の大きさと座標を返す
        width = img.shape[1]
        height = img.shape[0]
        loc = max_loc
        return width, height, loc
    else:
        return None, None, None
    
# 指定された画像ファイルが画面に表示されるまで待機し、表示されたらクリックする
def click_img(img_file: str, wait_time=0) -> bool:
    logger.info(f"{img_file}が表示されるまで{wait_time}秒待機し、表示されたらクリックします")
    
    # ループ回数を計算
    loop_max = wait_time / 0.1

    # 画像が表示されるまでループ
    loop_cnt = 0
    while True:
        # 画像が表示されるかどうかを確認
        width, height, loc = _find_img(img_file)
        if width is not None:
            # 画像が表示されたらクリック
            x = loc[0] + width // 2
            y = loc[1] + height // 2
            click(x, y)
            return True
        
        # ループを抜けるかどうか判定
        loop_cnt += 1
        if loop_max != 0 and loop_cnt >= loop_max:
            logger.info(f"{img_file}が表示されませんでした")
            return False
        
        time.sleep(0.1)

# 指定された画像ファイル1内に表示される画像ファイル2をクリックする
def click_img_in_img(img_file1: str, img_file2: str, wait_time: int = 0) -> bool:
    logger.info(f"{img_file1}内に表示される{img_file2}をクリックします")
    
    # ループ回数を計算
    loop_max = wait_time / 0.1
    
    loop_cnt = 0
    while True:
        # 画像1の座標を取得
        width1, height1, loc1 = _find_img(img_file1)
        if width1 is not None:
            # 画像2の座標を取得
            width2, height2, loc2 = _find_img(img_file2, loc1, (loc1[0] + width1, loc1[1] + height1))
            if width2 is not None:
                # 画像2をクリック
                x = loc1[0] + loc2[0] + width2 // 2
                y = loc1[1] + loc2[1] + height2 // 2
                click(x, y)
                return True
        
        # ループを抜けるかどうか判定
        loop_cnt += 1
        if loop_max != 0 and loop_cnt >= loop_max:
            logger.info(f"{img_file1}の中に{img_file2}が表示されませんでした")
            return False
        
        time.sleep(0.1)

# 表示された画像内をドラッグする
def scratch_in_img(img_file: str):
    logger.info(f"{img_file}内をスクラッチします")
    
    while True:
        # 画像の座標を取得
        width, height, loc = _find_img(img_file)
        if width is not None:
            # 画像内をスクラッチ
            top_left = loc
            top_right = (top_left[0] + width, top_left[1])
            mid_left = (top_left[0], top_left[1] + (height // 2))
            mid_right = (top_left[0] + width, top_left[1] + (height // 2))
            bottom_left = (top_left[0], top_left[1] + height)
            bottom_right = (top_left[0] + width, top_left[1] + height)
            
            pyautogui.moveTo(top_left[0], top_left[1], duration=0.2)
            pyautogui.dragTo(top_right[0], top_right[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(mid_left[0], mid_left[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(mid_right[0], mid_right[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(bottom_left[0], bottom_left[1], random.uniform(0.2, 0.5))
            pyautogui.dragTo(bottom_right[0], bottom_right[1], random.uniform(0.2, 0.5))
            return
        
        time.sleep(0.1)
    
# 指定された領域内に表示されている数値を取得する
def get_val_in_img(top_left: tuple, bottom_right: tuple) -> int:
    logger.info(f"指定された領域内に表示されている数値を取得します")
    
    # スクリーンショットを取得する
    screenshot = pyautogui.screenshot()
    screenshot_numpy = numpy.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_numpy, cv2.COLOR_RGB2BGR)
    
    # 指定された領域の画像を切り出す
    area = screenshot_bgr[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    
    # 切り出した画像を保存(デバッグ用)
    cv2.imwrite("tmp\\area.png", area)
    
    # areaをグレースケールに変換
    area_gray = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)
    
    # pytesseractで数字を認識
    recognized_text = pytesseract.image_to_string(area_gray, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')
    logger.debug(f"認識されたテキスト: {recognized_text}")
    
    # 認識されたテキストを数値に変換
    try:
        val = int(recognized_text.strip())
    except ValueError:
        val = None
    
    return val

# 画像が表示されるまで待機する関数
# 画像が表示されたら、画像の大きさと座標を返す
def wait_until_img_displayed(img_file: str) -> tuple:
    logger.info(f"{img_file}が表示されるまで待機します")
    
    # 画像が表示されるまでループ
    while True:
        width, height, loc = _find_img(img_file)
        if width is not None:
            return width, height, loc
        
        time.sleep(0.1)

# 画像が表示されるまで指定されたキーを連打する
def press_key_until_img_displayed(img_file: str, key: str):
    logger.info(f"{img_file}が表示されるまでクリックし続けます")
    
    # 画像が表示されるまでループ
    while True:
        width, height, loc = _find_img(img_file)
        if width is not None:
            return
        
        # Iキーを押して離す
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        
        # 0.1 ~ 0.5秒待つ
        time.sleep(random.uniform(0.1, 0.5))

# 指定されたキーを押す
def press_key(key: str):    
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

# 2つの画像ファイルのうち、どちらが表示されているかを判定する
def which_img_displayed(img_files: list[str]) -> int:
    logger.info(f"{img_files}のうち、どちらが表示されているかを判定します")
    
    while True:
        for img_file in img_files:
            width, height, loc = _find_img(img_file)
            if width is not None:
                return img_files.index(img_file)

# 画像までポインタを移動する
def move_to_img(img_file: str):
    logger.info(f"{img_file}までポインタを移動します")
    
    width, height, loc = _find_img(img_file)
    if width is not None:
        x = loc[0] + width // 2
        y = loc[1] + height // 2
        pyautogui.moveTo(x, y, duration=0.2)

# 画像が表示されるまでスクロールする
def scroll_to_img(img_file: str):
    logger.info(f"{img_file}が表示されるまでスクロールします")
    
    # 画像が表示されるまでループ
    while True:
        width, height, loc = _find_img(img_file)
        if width is not None:
            return
        
        pyautogui.scroll(-1)

# 指定された領域内に表示されている画像の数をカウントする
def count_img_in_capture(img_file: str) -> int:
    logger.info(f"{img_file}のキャプチャ内の画像をカウントします")
    
    # スクリーンショットを取得する
    screenshot = pyautogui.screenshot()
    screenshot_numpy = numpy.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_numpy, cv2.COLOR_RGB2BGR)
    
    # 画像を読み込む
    img_file_path = image_dir + img_file
    try:
        img = cv2.imread(img_file_path)
    except:
        logger.error(f"画像ファイルが読み込めません: {img_file}")
        return None, None, None
    
    # テンプレート画像の幅と高さを取得
    height, width = img.shape[:2]

    # ボタンの画像を画面の画像にマッチングさせる
    res = cv2.matchTemplate(screenshot_bgr, img, cv2.TM_CCOEFF_NORMED)

    # 一致度が閾値を超えている座標を取得
    locs = numpy.where(res >= threshold)
    
    # 重複を防ぐためのマスクを作成
    detected_boxes = []
    for pt in zip(*locs[::-1]):  # 横と縦の座標を取得
        box = (pt[0], pt[1], pt[0] + width, pt[1] + height)
        overlap = any(
            abs(box[0] - db[0]) < width and abs(box[1] - db[1]) < height
            for db in detected_boxes
        )
        if not overlap:
            detected_boxes.append(box)

    # 一致した画像の数を返す
    logger.info(f"{img_file}のキャプチャ内の画像数: {len(detected_boxes)}")
    return len(detected_boxes)