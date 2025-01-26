import markdown
import sys

def main(input_path, output_path):
    # ライブラリが用意してくれている一撃変換関数
    # markdown.markdownFromFile(
    #     input=input_path, 
    #     output=output_path,
    #     extensions=['tables'])

    # ファイル操作関数を使う場合
    with open(input_path, "r") as input_file:
        input_data = input_file.read()
        
        html = markdown.markdown(input_data, extensions=['tables']) # html文字列
        
        with open(output_path, "w") as output_file:
            output_file.write(html)
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Error: Invalid arguments.")
        sys.exit(1)
    
    if sys.argv[1] != "markdown":
        print("Error: Invalid method name.")
        sys.exit(1)
    
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    
    # input_pathの拡張子が.mdでない場合はエラー
    if not input_path.endswith(".md"):
        print("Error: The input file must be a markdown file.")
        sys.exit(1)
    
    # 出力ファイルの拡張子が.htmlでない場合はエラー
    if not output_path.endswith(".html"):
        print("Error: The output file must be a html file.")
        sys.exit(1)
    
    main(input_path, output_path)
