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
        duplicate_contentsImpl()
    
    @staticmethod
    def replace_string():
        replace_stringImpl()

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
        
def duplicate_contentsImpl() -> None:
    try:
        # コマンドのバリデーション
        validate_exist_args(check_input_path=True, check_output_path=False, check_params=True)

        # 関数個別のバリデーション
        errors = []

        if(len(Main.params) != 1):
            errors.append("The params must have one int element.")
        if len(Main.params) == 1 and not Main.params[0].isnumeric():
            errors.append("The param must be an integer.")
        if errors:
            error_message = "\n".join(errors)
            raise ValueError(error_message)

        # クラス変数から入力ファイルを読み込む
        with open(Main.input_path, "a+") as file:
            file.seek(0)
            contents = file.readlines()
            for n in range(int(Main.params[0])):
                file.writelines(contents)

    except FileNotFoundError as e:
        print(f"Error: {Main.input_path} is not found.")
    except ValueError as e:
        print(f"Error: {e}")

def replace_stringImpl() -> None:
    try:
        # コマンドのバリデーション
        validate_exist_args(check_input_path=True, check_output_path=False, check_params=True)

        # 関数個別のバリデーション
        errors = []
        if(len(Main.params) != 2):
            errors.append("The params must have two string element.")
        if errors:
            error_message = "\n".join(errors)
            raise ValueError(error_message)

        with open(Main.input_path, "r+") as file:
            contents = file.readlines() # 先頭から読み取って１行ごとにリストに格納
            
            updated_contents = [line.replace(Main.params[0], Main.params[1]) for line in contents] # 各行の文字列を置換
            
            file.seek(0) # 上書きするためにポインタをファイルの先頭に移動
            file.writelines(updated_contents)
            file.truncate() # ファイルの末尾を切り詰める

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
        raw_method_name= sys.argv[1] if len(sys.argv) > 1 else None
        if raw_method_name is None:
            print("Error: No method specified.")
            sys.exit(1)
        
        method_name = raw_method_name.replace("-", "_")
        
        # コマンド事に引数を解析する
        if method_name == "reverse":
            if len(sys.argv) < 3:
                print("Error: Invalid arguments.")
                sys.exit(1)
            
            Main.input_path = sys.argv[2]
            Main.output_path = sys.argv[3]
        elif method_name == "copy":
            if len(sys.argv) < 3:
                print("Error: Invalid arguments.")
                sys.exit(1)
            
            Main.input_path = sys.argv[2]
            Main.output_path = sys.argv[3]
        elif method_name == "duplicate_contents":
            if len(sys.argv) < 3:
                print("Error: Invalid arguments.")
                sys.exit(1)
            
            Main.input_path = sys.argv[2]
            Main.params = sys.argv[3:]
        elif method_name == "replace_string":
            if len(sys.argv) < 4:
                print("Error: Invalid arguments.")
                sys.exit(1)
            
            Main.input_path = sys.argv[2]
            Main.params = sys.argv[3:]
        # 実行    
        if hasattr(Main, method_name):
            method = getattr(Main, method_name)
            method()  # メソッドを実行
        else:
            print(f"Error: Method '{method_name}' not found in class Main.")
            sys.exit(1)
        
    else:
        print("Error: No method specified.")
        