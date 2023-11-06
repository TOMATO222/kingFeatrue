import os
import glob
import re
import time

from ltp import LTP, StnSplit
ltp = LTP()  # 默认加载 Small 模型
# ltp = LTP(path="small")
#     其中 path 可接受的路径为下载下来的模型或者解压后的文件夹路径
#     另外也可以接受一些已注册可自动下载的模型名(可使用 ltp.available_models() 查看):
#     base/base1/base2/small/tiny/GSD/GSD+CRF/GSDSimp/GSDSimp+CRF

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
    # srl_result = srlProcess(sentence)
    # length = len(srl_result)
    # for i in range(length):
    #     print(srl_result[i])

    # 规则1
    # rule1(sentcence, 0)

    print(sentcence)
    cws_result = SEGnPOS(sentcence).cws
    pos_result = SEGnPOS(sentcence).pos
    dep_result = depProcess(sentcence).dep

    # 规则2
    for c, p, h, l in zip(cws_result, pos_result, dep_result['head'], dep_result['label']):
        print(f"{c:<6} {p:<4} {h:<4} {l}")
    flag, triples, dependency_dict = rule2(cws_result, pos_result, dep_result, 0)
    for word, info in dependency_dict.items():
        print(word, ": ", info)

    # 规则5
    # flag, triples = rule5(dependency_dict, 0)
    # print(triples)

    # 规则6
    flag, triples = rule6(dependency_dict, 0)
    print(flag)
    print(triples)


    # 执行抽取函数
    # extraction(sentence)


# 获取文本的句子（存在多个句号的情况），并分句
def getSentence(fileLoc):
    with open(fileLoc, 'r', encoding='utf-8') as file:
        # 读取文件内容并按换行符分割成句子
        sentences = file.read().split('\n')
    sentence_list = []
    for sentence in sentences:
        new_sentence = re.sub(r'\s', '', sentence)
        sents_list = StnSplit().split(new_sentence)
        for sent in sents_list:
            sentence_list.append(sent)
    return sentence_list


# 分词 + 词性标注
def SEGnPOS(sentence):
    output = ltp.pipeline(sentence, tasks=["cws", "pos"])
    return output
    # output.cws -- 分词结果； output.pos -- 词性标注结果


# 依存句法分析
def depProcess(sentence):
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

# 利用规则抽取事件三元组
def extraction(sentence):
    # 返回结果
    result = ""

    print(sentence)
    result += sentence + '\n'

    # 用于去重
    triple_in = []

    # 判断 规则 是否抽取出了对应三元组 0-no, 1-rule1 ,..., 5-rule5
    flag = 0

    # 规则1
    flag, triples1 = rule1(sentence, flag)
    # 规则1 抽到了三元组
    if flag == 1:
        for triple in triples1:
            # print("【RULE 1】", triple)
            result += "【RULE 1】" + str(triple) + '\n'
            triple_in.append(triple)

    # 进入规则2-5，依赖于词性标注结果+依存句法分析结果
    cws_result = SEGnPOS(sentence).cws
    pos_result = SEGnPOS(sentence).pos
    dep_result = depProcess(sentence).dep

    # dependency_dict: 该句话词性标注为verb 的词的依存句法结果字典

    # 规则2
    flag, triple2, dependency_dict = rule2(cws_result, pos_result, dep_result, flag)
    # 规则2 抽到了三元组
    if flag == 2:
        for triple in triple2:
            if triple not in triple_in:
                # print("【RULE 2】", triple)
                result += "【RULE 2】" + str(triple) + '\n'
                triple_in.append(triple)

    # 规则5
    flag, triple5 = rule5(dependency_dict, flag)
    # 规则5 抽到了三元组
    if flag == 5:
        for triple in triple5:
            if triple not in triple_in:
                # print("【RULE 5】", triple)
                result += "【RULE 5】" + str(triple) + '\n'
                triple_in.append(triple)

    # 规则6 用于优化和补充抽取
    if flag == 0:
        flag, triple6 = rule6(dependency_dict, flag)
    # 规则6 抽到了三元组
    if flag == 6:
        for triple in triple6:
            if triple not in triple_in:
                result += "【RULE 6】" + str(triple) + '\n'
                triple_in.append(triple)

    # 方便看，每个句子完成后空行
    # print('\n')
    result += '\n'

    return result

    # # 规则3 -- 不采用
    # flag, triple3 = rule3(dependency_dict, flag)
    # # 规则3 抽到了三元组
    # if flag == 3:
    #     print("【RULE 3】", triple3)

    # 规则4 -- 不采用
    # flag, triple4 = rule4(dependency_dict, flag)
    # # 规则4 抽到了三元组
    # if flag == 4:
    #     print("【RULE 4】", triple4)


# rule1: 语义角色标注结果A0 verb A1
def rule1(sentence, flag):
    # print("rule1 begin")
    rule1_triples = []
    # 语义角色标注结果集
    srl_results = srlProcess(sentence)
    # print(srl_results)
    # 遍历该句话的结果
    for srl_result in srl_results:
        # 谓词
        predicate = srl_result['predicate']
        # 该谓词对应的语义角色标注结果
        arguments = srl_result['arguments']
        # 创建语义角色依存字典，用于存储依存关系标签和它们对应的词
        dependencies = {}
        for label, word in arguments:
            dependencies[label] = word
        # 判断同时出现了'A0'和'A1'，即符合规则1
        if 'A0' in dependencies and 'A1' in dependencies:
            flag = 1
            triple = dependencies['A0'], predicate, dependencies['A1']
            rule1_triples.append(triple)
    # print(rule1_triples)
    # print("rule1 done")
    return flag, rule1_triples

# rule 2: 依存句法分析，SBV verb VOB
def rule2(cws_result, pos_result, dep_result, flag):
    # print(cws_result)
    # print(dep_result)
    # 存储抽取到的三元组
    rule2_triples = []
    # 创建字典，存储 verb 的依存句法分析结果
    dependency_dict = {}
    # 遍历句子中的每个词
    for i, word in enumerate(cws_result):
        if pos_result[i] == 'v':
            # 初始化一个空字典来存储指向该动词的分词的依存句法分析结果
            head_dependencies = {}

            # 存储当前动词指向的分词
            head_dependencies[cws_result[dep_result['head'][i]-1]] = dep_result['label'][i]

            # 查找所有head指向该动词的分词
            for j, head in enumerate(dep_result['head']):
                if head == i + 1:  # 注意：索引从0开始，需要加1
                    head_word = cws_result[j]
                    head_label = dep_result['label'][j]
                    head_dependencies[head_word] = head_label

            # 存储所有指向该动词的分词的依存句法分析结果
            dependency_dict[word] = head_dependencies
    # 遍历verb的依存句法分析结果字典，找SBV & VOB 共现
    for word, info in dependency_dict.items():
        # 检查是否同时出现"SBV"和"VOB"关系
        if "SBV" in info.values() and "VOB" in info.values():
            sbv_word = None
            vob_word = None
            # 找到对应的分词
            for dep_word, label in info.items():
                if label == "SBV":
                    sbv_word = dep_word
                elif label == "VOB":
                    vob_word = dep_word
            if sbv_word and vob_word:
                flag = 2
                triple = sbv_word, word, vob_word
                rule2_triples.append(triple)
                # print(triple)

    return flag, rule2_triples, dependency_dict

# rule 3: 依存句法分析， ATT verb VOB  不采用
def rule3(dependency_dict, flag):
    # 存储抽取的三元组
    rule3_triples = []
    # 遍历依存句法分析结果字典，找ATT & VOB 共现
    for word, info in dependency_dict.items():
        # 检查是否同时出现"ATT"和"VOB"关系
        if "ATT" in info.values() and "VOB" in info.values():
            att_word = None
            vob_word = None
            # 找到对应的分词
            for dep_word, label in info.items():
                if label == "ATT":
                    att_word = dep_word
                elif label == "VOB":
                    vob_word = dep_word
            if att_word and vob_word:
                flag = 3
                triple = att_word, word, vob_word
                rule3_triples.append(triple)
                # print(triple)
    return flag, rule3_triples

# rule 4: 依存句法分析，SBV verb+CMP POB
def rule4(dependency_dict, flag):
    pass

# rule 5: 依存句法分析，SBV-verb1 verb1-COO-verb2 verb2-VOB
def rule5(dependency_dict, flag):
    # 存储抽取的三元组
    rule5_triples = []

    # 遍历依存句法分析结果字典，找SBV-verb1 verb1-COO-verb2 verb2-VOB
    for word, info in dependency_dict.items():
        # 检查是否同时出现"SBV"和"COO"关系
        if "SBV" in info.values() and "COO" in info.values():
            sbv_word = None
            coo_word = None
            # 找到对应的分词
            for dep_word, label in info.items():
                if label == "SBV":
                    sbv_word = dep_word
                elif label == "COO":
                    coo_word = dep_word
            # 满足一个条件，找到了主谓
            if coo_word and sbv_word:
                # 检查是否verb2有VOB关系
                if coo_word in dependency_dict:
                    coo_verb_info = dependency_dict[coo_word]
                    if "VOB" in coo_verb_info.values():
                        vob_word = None
                        for dw, lb in coo_verb_info.items():
                            # 找到对应分词
                            if lb == "VOB":
                                vob_word = dw
                        # 满足两个条件，找到了主谓宾
                        if vob_word:
                            flag = 5
                            triple =sbv_word, coo_word, vob_word
                            rule5_triples.append(triple)

    return flag, rule5_triples

# rule 6: 依存句法分析， 单SBV/ VOB
def rule6(dependency_dict, flag):
    # 存储抽取的三元组
    rule6_triples = []

    # 遍历verb的依存句法分析结果字典，找SBV or VOB
    for word, info in dependency_dict.items():
        # 检查只出现"SBV"
        if "SBV" in info.values():
            sbv_word = None
            vob_word = None
            # 找到对应的分词
            for dep_word, label in info.items():
                if label == "SBV":
                    sbv_word = dep_word
            if sbv_word:
                flag = 6
                triple = sbv_word, word, vob_word
                rule6_triples.append(triple)

        # 检查只出现"VOB"
        elif "VOB" in info.values():
            sbv_word = None
            vob_word = None
            # 找到对应的分词
            for dep_word, label in info.items():
                if label == "VOB":
                    vob_word = dep_word
            if vob_word:
                flag = 6
                triple = sbv_word, word, vob_word
                rule6_triples.append(triple)

    return flag, rule6_triples


# 不做命名实体识别自定义字典、指代消解自定义字典的事件三元组抽取
def getTriple(inFile, outFile):
    # 存储inflie每个句子的抽取结果
    result = ""
    # 获得分句
    sentence_list = getSentence(inFile)
    for sentence in sentence_list:
        result += extraction(sentence)
    with open(outFile, 'w', encoding='utf-8') as f:
        f.write(result)





if __name__ == '__main__':
    ########################################
    # test part
    #
    # sentence = '太公去看刘媪，见到一条蛟龙在她身上，后来刘媪怀了孕，就生了高祖。'
    # sentence = '端午节传遍全国各地，主要分布于广大汉族地区'
    # sentence = '新年指夏历（农历）正月初一，是一年中最隆重的节日。'
    # sentence = '周武王逝世。'
    # sentence = '杀死比尔。'
    # test(sentence)
    # extraction(sentence)
    #
    # fileLoc = '/Users/tanyuyao/Desktop/draft/target.txt'
    # outLoc = '/Users/tanyuyao/Desktop/draft/output.txt'
    # getTriple_dry(fileLoc, outLoc)
    ########################################

    # ########################################
    # process part
    #
    # 获得目标文件名称
    # 统一读入文件的路径
    directory = '/Users/tanyuyao/Documents/PaperDocument/targetDoc'
    # 读入的文件
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    # 统一输出文件的路径
    out_dir = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Triple_clean'
    # 构建输出文件的路径
    for txt_file in txt_files:
        output_file = os.path.join(out_dir, os.path.basename(txt_file))
        print(txt_file, "PROCESSING")
        getTriple(txt_file, output_file)
        print(txt_file, "DONE")
    # ########################################