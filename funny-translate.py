# 导入 requests 包
try:
    import requests
    from bs4 import BeautifulSoup
    while True:
        text=input('翻译哪些句子？（150字以下）：')
        if len(text)>150:
            raise IOError('字数太多了 :(')
        # 发送请求
        text=text.replace(","," ， ")
        text=text.replace("."," 。 ")
        text=text.replace("!"," ！ ")
        text=text.replace("?"," ？ ")
        wordlist=text.split(" ")
        print("翻译结果")
        print("="*40)
        for word in wordlist:
            try:
                if word not in "？！。，":
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
                else:
                    print(word,end="")
            except AttributeError:
                raise Exception('请检查单词拼写是否有错')
        print("\n")
        print("="*30)
except ModuleNotFoundError:
    raise Exception('请确保您有下载对应的模块！')
