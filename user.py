import phkit

def zhfile2phfile(file,opath):
    wav_list=[]
    text_list=[]
    #输入格式化
    with open(file,encoding='utf-8') as intmp:
        for line in intmp:
            y=1
            wav=""
            text=""
            for word in line:
                if y==1:
                    if not word == ' ':
                        wav+=word
                        continue
                    else:
                        y=0
                        continue
                else:
                    if not word==" ":
                        text+=word
                        continue
                    else:
                        continue
            wav_list.append(wav)
            text_list.append(text)
    print("file loaded")
    phoneme_list=[]
    phoneme_zh=""
    for text in text_list:
        phoneme_zh="sil"
        phoneme=phkit.text2phoneme(text)
        lword=""
        for word in phoneme:
            if word == '-':
                word ='#0'#这个是分隔符
            if word == '~':
                word ='sil'#这个是首尾标志符
            if word == '_':
                word ='eos'#这个是末位标识符
            if word == '1' or word == '2' or word == '3' or word == '4' or word == '5' :
                phoneme_zh+=word
                continue
            if lword=='#0' and word == '#0':#去重复
                continue
            lword=word
            phoneme_zh+=' '+word
        phoneme_list.append(phoneme_zh+'\n')


    with open(opath+file,mode='w',encoding='utf-8') as otmp:
        for i in range(len(wav_list)):
            otmp.write(".\\file\\"+wav_list[i]+".wav |"+phoneme_list[i])#这里是输出格式化
    print("done")


if __name__ == "__main__":
    zhfile2phfile("filename",".\output\\")