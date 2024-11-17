from .lib import control_game

# ツールのメイン処理
def main():
    # # ゲームを起動する
    # control_game.start_game()
    
    # インターノット会員報酬を受け取る
    control_game.get_internot_rewards()
    
    # コーヒーを飲む
    control_game.drink_coffee()

if __name__ == "__main__":
    main()
