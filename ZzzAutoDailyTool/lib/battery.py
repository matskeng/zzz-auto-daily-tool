import logging
import json
import time
from . import util

logger = logging.getLogger(__name__)

# 所持バッテリー値を取得する
def _get_current_battery() -> int:
    logger.info('所持バッテリー値を取得します')
    
    # F2ボタンが表示されるまで待機
    util.wait_until_img_displayed("button_f2.png")
    # F2キーを押す
    util.press_key("f2")
    
    # 訓練タブが表示されていない場合、タブを切り替える
    if util.which_img_displayed(["panel_practice_not_chosen.png", "panel_practice_chosen.png"]) == 0:
        util.click_img("panel_practice_not_chosen.png")
    
    # 所持バッテリー値を確認する
    width, height, loc = util.wait_until_img_displayed("current_battery.png")
    current_battery = util.get_val_in_img((loc[0]+width, loc[1]), (loc[0]+width+65, loc[1]+height))
    logger.info(f"所持バッテリー値: {current_battery}")
    
    return current_battery

# ユーザー設定を読み込む
def _load_user_setting() -> tuple:
    logger.info('バッテリー使用方法を読み込みます')
    
    # user_config.jsonを読み込む
    with open("config\\user_setting.json", "r", encoding="utf-8") as f:
        setting = json.load(f)
        
    # 戦闘で使用するキーを取得
    battle_key = setting["battle_key"]
    
    # バッテリー使用方法のidを取得
    id = setting["battery_usage_id"]
    
    # battery_usage_methods.jsonを読み込む
    with open("config\\battery_usage_methods.json", "r", encoding="utf-8") as f:
        battery_usage_methods = json.load(f)
        
        # idが一致する要素を検索
        for method in battery_usage_methods["methods"]:
            if method["id"] == id:
                category1 = method["category1"]
                category2 = method["category2"]
                category3 = method["category3"]
                break
    
    return category1, category2, category3, battle_key

# バッテリー使用方法を選択する
def _choose_battery_usage(category1: str, category2: str, category3: str):
    logger.info('バッテリー使用方法に従って戦闘画面に移行します')
    
    # カテゴリ1の選択
    util.click_img(f"category1_{category1}.png")
    # カテゴリ2の選択
    util.move_to_img("button_go_2.png")
    util.scroll_to_img(f"category2_{category2}.png")
    util.click_img_in_img(f"category2_{category2}.png", "button_go_2.png")
    util.click_img("button_ok.png")
    # カテゴリ3の選択
    util.click_img(f"category3_{category3}.png")

# 戦闘で出現する敵の設定
def _set_enemy_count(category3: str, enemy_count: int):
    logger.info('戦闘で出現する敵の設定を行います')
    
    # 戦闘で出現する敵の設定
    width, height, loc = util.wait_until_img_displayed(f"category3_{category3}.png")
    util.click(loc[0]+width//2, loc[1]+height//2-500)
    util.wait_until_img_displayed("button_save_deck.png")
    enemy_count_set = 5 - util.count_img_in_capture("enemy_empty.png")
    while enemy_count != enemy_count_set:
        if enemy_count < enemy_count_set:
            util.click_img(f"decrease_enemy_{category3}.png")
            enemy_count_set -= 1
        else:
            util.click_img(f"increase_enemy_{category3}.png")
            enemy_count_set += 1
        time.sleep(0.1)
    util.click_img("button_save_deck.png")

# 戦闘を行う
def _battle(battle_key: str):
    logger.info('戦闘を行います')
        
    # 完了ボタンが表示されるまで、通常攻撃のキーを連打する
    time.sleep(1)
    util.press_key_until_img_displayed("button_complete.png", battle_key)
    
# バッテリーがなくなるまで戦闘を行う
def _battle_until_battery_empty(battery: int, category1: str, category2: str, category3: str, battle_key: str):
    logger.info('バッテリーがなくなるまで戦闘を行います')
    
    # 1戦闘ごとのバッテリー消費量を設定
    if category1 == "mock_practice":
        # 戦闘回数を計算
        full_battle_num = battery // 100
        extra_enemy_num = (battery % 100) // 20
        
        # フル戦闘(敵5体分の戦闘)を消化
        if full_battle_num > 0:
            # 戦闘で出現する敵の設定
            _set_enemy_count(category3, 5)
            # フル戦闘を行う
            for battle_count in range(full_battle_num):
                # 初回
                if battle_count == 0:
                    # 次へボタンをクリック
                    util.click_img("button_next.png")
                    # 出撃ボタンをクリック
                    util.click_img("button_sortie.png")
                    # 戦闘を行う
                    _battle(battle_key)
                # 2回目以降
                else:
                    # リトライボタンをクリック
                    util.click_img("button_retry.png")
                    # 戦闘を行う
                    _battle(battle_key)
            # 完了ボタンをクリック
            util.click_img("button_complete.png")
            
        # 余りの敵を戦闘を消化
        if extra_enemy_num > 0:
            # 戦闘で出現する敵の設定
            _set_enemy_count(category3, extra_enemy_num)
            # 次へボタンをクリック
            util.click_img("button_next.png")
            # 出撃ボタンをクリック
            util.click_img("button_sortie.png")
            # 戦闘を行う
            _battle(battle_key)
            # 完了ボタンをクリック
            util.click_img("button_complete.png")
    else:
        # 戦闘回数を計算
        battle_num = battery // 40
        # 戦闘を行う
        for battle_count in range(battle_num):
                # 初回
                if battle_count == 0:
                    # 次へボタンをクリック
                    util.click_img("button_next.png")
                    # 出撃ボタンをクリック
                    util.click_img("button_sortie.png")
                    # 戦闘を行う
                    _battle(battle_key)
                # 2回目以降
                else:
                    # リトライボタンをクリック
                    util.click_img("button_retry.png")
                    # 戦闘を行う
                    _battle(battle_key)
        # 完了ボタンをクリック
        util.click_img("button_complete.png")
    
    # 戻るボタンをクリック
    util.click_img("button_return.png")
    # 戻るボタンをクリック
    util.click_img("button_return.png")

# バッテリーを使用する
def use_battery():
    logger.info('バッテリーを使用します')
    
    # 所持バッテリー値を取得する
    current_battery = _get_current_battery()
    
    # ユーザー設定を読み込む
    category1, category2, category3, battle_key = _load_user_setting()
    
    # バッテリー使用方法を選択する
    _choose_battery_usage(category1, category2, category3)
    
    # バッテリーがなくなるまで戦闘を行う
    _battle_until_battery_empty(current_battery, category1, category2, category3, battle_key)
