import pandas as pd
import os
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

def LabeledData():
    # 指定根目录
    root_directory = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData'

    # 获取根目录下所有子文件夹
    subdirectories = [d for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d))]

    # 遍历每个子文件夹
    for subdirectory in subdirectories:
        # 构建文件路径
        train_csv_path = os.path.join(root_directory, subdirectory, 'train.csv')
        test_csv_path = os.path.join(root_directory, subdirectory, 'test.csv')
        predicate_csv_path = os.path.join(root_directory, subdirectory, 'predicate.csv')

        # 读取CSV文件内容
        train_df = pd.read_csv(train_csv_path)
        test_df = pd.read_csv(test_csv_path)
        predicate_df = pd.read_csv(predicate_csv_path)

        # 提取'content'列和'label'列的内容
        content_series = pd.concat([train_df['content'], test_df['content'], predicate_df['content']],
                                   ignore_index=True)
        label_series = pd.concat([train_df['label'], test_df['label'], predicate_df['label']], ignore_index=True)

        # 将提取的内容添加到新的 DataFrame 中
        subdirectory_df = pd.DataFrame({'content': content_series, 'label': label_series})

        # 将当前子文件夹的数据保存为CSV文件，文件名与子文件夹相同
        output_csv_path = os.path.join(root_directory, subdirectory, f'{subdirectory}_merged.csv')
        subdirectory_df.to_csv(output_csv_path, index=False)

        print(f'Merged CSV saved to: {output_csv_path}')

if __name__ == '__main__':
    # completeModelData()
    LabeledData()