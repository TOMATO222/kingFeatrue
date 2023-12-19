from ltp import LTP
import os
import pandas as pd

# ltp = LTP()

# def SEG():
#     result = ltp.pipeline(["这样，就使君主失去了威严和尊贵。"], tasks=["cws", "pos"])
#     print(result.cws)
#     print(result.pos)
#
# def DP():
#     result = ltp.pipeline(["这样，就使君主失去了威严和尊贵。"], tasks=["cws", "dep"])
#     print(result.dep)
#
# def SRL():
#     result = ltp.pipeline(['这样，就使君主失去了威严和尊贵。'], tasks=["cws", "srl"])
#     print(result.srl)

def checkDataNum():
    totalTrain = 0
    # 定义文件夹路径
    folder_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData'

    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否为train.csv
            if file == 'train.csv':
                # 构建完整的文件路径
                file_path = os.path.join(root, file)

                # 读取CSV文件
                df = pd.read_csv(file_path)

                # 统计条数并输出
                print(f"{file_path}: {len(df)} 条数据")
                totalTrain += len(df)
    print("total train: ", totalTrain)

    totalTest = 0
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否为train.csv
            if file == 'test.csv':
                # 构建完整的文件路径
                file_path = os.path.join(root, file)

                # 读取CSV文件
                df = pd.read_csv(file_path)

                # 统计条数并输出
                print(f"{file_path}: {len(df)} 条数据")
                totalTest += len(df)
    print("total test: ", totalTest)

def completeModelData():
    # 定义文件夹路径
    folder_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData'
    output_train_file_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/train_total.csv'
    output_test_file_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/test_total.csv'
    output_predicate_file_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/predicate_total.csv'

    # train.csv
    totalTrain = 0
    # 初始化一个空的 DataFrame
    combined_df_train = pd.DataFrame(columns=['content', 'label'])

    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否为train.csv
            if file == 'train.csv':
                # 构建完整的文件路径
                file_path = os.path.join(root, file)

                # 读取CSV文件
                df = pd.read_csv(file_path)

                # 统计条数
                totalTrain += len(df)
                # 合并到总的 DataFrame
                combined_df_train = pd.concat([combined_df_train, df[['content', 'label']]], ignore_index=True)
    print("total train: ", totalTrain)
    # 将合并后的数据保存到新文件中
    combined_df_train.to_csv(output_train_file_path, index=False)

    # test.csv
    totalTest = 0
    # 初始化一个空的 DataFrame
    combined_df_test = pd.DataFrame(columns=['content', 'label'])
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否为train.csv
            if file == 'test.csv':
                # 构建完整的文件路径
                file_path = os.path.join(root, file)

                # 读取CSV文件
                df = pd.read_csv(file_path)

                # 统计条数
                totalTest += len(df)
                # 合并到总的 DataFrame
                combined_df_test = pd.concat([combined_df_test, df[['content', 'label']]], ignore_index=True)
    print("total test: ", totalTest)
    # 将合并后的数据保存到新文件中
    combined_df_test.to_csv(output_test_file_path, index=False)

    # predicate.csv
    totalPredicate = 0
    # 初始化一个空的 DataFrame
    combined_df_predicate = pd.DataFrame(columns=['content', 'label'])
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否为train.csv
            if file == 'predicate.csv':
                # 构建完整的文件路径
                file_path = os.path.join(root, file)

                # 读取CSV文件
                df = pd.read_csv(file_path)

                # 统计条数
                totalPredicate += len(df)
                # 合并到总的 DataFrame
                combined_df_predicate = pd.concat([combined_df_predicate, df[['content', 'label']]], ignore_index=True)
    print("total predicate: ", totalPredicate)
    # 将合并后的数据保存到新文件中
    combined_df_predicate.to_csv(output_predicate_file_path, index=False)

if __name__ == '__main__':
    # SEG()
    # DP()
    # SRL()
    # checkDataNum()
    completeModelData()