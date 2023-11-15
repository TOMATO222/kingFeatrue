import os
import glob
import sys

import pandas as pd

from ltp import LTP, StnSplit
ltp = LTP()  # 默认加载 Small 模型

# 得到情感词汇字典
def getDictionary():
    dictionary = {}
    file1 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/台湾大学NTUSD简体中文情感词典/ntusd-negative.txt'
    file2 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/台湾大学NTUSD简体中文情感词典/ntusd-positive.txt'
    file3 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/情感分析停用词、程度副词、否定词表/正面情绪词.txt'
    file4 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/情感分析停用词、程度副词、否定词表/负面情绪词.txt'
    file5 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/清华大学李军中文褒贬义词典/tsinghua.negative.gb.txt'
    file6 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/清华大学李军中文褒贬义词典/tsinghua.positive.gb.txt'
    file7 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/知网HowNet情感分析用词典/正面评价词语（中文）.txt'
    file8 = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/知网HowNet情感分析用词典/负面评价词语（中文）.txt'
    file_list = []
    file_list.extend([file1, file2, file3, file4, file5, file6, file7, file8])
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            for line in lines:
                # 去掉每一行的空白字符，然后添加到字典中
                word = line.strip()
                dictionary[word] = 1  # 这里的值可以是任意非空的值，因为我们只关心词语是否存在

    # 读取Excel文件
    excel_path = '/Users/tanyuyao/Documents/pythonCode/kingFeature_plus_others/Sentiment_dictionary/大连理工情感词汇本体/情感词汇本体.xlsx'  # 替换为你的Excel文件路径
    df = pd.read_excel(excel_path)
    # 指定列名
    target_column = '词语'  # 替换为你的目标列名
    # 提取指定列的内容
    target_content = df[target_column]
    # 将内容按照换行符分割，并存储在set中
    for cell_content in target_content:
        if isinstance(cell_content, str):
            dictionary[cell_content] = 1

    # 得到字典
    # print(len(dictionary))
    # print(dictionary.items())
    return dictionary

def cutwords(sentence):
    sents_list = StnSplit().split(sentence)
    words = []
    for sent in sents_list:
        words += ltp.pipeline(sent, tasks=["cws"], return_dict=False)
    return words

# 匹配词表的到形象特征词
def getFeature(txt_file, output_file):
    dictionary = getDictionary()
    # print(dictionary)
    with open(txt_file, 'r', encoding='utf-8') as file:
        # 读取文件内容并按换行符分割成句子
        sentences = file.read().split('\n')
    result = ""
    for sentence in sentences:
        sentence = sentence.replace('\n', '').replace(' ', '')
        # 分句+分词
        tokens = cutwords(sentence)
        # 将嵌套列表转为扁平的单层列表
        word_list = [word for sublist in tokens for word in sublist]
        # 输出在字典中出现的词语
        features = [word for word in word_list if word in dictionary]
        if features:
            result += sentence + '\n'
            result += ' '.join(features) + '\n' + '\n'
    with open(output_file, 'w', encoding='utf-8') as f:
        sys.stdout = f
        print(result)
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    # test
    # getDictionary()

    # 获得目标文件名称
    # 统一读入文件的路径
    directory = '/Users/tanyuyao/Documents/PaperDocument/targetDoc'
    # 读入的文件
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    # 统一输出文件的路径
    out_dir = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/feature_match'
    # 构建输出文件的路径
    for txt_file in txt_files:
        output_file = os.path.join(out_dir, os.path.basename(txt_file))
        print("*", txt_file, "*", "PROCESSING")
        getFeature(txt_file, output_file)
        print("*", txt_file, "*", "DONE")