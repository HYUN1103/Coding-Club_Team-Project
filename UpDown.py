# 플레이어와 컴퓨터가 참여하는 업다운게임

# 컴퓨터는 1부터 100사이의 랜덤한 숫자를 생성
# 플레이어는 숫자를 입력 = 컴퓨터의 숫자를 비교
# "업" 혹은 "다운" , "힌트 " 제공
# 플레이어가 숫자를 맞힐 때까지 위 과정을 반복한다.
# 플레이어가 입력한 숫자 의외에 입력한 경우 숫자를 입력하도록 유도
# 시도한 횟수, 재게임질문, 게임종료 문구 출력


import random


def game_updaum():

    print("Up,Down 게임을 시작합니다.")

    # 컴퓨터는 1부터 100까지 랜덤으로 뽑는다.
    computer_user = random.randint(1, 100)
    # print(computer_user)

    count = 0  # 게임 횟수를 알려준다.

    while True:
        user_player = input("숫자를 입력하세요")  # 유저가 입력을 받는다.

        if not user_player.isdigit() or int(user_player) == 0 or int(user_player) > 100:
            print("유효한 범위 내의 숫자를 입력하세요 ")
            continue

        user_player = int(user_player)
        count += 1

        if computer_user == user_player:
            print("맞았습니다!!")
            print(f'시도한 횟수: {count}')
            break

        elif computer_user > user_player:
            print("UP")
        else:
            print("Down")

    restart_game = input("게임을 다시 시작하겠습니다? (Y/N)")

    if restart_game == "Y" or restart_game == "y":
        game_updaum()
    else:
        print("게임을 종료합니다.")


game_updaum()
