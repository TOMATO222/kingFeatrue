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

def modifytxt(fileLoc):
    with open(fileLoc, 'r', encoding='utf-8') as file:
        text = file.read()
    # 使用字符串替换功能将换行符和空格替换为空字符
    text = text.replace('\n', '').replace(' ', '')
    print(text)
    return text


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
    # 打开写入的文件
    with open(write_path, 'a', encoding='utf-8') as file:
        # # 获得分句
        # sentences = getSentences(open_path)

        # 获得初始文本
        sentences = modifytxt(open_path)

        # 针对每一个分句进行命名实体识别与结果打印
        id = 1
        for sentence in sentences:
            # hanLP接口限流
            time.sleep(60)
            # 在休息结束后执行后续代码
            print("1分钟休息结束，执行后续代码")

            # 分词
            tokens = cutwords(sentence)
            # 命名实体识别
            NER_result = NER4Modern(tokens)
            # 打印
            # 重定向输出位置为打开的文件
            sys.stdout = file
            print("【", id, "】", " : ", sentence)
            id += 1
            print(NER_result)
            print('\n')
            # 重定向标准输出到原始位置
            sys.stdout = sys.__stdout__
            print("done: ", sentence)

    # 关闭写入的文件
    file.close()

def gaozu(loc):
    # open file location
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt'
    # writen file location
    custom_filename = 'gaozu.txt'
    write_path = os.path.join(loc, custom_filename)
    pipelineWork(open_path, write_path)

if __name__ == '__main__':
    # #################################
    # # test part
    # test(sentence='2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。高阻来到北京立方庭参观自然语义科技公司。')
    # modifytxt('/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt')
    open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/gaozu/target.txt'
    write_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    # #################################

    # # lvtaihou
    # # open file location
    # open_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/lvtaihou/target2.txt'
    # # writen file location
    # write_path = '/Users/tanyuyao/Documents/PaperDocument/Historian/EnglishLoc/lvtaihou/preProcessed.txt'

    # # process part
    # pipelineWork(open_path, write_path)
