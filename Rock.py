
# 플레이어와 컴퓨터가 참여하는 가위바위보 게임
# 플레이어가 가위,바위,보 중 하나를 입력합니다.
# 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
# 결과를 출력하여 승부를 알려줍니다.
# 게임의 승, 패, 무승부의 횟수를 기록합니다.
# 게임 종료 시에 플레이어에게 통계를 제공합니다.
# 플레이어가 입력할 때 대소문자를 구분하지 않도록 합니다.
# 플레이어가 게임을 반복하고 싶을 경우 재시작 하거나, 종료하는 기능을 추가해주세요.

import random
import re


def game_start():

    game = ['가위', '바위', '보']
    computer_player = random.choice(game)

    victory_count = 0
    defeat_count = 0
    draw_count = 0

    while True:
        user = input("가위, 바위, 보 중 하나를 선택해주세요").strip()
        kor = re.sub(r"[^가-힣]", "", user)

        # kor 가 game 안에 없을 때
        if kor not in game:
            print("유효한 입력이 아닙니다.")
            continue

        if computer_player == "가위" and user == "바위" or computer_player == "바위" and user == "보" or computer_player == "보" and user == "가위":
            print("사용자 승리")
            victory_count += 1

        elif computer_player == "바위" and user == "가위":
            print("컴퓨터 승리")
            defeat_count += 1

        else:
            print("비겼습니다.")
            draw_count += 1

        restart = input("다시 하시겠습니까? (y/n)")
        if restart == "Y" or restart == "y":
            pass  # 아무것도 안하면 if문으로 들어감
        else:
            print("게임을 종료합니다.")
            print(f'승: {victory_count}, 패: {defeat_count}, 무:{draw_count}')
            break


game_start()
