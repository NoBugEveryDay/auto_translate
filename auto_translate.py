import sys
sys.path.append(sys.path[0]+"/pip_lib")

# pip install pyperclip --target=./pip_lib
# pip install requests --target=./pip_lib

import pyperclip
import time
import translator

def aggregate_translate(text):
    try:
        print("==================")
        print("=Youdao Translate=")
        print("==================")
        translator.main(argv = ["", "--engine=youdao", "--from=en", "--to=zh-CH", text])
        print()
    except Exception as e:
        print(e)
    
    if (len(text) > 30):
        return
    try:
        print("================")
        print("=Bing Translate=")
        print("================")
        translator.main(argv = ["", "--engine=bing", "--from=en", "--to=zh-CH", text])
        print()
    except Exception as e:
        print(e)
    
    try:
        print("==================")
        print("=Google Translate=")
        print("==================")
        translator.main(argv = ["", "--engine=google", "--from=en", "--to=zh-CH", text])
        print()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("=========================================")
    while True:
        try:
            old_text = str(pyperclip.paste())
            while True:
                new_text = str(pyperclip.paste())
                if new_text != old_text:
                    old_text = new_text
                    new_text = new_text.replace('\r\n', ' ')
                    new_text = new_text.split('.')
                    for i in new_text:
                        if i == '' or len(i) <= 2:
                            continue
                        i = i + "."
                        print(i)
                        aggregate_translate(i)
                        print("=========================================")
                time.sleep(1)
        except Exception as e:
            print(e)
            print("=========================================")

        time.sleep(1)