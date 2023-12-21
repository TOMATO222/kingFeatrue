import os
import pandas as pd
import re
import ast

def evaluateModel(resultcsv, modelcsv):
    # 从 albert-test-predicate.csv 中读取 'label' 列
    predicate_df = pd.read_csv(modelcsv)
    predicate_labels = predicate_df['label'].apply(ast.literal_eval).tolist()

    # 从 test_total.csv 中读取 'label' 列
    result_df = pd.read_csv(resultcsv)
    result_labels_tmp = result_df['label']
    result_labels = []
    for result_label in result_labels_tmp:
        result_label = result_label.split(',')
        result_labels.append(result_label)

    # 确保两个列表长度一致
    assert len(predicate_labels) == len(result_labels), "长度不一致，无法一一对应存储"

    # 一一对应存储
    label_mapping = list(zip(result_labels, predicate_labels))

    # 遍历计算指标
    TP = 0.0
    FP = 0.0
    TN = 0.0
    FN = 0.0
    for result_label, predicate_label in label_mapping:
        print(f"Result Label: {result_label}, Predicate Label: {predicate_label}")
        if '|' in result_label and not predicate_label:
            tni = 1.0
            tpi = 0.0
            fni = 0.0
            fpi = 0.0
            # 打印检查
            print("tpi: ", tpi, " tni:", tni, " fpi:", fpi, " fni:", fni)

        else:
            # 将列表转为集合
            result_set = set(result_label)
            predicate_set = set(predicate_label)

            # 算分母
            union_count = len(result_set.union(predicate_set))
            # print("分母：", union_count)

            # 计算重合元素个数:tpi 分子
            intersection_count = len(result_set.intersection(predicate_set))
            # print("计算重合元素个数:tpi分子", intersection_count)
            tpi = float(intersection_count)/float(union_count)

            # 计算集合 predicate_set 中有但集合 result_set 中没有的元素个数: fpi 分子
            exclusive_to_predicate = len(predicate_set.difference(result_set))
            # print("计算集合 predicate_set 中有但集合 result_set 中没有的元素个数:fpi分子", exclusive_to_predicate)
            fpi = float(exclusive_to_predicate)/float(union_count)

            # 计算集合 predicate_set 中有但集合 result_set 中没有的元素个数: fni 分子
            exclusive_to_result = len(result_set.difference(predicate_set))
            # print("计算集合 result_set 中有但集合 predicate_set 中没有的元素个数:fni分子", exclusive_to_result)
            fni = float(exclusive_to_result) / float(union_count)

            # 计算tni
            tni = 1.0 - float(fni) - float(tpi) - float(fpi)

            # 打印检查
            print("tpi: ", tpi, " tni:", tni, " fpi:", fpi, " fni:", fni)

        TP += tpi
        TN += tni
        FP += fpi
        FN += fni
    # print(TP, FP, FN, TN)
    Precision = float(TP)/(TP+FP)
    Recall = float(TP)/(TP+FN)
    F1 = float(2.0*Precision*Recall)/(Precision+Recall)
    print("Precision:", Precision, "Recall:", Recall, "F1:", F1)

if __name__ == '__main__':
    evaluateModel('/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/test_total.csv', '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelResults/s2s-test-predicate.csv')