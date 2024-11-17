import keyboard
from .screen_recog import rcg_and_click
from .screen_recog import rcg_and_click_while_loop
from .screen_recog import rcg_and_return_coords_while_loop
from .screen_recog import rcg_and_click_in_area

# HoYoPlayランチャーからゲームを起動する関数
def start_game():
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
    # インターノット会員報酬を受け取るボタンをクリック
    rcg_and_click_while_loop("internot_reward.png", 10)

# コーヒーを飲む関数
def drink_coffee():
    # F2キーを押す
    keyboard.press('f2')
    
    # コーヒーを飲むパネルが表示されるか確認
    top_left, bottom_right = rcg_and_return_coords_while_loop("task_drink_coffee.png", 3)
    
    # コーヒーを飲むパネルが表示されなかった場合は関数を抜ける
    if top_left is None:
        return
    
    # パネル内のgoボタンをクリック
    rcg_and_click_in_area("button_go.png", top_left, bottom_right)
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
    
    # 注文ボタンをクリック
    rcg_and_click("button_order.png")
    
    # OKボタンをクリック
    rcg_and_click("button_ok.png")
