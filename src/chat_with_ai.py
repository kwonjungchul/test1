# chat_with_ai.py
import os

def handle_user_input(user_input):
    if user_input.lower().startswith("run auto trading"):
        os.system("python run_auto_trading.py")
        return "자동매매 프로세스가 시작되었습니다."

    # 다른 명령 처리 추가 가능

    return "알 수 없는 명령입니다."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = handle_user_input(user_input)
        print(f"AI: {response}")
