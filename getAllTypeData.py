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
    in_path = '/data/Event_final/gaozu.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/gaozu'
    getCSV(in_path, out_path)

def lvtaihou():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/lvtaihou.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/lvtaihou'
    getCSV(in_path, out_path)


def qinershi():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/qinshihuang_qinershi.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/qinershi'
    getCSV(in_path, out_path)

def qinshihuang():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/qinshihuang_qinshihuang.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/qinshihuang'
    getCSV(in_path, out_path)

def ziying():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/qinshihuang_ziying.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/ziying'
    getCSV(in_path, out_path)

def diku():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/wudi_diku.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/diku'
    getCSV(in_path, out_path)

def dishun():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/wudi_dishun.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/dishun'
    getCSV(in_path, out_path)

def diyao():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/wudi_diyao.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/diyao'
    getCSV(in_path, out_path)

def huangdi():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/wudi_huangdi.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/huangdi'
    getCSV(in_path, out_path)

def zhuanxu():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/wudi_zhuanxu.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/zhuanxu'
    getCSV(in_path, out_path)

def xiaqi():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xia_qi.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiaqi'
    getCSV(in_path, out_path)

def xiayu():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xia_yu.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiayu'
    getCSV(in_path, out_path)

def xiangyu():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xiangyu.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiangyu'
    getCSV(in_path, out_path)

def xiaojing():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xiaojing.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiaojing'
    getCSV(in_path, out_path)

def xiaowen():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xiaowen.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiaowen'
    getCSV(in_path, out_path)

def xiaowu():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/xiaowu.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/xiaowu'
    getCSV(in_path, out_path)

def yintang():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/yin_tang.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/yintang'
    getCSV(in_path, out_path)

def yinzhou():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/yin_zhou.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/yinzhou'
    getCSV(in_path, out_path)

def zhouwuwang():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/zhou_wuwang.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/zhouwuwang'
    getCSV(in_path, out_path)

def zhouyouwang():
    in_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Event_final/zhou_youwang.csv'
    out_path = '/Users/tanyuyao/Documents/pythonCode/kingFeatrue/ModelData/zhouyouwang'
    getCSV(in_path, out_path)


if __name__ == '__main__':
    gaozu()
    lvtaihou()
    qinershi()
    qinshihuang()
    ziying()
    diku()
    dishun()
    diyao()
    huangdi()
    zhuanxu()
    xiaqi()
    xiayu()
    xiangyu()
    xiaojing()
    xiaowen()
    xiaowu()
    yintang()
    yinzhou()
    zhouwuwang()
    zhouyouwang()

