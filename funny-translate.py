# 导入 requests 包
try:
    import requests
    from bs4 import BeautifulSoup
    while True:
        text=input('翻译哪些句子？（150字以下）\n')
        if len(text)>150:
            raise IOError('字数太多了 :(')
        # 发送请求
        wordlist=text.split(" ");
        print("翻译结果")
        print("="*40)
        for word in wordlist:
            try:
                x = requests.get('https://dict.youdao.com/result?word={}&lang=en'.format(word))
                x.encoding="utf-8"
                soup=BeautifulSoup(x.text,'html.parser')
                a=soup.find(class_='trans')
                tmp=a.text.split("；", 1)[0]
                if "，"in tmp:
                    tmp=tmp.split("，",1)[0]
                if "（"in tmp and tmp[0] != "（":
                    tmp=tmp.split("（",1)[0]
                if "（"in tmp:
                    tmp=tmp.replace("（","")
                    tmp=tmp.replace("）","")
                print(str(tmp),end="")
            except AttributeError:
                raise Exception('你输入的不是一个单词哦！')
        print("\n")
        print("="*30)
except ModuleNotFoundError:
    raise Exception('请确保您有下载对应的模块！')
