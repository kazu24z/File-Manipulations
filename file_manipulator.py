import sys
from typing import Optional

class Main:    
    input_path: Optional[str] = None
    output_path: Optional[str] = None
    params: Optional[list[str]] = None

    @staticmethod
    def reverse() -> None:
        reverseImpl()
    
    @staticmethod
    def copy():
        copyImpl()
    
    @staticmethod
    def duplicate_contents():
        pass
    
    @staticmethod
    def replace_string():
        pass

def reverseImpl() -> None:
    try:
        # コマンドのバリデーション
        validate_exist_args(check_input_path=True, check_output_path=True, check_params=False)
        
        # クラス変数から入力ファイルを読み込む
        with open(Main.input_path) as file:
            contents = file.readlines() # [line1, line2, ...]
        
        output_contents = []
        
        # listの各要素の文字を逆順にする
        for line in contents:
            reversed_line = line.strip()[::-1] + "\n"
            output_contents.append(reversed_line)
        
        # 配列の要素を逆順にする（末尾から先頭にする）
        output_contents = output_contents[::-1]
        output_contents[-1] = output_contents[-1].rstrip("\n")  # 最後の要素の改行を削除
        
        # クラス変数から出力ファイルに書き込む
        with open(Main.output_path, "w") as file:
            file.writelines(output_contents)
    
    except FileNotFoundError as e:
        print(f"Error: {Main.input_path} is not found.")
    except ValueError as e:
        print(f"Error: {e}")
    
def copyImpl() -> None:
    try:
        # コマンドのバリデーション
        validate_exist_args(check_input_path=True, check_output_path=True, check_params=False)
        
        # クラス変数から入力ファイルを読み込む
        with open(Main.input_path) as file:
            contents = file.readlines() # [line1, line2, ...]
        
        with open(Main.output_path, "w") as file:
            file.writelines(contents)
    except FileNotFoundError as e:
        print(f"Error: {Main.input_path} is not found.")
    except ValueError as e:
        print(f"Error: {e}")

def validate_exist_args(check_input_path: bool, check_output_path: bool, check_params: bool) -> None:
    errors: list[str] = []
    
    if check_input_path and Main.input_path is None:
        errors.append("The input_path argument is required.")
    if check_output_path and Main.output_path is None:
        errors.append("The output_path argument is required.")
    if check_params and Main.params is None:
        errors.append("params argument is required.")
    
    if errors:
        error_message = "\n".join(errors)
        
        raise ValueError(error_message)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        method_name = sys.argv[1]  # コマンドライン引数でメソッド名を取得
        Main.input_path = sys.argv[2] if len(sys.argv) > 2 else None
        Main.output_path = sys.argv[3] if len(sys.argv) > 3 else None
        Main.params = sys.argv[4:] if len(sys.argv) > 4 else None

        if hasattr(Main, method_name):
            method = getattr(Main, method_name)
            method()  # メソッドを実行
        else:
            print(f"Error: Method '{method_name}' not found in class Main.")
    else:
        print("Error: No method specified.")
        