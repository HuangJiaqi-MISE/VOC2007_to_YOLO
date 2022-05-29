# VOC数据集格式的转化（以VOC格式转化为YOLO为例）

在模式识别课程编程作业的第一部分中，我们使用了SSD作为口罩识别的深度学习训练网络。在进行训练前我们使用labelimg为每张图片标注标签，并将他们储存为VOC2007格式。

为了减少数据标注的工作量，在下面使用YOLO网络进行训练时可以将VOC格式的标注文件转化为YOLO格式。

由此，可以使用本代码仓库中的main.py文件对已有的VOC标注文件转化为YOLO格式。

```bash
Author：Huang Jiaqi
Created：2022-05-16
Last updated：2022-05-18
Function：用于VOC数据集XML文件的转化与预处理，使用该程序可以将VOC2007格式的标注文件转化为YOLO格式的标注文件。
```

