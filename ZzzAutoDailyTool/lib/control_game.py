from .screen_rcg_and_click import screen_rcg_and_click

# HoYoPlayランチャーからゲームを起動する関数
def start_game():
    # ZZZのアイコンをクリック
    screen_rcg_and_click("launcher_zzz.png")
    
    # ゲーム開始のボタンをクリック
    screen_rcg_and_click("launcher_start_game.png")
    
    # ゲーム内でゲーム開始が表示されたらクリック
    screen_rcg_and_click("game_start_game.png")
    
    # ゲーム内でゲーム開始が表示されたらクリック
    screen_rcg_and_click("game_start_game.png")

# インターノット会員報酬を受け取る関数
def get_internot_rewards():
    # インターノット会員報酬を受け取るボタンをクリック
    screen_rcg_and_click("internot_rewards.png")
