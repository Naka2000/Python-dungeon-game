import random

# 迷宮のマップを作成
map_size = 5
treasure_location = (random.randint(0, map_size-1), random.randint(0, map_size-1))

# プレイヤーの初期位置
player_location = (0, 0)

# ゲームのループ
while True:
    # プレイヤーの位置を表示
    print("現在地:", player_location)

    # 宝物が見つかった場合、ゲーム終了
    if player_location == treasure_location:
        print("宝物を見つけました！ゲームクリア！")
        break

    # 移動方向の入力を受け付ける
    direction = input("移動方向を選択してください（上: w, 下: s, 左: a, 右: d）: ")

    # プレイヤーの移動
    if direction == "w":
        if player_location[0] > 0:
            player_location = (player_location[0] - 1, player_location[1])
        else:
            print("壁です。別の方向を選択してください。")
    elif direction == "s":
        if player_location[0] < map_size - 1:
            player_location = (player_location[0] + 1, player_location[1])
        else:
            print("壁です。別の方向を選択してください。")
    elif direction == "a":
        if player_location[1] > 0:
            player_location = (player_location[0], player_location[1] - 1)
        else:
            print("壁です。別の方向を選択してください。")
    elif direction == "d":
        if player_location[1] < map_size - 1:
            player_location = (player_location[0], player_location[1] + 1)
        else:
            print("壁です。別の方向を選択してください。")
    else:
        print("無効な入力です。")

