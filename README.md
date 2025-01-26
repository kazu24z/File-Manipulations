# Some CLIs

## Guess the number game

ランダムで生成される数値を当てるCLIゲームです。

### 遊び方

1. 以下のようにn, mに任意の整数を入力して実行します。（nはm未満）
2. 回答の入力を求められるので、n~mまでの整数値を入力して回答します。
3. 正解の場合は「Excellent!」と表示され、不正解の場合は「Miss...」と表示され再入力を求められます。
※不正解の場合はトータルでn回まで入力が可能です。

```
python3 main.py　<n> <m>

実行例
python3 main.py 2 10
```

## File Manipulator
ファイルへの操作をCLI上で実行できるツールです。

### コマンド

基本
```
python3 file_manipulator.py <コマンド名> 引数1 ... 引数n
```

### reverse
  指定したファイルの内容を逆にしたファイルを出力します。

  `python3 file_manipulator.py reverse <入力ファイルパス> <出力ファイルパス>`

### copy
  指定したファイルの内容をコピーしたファイルを出力します。

  `python3 file_manipulator.py copy <入力ファイルパス> <出力ファイルパス>`

### duplicate-contents
  指定したファイルの内容を、指定した回数分重複させます。

  `python3 file_manipulator.py duplicate-contents <入力ファイルパス> 繰り返し回数`

### replace-string
  指定したファイル内にある"needle"を"new-string"に置き換えます。

  `python3 file_manipulator.py replace-string <入力ファイルパス> <needle> <new-string>`

## File Converter
markdown形式をHTMLに変換するツールです。

### コマンド

```
python3 file-converder.py markdown <mdファイルパス> <htmlファイルパス>
```
