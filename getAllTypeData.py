import pandas as pd
from sklearn.model_selection import train_test_split
import os


def getCSV(in_path, out_path):
    # 读取原始CSV文件
    input_csv_path = in_path
    data = pd.read_csv(input_csv_path)

    # 划分数据集
    train_data, temp_data = train_test_split(data, test_size=0.4, random_state=42)
    test_data, predicate_data = train_test_split(temp_data, test_size=0.25, random_state=42)

    # 输出文件夹
    output_folder = out_path
    os.makedirs(output_folder, exist_ok=True)

    # 输出训练集、测试集和预测集到文件
    train_data.to_csv(os.path.join(output_folder, 'train.csv'), index=False)
    test_data.to_csv(os.path.join(output_folder, 'test.csv'), index=False)
    predicate_data.to_csv(os.path.join(output_folder, 'predicate.csv'), index=False)


def gaozu():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Triple_final/gaozu/data.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/gaozu'
    getCSV(in_path, out_path)

if __name__ == '__main__':
    gaozu()
