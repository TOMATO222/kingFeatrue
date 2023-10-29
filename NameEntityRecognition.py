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
HanLP = HanLPClient('https://www.hanlp.com/api', auth=None, language='zh')


def cutwords(sentence):
    tokens = HanLP.tokenize(sentence)
    return tokens


def NER4Modern(sentence):
    # HanLP.parse(tokens=sentence, tasks='ner').pretty_print()
    NER_result = HanLP.parse(tokens=sentence, tasks='ner')
    return NER_result


def coreferenceModern(sentence):
    HanLP.coreference_resolution(sentence)


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
    # 初始化一个计数器以在每40个句子后添加换行符
    count = 0
    result = ''
    for sentence in sentences:
        result += sentence + '。'
        count += 1
        if count == 40:
            result += '\n'
            count = 0

    # 将结果写回文件
    with open(outLoc, 'w', encoding='utf-8') as output_file:
        output_file.write(result)


def test(sentence):
    # 分词
    tokens = cutwords(sentence)
    # 命名实体识别
    NER_result = NER4Modern(tokens)
    # 打印
    with open('/Users/tanyuyao/Desktop/draft/preProcessed.txt', 'w', encoding='utf-8') as file:
        sys.stdout = file
        print(NER_result)
    # 重定向标准输出到原始位置
    sys.stdout = sys.__stdout__


def pipelineWork(open_path, write_path):
    # 获得文本的段落
    sentences = getSentences(open_path)
    # 打开写入的文件

    for sentence in sentences:
        # api限流，1分钟只能调2次
        time.sleep(30)
        print(sentence)

        # 分句+分词
        tokens = cutwords(sentence)
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
            for i in range(length):
                print(tokenList[i])
                print(nerList[i])
                print('\n')
            # 重定向标准输出到原始位置
            sys.stdout = sys.__stdout__
            print("done ")
        # 关闭写入的文件
        file.close()


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

if __name__ == '__main__':
    # #################################
    # # test part
    # test(sentence='2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。高阻来到北京立方庭参观自然语义科技公司。')
    # modifytxt('/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt')
    # open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt'
    # write_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    # #################################

    # process part
    loc = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    gaozu(loc)
