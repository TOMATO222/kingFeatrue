from ltp import LTP, StnSplit
import os
import glob

ltp = LTP()  # 默认加载 Small 模型


# ltp = LTP(path="small")
#     其中 path 可接受的路径为下载下来的模型或者解压后的文件夹路径
#     另外也可以接受一些已注册可自动下载的模型名(可使用 ltp.available_models() 查看):
#     base/base1/base2/small/tiny/GSD/GSD+CRF/GSDSimp/GSDSimp+CRF

# 获取文本的句子（存在多个句号的情况），并分句
def getSentence(fileLoc):
    with open(fileLoc, 'r', encoding='utf-8') as file:
        # 读取文件内容并按换行符分割成句子
        sentences = file.read().split('\n')
    sentence_list = StnSplit().split(sentences)
    return sentence_list


# 分词 + 词性标注
def SEGnPOS(sentence):
    output = ltp.pipeline(sentence, tasks=["cws", "pos"])
    return output
    # output.cws -- 分词结果； output.pos -- 词性标注结果


# 依存句法分析
def depProcess(sentence):
    sentences = StnSplit().batch_split(sentence)
    result = ltp.pipeline(sentence, tasks=["cws", "dep"])
    return result
    # result.cws -- 分词结果
    # result.dep -- 依存句法分析结果


# 语义角色标注
def srlProcess(sentence):
    result = ltp.pipeline(sentence, tasks=["cws", "srl"])
    return result.srl
    # result.cws -- 分词结果
    # result.srl -- 语义角色标注结果


def test(sentcence):
    pass
    # 分句
    # sents_list = StnSplit().split(sentcence)
    # print(sents_list)

    # 分词 + 词性标注
    # result = SEGnPOS(sentcence)
    # cws_result = result.cws
    # pos_result = result.pos
    # print(cws_result)
    # print(pos_result)
    # length = len(cws_result)
    # for i in range(length):
    #     print(cws_result[i])
    #     print(pos_result[i])

    # 依存句法分析
    # dep_result = depProcess(sentcence)
    # print(dep_result.cws)
    # print(dep_result.dep)
    # '''['太公', '去', '看', '刘媪', '，', '见到', '一', '条', '蛟龙', '在', '她', '身上', '，', '后来', '刘媪', '怀', '了', '孕', '，', '就', '生', '了', '高祖', '。']
    #     {'head': [2, 0, 2, 3, 2, 2, 8, 9, 6, 6, 12, 10, 2, 16, 16, 2, 16, 16, 16, 21, 16, 21, 21, 2], 'label': ['SBV', 'HED', 'COO', 'VOB', 'WP', 'COO', 'ATT', 'ATT', 'DBL', 'VOB', 'ATT', 'VOB', 'WP', 'ADV', 'SBV', 'COO', 'RAD', 'VOB', 'WP', 'ADV', 'COO', 'RAD', 'VOB', 'WP']}
    # '''
    # length = len(dep_result.cws)
    # dep_result_head = dep_result.dep.get('head')
    # dep_result_label = dep_result.dep.get('label')
    # for i in range(length):
    #     print(dep_result.cws[i], " ", dep_result_head[i], " ", dep_result_label[i])

    # 语义角色标注
    # srl_result = srlProcess(sentence).srl
    # length = len(srl_result)
    # for i in range(length):
    #     print(srl_result[i])


if __name__ == '__main__':
    ########################################
    # test part
    # sentence = '太公去看刘媪，见到一条蛟龙在她身上，后来刘媪怀了孕，就生了高祖。'
    # test(sentence)
    ########################################

    # 统一路径文件夹
    directory = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data'
    # 拼相应文件
    # 使用glob模块来获取目录下所有的txt文件
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    for fileLoc in txt_files:
        print(fileLoc)
