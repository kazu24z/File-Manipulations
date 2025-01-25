import sys
import random

def main():
    args = sys.argv
    if len(args) < 3:  # 引数が足りない場合のチェック
        print("Error: python3 main.py <arg1> <arg2>")
        return

    # 入力値n, mを取得
    try:
        n = int(args[1])  # 最初の引数を取得
        m = int(args[2])  # 2番目の引数を取得
    except ValueError:
        print("Error: arg1 and arg2 must be integer")
        return
    
    if(n > m):
        print("Error: arg1 must be less than arg2")
        return
    
    # n~mまでの範囲で乱数を生成
    randNum = random.randint(n, m)
    
    # 回答を求める標準入力受付
    for x in range(n):
        answer = input(f"Input answer（now {x+1} times）:")
        answer = int(answer)
        if answer == randNum:
            print("Excellent!")
            break
        else:
            print("Miss...")

if __name__ == "__main__":
    main()
