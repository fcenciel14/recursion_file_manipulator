import sys

# 引数の入力をチェック
def validate_arguments(args, n):
    if len(sys.argv) != n:
        print("Invalid arguments")
        sys.exit(1)

# 内容を反転
def reverse_file_contents(inputpath, outputpath):
    validate_arguments(sys.argv, 4)
    with open(inputpath, 'r') as input_file:
        contents = input_file.read()

    reversed_contents = contents[::-1]

    with open(outputpath, 'w') as output_file:
        output_file.write(reversed_contents)

# 内容を複製
def copy_file_contents(inputpath, outputpath):
    validate_arguments(sys.argv, 4)
    with open(inputpath, 'r') as input_file:
        contents = input_file.read()

    with open(outputpath, 'w') as output_file:
        output_file.write(contents)

# 内容を同一ファイル内にn回複製
def duplicate_file_contents(inputpath, n):
    validate_arguments(sys.argv, 4)
    with open(inputpath, 'r') as input_file:
        contents = input_file.read()

    with open(inputpath, 'a') as input_file:
        for i in range(0, int(n)):
            input_file.write(contents)

# 文字列の置換
def replace_file_contents(inputpath, old_string, new_string):
    validate_arguments(sys.argv, 5)
    with open(inputpath, 'r') as input_file:
        contents = input_file.read()

    with open(inputpath, 'w') as input_file:
        input_file.write(contents.replace(old_string, new_string))


# スクリプトが直接実行された場合、__name__は__main__となる
if __name__ == "__main__":
    # スクリプトが直接実行された場合の処理
    # インポートされた場合は実行されない
    command = sys.argv[1]
    inputpath = sys.argv[2]

    if command == "reverse":
        outputpath = sys.argv[3]
        reverse_file_contents(inputpath, outputpath)
    elif command == "copy":
        outputpath = sys.argv[3]
        copy_file_contents(inputpath, outputpath)
    elif command == "duplicate-contents":
        n = sys.argv[3]
        duplicate_file_contents(inputpath, n)
    elif command == "replace-string":
        old_string = sys.argv[3]
        new_string = sys.argv[4]
        replace_file_contents(inputpath, old_string, new_string)
    else:
        print("Invalid command.")
