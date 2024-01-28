import PyPDF2
import os
import time

def merge_pdfs():
    front_path = input("请输入正面PDF文件的路径：")
    back_path = input("请输入反面PDF文件的路径：")

    front = PyPDF2.PdfFileReader(front_path)
    back = PyPDF2.PdfFileReader(back_path)
    output = PyPDF2.PdfFileWriter()

    min_pages = min(front.getNumPages(), back.getNumPages())

    # 先合并正反面页数相同的部分
    for i in range(min_pages):
        output.addPage(front.getPage(i))
        output.addPage(back.getPage(i))

    # 如果正面页数多，将多出来的正面页面添加到最后
    if front.getNumPages() > min_pages:
        for i in range(min_pages, front.getNumPages()):
            output.addPage(front.getPage(i))

    # 如果反面页数多，将多出来的反面页面添加到最后
    if back.getNumPages() > min_pages:
        for i in range(min_pages, back.getNumPages()):
            output.addPage(back.getPage(i))

    output_path = os.path.join(os.path.dirname(front_path), '输出.pdf')
    with open(output_path, 'wb') as f:
        output.write(f)

    print(f"合并完成，输出文件位于：{output_path}")
    
    time.sleep(5)

# 使用方法
merge_pdfs()

