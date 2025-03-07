import win32com
from win32com.client import Dispatch, constants
from conf import conf

ppt = win32com.client.Dispatch('PowerPoint.Application')
ppt.Visible = 1
pptSel = ppt.Presentations.Open(conf.path_temp["模板2"])
# pptSel = ppt.Presentations.Open(r"D:\PythonProjects\PPT\file\ppt_save\资产设备管理系统20191029.pptx")

win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
# #get the ppt's pages

slide_count = pptSel.Slides.Count

# 目录页由模板指定 不需要再更改
# tempPPT.Slides(2).Shapes(1).TextFrame.TextRange.Text="目录测试1\n目录测试2"

# 修改标题,Title不一定每页都有
# tempPPT.Slides(4).Shapes.Title.TextFrame.TextRange.Text = "子页标题"
# print(tempPPT.Slides(4).Shapes.Title.TextFrame.TextRange.Text)

# 查找一页并且复制
# tempPPT.Slides.FindBySlideID(270).Copy()
# 粘贴到指定index之前,不写则追加到最后
# tempPPT.Slides.Paste(5)

# for i in range(5, slide_count + 1):
for i in range(9, 10):
    slide = pptSel.Slides(i)
    shape_count = slide.Shapes.Count
    print(i, "页")

    # print(slide.Shapes.Title.TextFrame.TextRange.Text)

    for j in range(1, shape_count + 1):
        if slide.Shapes(j).HasTextFrame:
            # 每一个内容   类型14 大标题
            s = slide.Shapes(j).TextFrame.TextRange.Text
            print(" ",j, slide.Shapes(j).Type, s)
    print("\n")
# ppt.Quit()
