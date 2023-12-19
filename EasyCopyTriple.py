import re
def process(file_path):
    # 打开文件
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件内容
        lines = file.readlines()
    id = 1
    # 处理每一行
    for line in lines:
        # 如果行的开头是"【"
        if line.startswith("【"):
            # 使用正则表达式清除非中文字符
            cleaned_text = re.sub('[^\u4e00-\u9fa5]', '', line)

            # 输出结果
            print(cleaned_text)
        else:
            # 如果行的开头不是"【"，直接输出原行
            # print(line.strip())
            id += 1

if __name__ == '__main__':
    process('/Users/tanyuyao/Documents/pythonCode/kingFeatrue/data/Triple_final/qinshihuang/ziying.txt')