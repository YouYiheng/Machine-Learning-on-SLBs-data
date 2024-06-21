import glob
import pdfplumber
import re
import os

pdf_path = "SPO/"
pdfs = glob.glob("{}/*.pdf".format(pdf_path))
print(pdfs)

txt_path = "SPOTXT/"
if not os.path.exists(txt_path): os.mkdir(txt_path) #如果不存在，创建目录
count = 1

for p in pdfs: # p是遍历出来的每个PDF文件的路径
    filename = os.path.split(p)[1] # 切分出我们需要的文件名字
    print('现在开始第{}个文件{}'.format(count, filename))
    try:
        with pdfplumber.open(p) as pdf:
            for page in pdf.pages:
                txt = open('{}{}.txt'.format(txt_path,filename), mode='a',encoding='utf-8')
                content = page.extract_text()
                txt.write(content)
                txt.close()
    except:
        print('##########################')
        print('{}提取出现问题，已跳过'.format(filename))
    count += 1


def remove_newlines_from_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 去掉换行符
    content = content.replace('\n', ' ').replace('\r', '')

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_files_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):  # 只处理txt文件
                file_path = os.path.join(root, file)
                remove_newlines_from_file(file_path)
                print(f"Processed file: {file_path}")

# 调用函数，传入文件路径
process_files_in_directory('SPOTXT')