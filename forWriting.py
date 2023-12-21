from ltp import LTP
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

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



def drawLoss():
    # 读取日志文件
    with open('/Users/tanyuyao/Documents/pythonCode/kingFeatrue/Albert训练打印.txt', 'r') as file:
        log_content = file.read()

    # 使用正则表达式提取时间、Epoch、Batch number、Loss、Accuracy
    pattern = r'Time:(.*?), Epoch:(\d+), Batch number:(\d+)/\d+, Loss:([\d.]+)'

    matches = re.findall(pattern, log_content)

    # 提取数据
    times = [match[0] for match in matches]
    epochs = [int(match[1]) for match in matches]
    batch_numbers = [int(match[2]) for match in matches]
    loss_values = [float(match[3]) for match in matches]
    # accuracy_values = [float(match[4]) for match in matches]

    # 绘制曲线图
    plt.figure(figsize=(12, 6))

    # 绘制 Loss 曲线
    plt.subplot(2, 1, 1)
    plt.plot(loss_values, label='Loss', color='blue')
    plt.title('Loss Over Time')
    plt.xlabel('Batch Number')
    plt.ylabel('Loss')
    plt.legend()

    # 绘制 Accuracy 曲线
    # plt.subplot(2, 1, 2)
    # plt.plot(accuracy_values, label='Accuracy', color='green')
    # plt.title('Accuracy Over Time')
    # plt.xlabel('Batch Number')
    # plt.ylabel('Accuracy')
    # plt.legend()

    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    # SEG()
    # DP()
    # SRL()
    # checkDataNum()
    # completeModelData()
    drawLoss()