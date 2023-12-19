# # 处理古文
# from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("SIKU-BERT/sikubert")
# model = AutoModel.from_pretrained("SIKU-BERT/sikubert")
import os
import sys
import time

# 处理现代文
from hanlp_restful import HanLPClient

# auth不填则匿名，zh中文，mul多语种
HanLP = HanLPClient('https://www.hanlp.com/api', auth='MzI5N0BiYnMuaGFubHAuY29tOmNwRDNYbktubWRnUmQ4ZmQ=', language='zh')


## 针对具体文本的调用 ##
def gaozu(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'gaozu.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def lvtaihou(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/lvtaihou/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/lvtaihou/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'lvtaihou.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def qin(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/qin/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/qin/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'qin.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def qinshihuang(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/qinshihuang/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/qinshihuang/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'qinshihuang.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def wudi(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/wudi/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/wudi/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'dishun.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def xia(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xia/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xia/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'yu.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def xiangyu(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiangyu/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiangyu/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'xiangyu.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def xiaojing(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaojing/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaojing/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'xiaojing.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def xiaowen(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaowen/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaowen/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'xiaowen.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def xiaowu(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaowu/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/xiaowu/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'xiaowu.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def yin(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/yin/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/yin/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'wuwang.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)


def zhou(loc):
    # 原始文本地址
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/zhou/target.txt'
    # 合并段落的文本地址--用于命名实体识别的文件
    outLoc = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/zhou/target2.txt'
    # 合并段落
    modifytxt(open_path, outLoc)

    # 写入处理结果的文本地址
    custom_filename = 'tang.txt'
    write_path = os.path.join(loc, custom_filename)

    # 命名实体识别
    pipelineWork(outLoc, write_path)




def cutwords(sentence):
    tokens = HanLP.tokenize(sentence)
    return tokens


def NER4Modern(sentence):
    # HanLP.parse(tokens=sentence, tasks='ner').pretty_print()
    NER_result = HanLP.parse(tokens=sentence, tasks='ner')
    return NER_result


def coreferenceModern(sentence):
    COR_result = HanLP.coreference_resolution(tokens=sentence)
    return COR_result


def getSentences(fileLoc):
    with open(fileLoc, 'r', encoding='utf-8') as file:
        # 读取文件内容并按换行符分割成句子
        sentences = file.read().split('\n')
    return sentences


def modifytxt(fileLoc, outLoc):
    with open(fileLoc, 'r', encoding='utf-8') as file:
        text = file.read()
    # 使用字符串替换功能将换行符和空格替换为空字符
    text = text.replace('\n', '').replace(' ', '')

    # 按句号分割文本
    sentences = text.split('。')
    # 初始化一个计数器以在每50个句子后添加换行符
    count = 0
    result = ''
    for sentence in sentences:
        result += sentence + '。'
        count += 1
        if count == 50:
            result += '\n'
            count = 0

    # 将结果写回文件
    with open(outLoc, 'w', encoding='utf-8') as output_file:
        output_file.write(result)


def test(sentence):
    # 分词
    tokens = cutwords(sentence)
    # 指代消解
    COR_result = coreferenceModern(tokens)
    # 命名实体识别
    NER_result = NER4Modern(tokens)
    # 规范输出
    # 匹配结果里的token & ner，并打印出来
    tokenList = NER_result.get("tok")
    nerList = NER_result.get("ner/msra")
    length = len(tokenList)
    # 打印
    with open('/Users/tanyuyao/Desktop/draft/preProcessed.txt', 'w', encoding='utf-8') as file:
        sys.stdout = file
        print('**********')
        print(sentence)
        for cor in COR_result:
            print(cor)
        print('\n')
        for i in range(length):
            print(tokenList[i])
            print(nerList[i])
            print('\n')
        print('\n')
    # 重定向标准输出到原始位置
    sys.stdout = sys.__stdout__
    print("done")


def pipelineWork(open_path, write_path):
    # 获得文本的段落
    sentences = getSentences(open_path)
    # 打开写入的文件

    for sentence in sentences:
        # api限流，1分钟只能调50次
        time.sleep(5)
        print(sentence)

        # 分句+分词
        tokens = cutwords(sentence)
        # 指代消解
        COR_result = coreferenceModern(tokens)
        # 命名实体识别
        NER_result = NER4Modern(tokens)
        # 匹配结果里的token & ner，并打印出来
        tokenList = NER_result.get("tok")
        nerList = NER_result.get("ner/msra")
        length = len(tokenList)
        # 打印
        with open(write_path, 'a', encoding='utf-8') as file:
            # 重定向输出位置为打开的文件
            sys.stdout = file
            print('**********')
            # 打印段落
            print(sentence)
            # 打印该段落的指代消解结果
            for cor in COR_result:
                print(cor)
            print('\n')
            # 打印该段落各句子的命名实体识别结果
            for i in range(length):
                print(tokenList[i])
                print(nerList[i])
                print('\n')
            print('\n')
            # 重定向标准输出到原始位置
            sys.stdout = sys.__stdout__
            print("done ")
        # 关闭写入的文件
        file.close()




if __name__ == '__main__':
    # #################################
    # # test part
    # sentence = '高祖，沛县丰邑中阳里人。姓刘，字季。父亲叫太公，母亲叫刘媪。先前刘媪曾经在大湖岸边休息，睡梦中与神相遇。这时雷电交作，天昏地暗。太公去看刘媪，见到一条蛟龙在她身上，后来刘媪怀了孕，就生了高祖。'
    # test(sentence)
    # modifytxt('/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt')
    # open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt'
    # write_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    # coreferenceModern('高祖，沛县丰邑中阳里人。姓刘，字季。父亲叫太公，母亲叫刘媪。先前刘媪曾经在大湖岸边休息，睡梦中与神相遇。这时雷电交作，天昏地暗。太公去看刘媪，见到一条蛟龙在她身上，后来刘媪怀了孕，就生了高祖。')
    # #################################

    # process part
    loc = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    # gaozu(loc)
    # print("gaozu done")
    # lvtaihou(loc)
    # print("lvtaihou done")
    qin(loc)
    print("qin done")
    qinshihuang(loc)
    print("qinshihuang done")
    wudi(loc)
    print("wudi done")
    xia(loc)
    print("xia done")
    xiangyu(loc)
    print("xiangyu done")
    xiaojing(loc)
    print("xiaojing done")
    xiaowen(loc)
    print("xiaowen done")
    xiaowu(loc)
    print("xiaowu done")
    yin(loc)
    print("yin done")
    zhou(loc)
    print("zhou done")
