# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# -*- coding:utf-8 -*-
# 作者：黄家琦
# 创建：2022-05-09
# 更新：2022-05-21
# 用意：用于VOC数据集XML文件的转化与预处理，使用该程序可以将VOC2007格式的标注文件转化为YOLO格式的标注文件。

import os
import shutil
import cv2
from lxml import etree


def VOCtoYolo(class_num, voc_img_path, voc_xml_path, yolo_txt_save_path, yolo_img_save_path=None):
    xmls = os.listdir(voc_xml_path)
    xmls = [x for x in xmls if x.endswith('.xml')]
    if yolo_img_save_path is not None:
        if not os.path.exists(yolo_img_save_path):
            os.mkdir(yolo_img_save_path)
    if not os.path.exists(yolo_txt_save_path):
        os.mkdir(yolo_txt_save_path)
    all_xmls = len(xmls)
    for idx, one_xml in enumerate(xmls):
        xl = etree.parse(os.path.join(voc_xml_path, one_xml))
        root = xl.getroot()
        objects = root.findall('object')
        img_size = root.find('size')
        img_w = 0
        img_h = 0
        if img_size:
            img_width = img_size.find('width')
            if img_width is not None:
                img_w = int(img_width.text)
            img_height = img_size.find('height')
            if img_height is not None:
                img_h = int(img_height.text)
        label_lines = []
        for ob in objects:
            one_annotation = {}
            label = ob.find('name').text
            one_annotation['tag'] = label
            one_annotation['flag'] = False
            bbox = ob.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)
            if img_w == 0 or img_h == 0:
                img = cv2.imread(os.path.join(voc_img_path, one_xml.replace('.xml', '.jpg')))
                img_h, img_w = img.shape[:2]
            bbox_w = (xmax - xmin) / img_w
            bbox_h = (ymax - ymin) / img_h
            bbox_cx = (xmin + xmax) / 2 / img_w
            bbox_cy = (ymin + ymax) / 2 / img_h
            try:
                bbox_label = class_num[label]
                label_lines.append(f'{bbox_label} {bbox_cx} {bbox_cy} {bbox_w} {bbox_h}' + '\n')
            except Exception as e:
                print("not find number label in class_num ", e, one_xml)
                label_lines = []
                break
        if len(label_lines):
            with open(os.path.join(yolo_txt_save_path, one_xml.replace('.xml', '.txt')), 'w') as fp:
                fp.writelines(label_lines)
            if yolo_img_save_path is not None:
                shutil.copy(os.path.join(voc_img_path, one_xml.replace('.xml', '.jpg')),
                            os.path.join(yolo_img_save_path))
        print(f"processing: {idx}/{all_xmls}")


if __name__ == '__main__':
    VOCtoYolo(
        class_num={'unmask': 0, 'mask': 1},  # 标签种类
        voc_img_path=r'C:\Users\HUANG JIAQI\Desktop\YOLO_Mask\score\images\train', # 数据集图片文件夹存储路径
        voc_xml_path=r'C:\Users\HUANG JIAQI\Desktop\YOLO_Mask\score\labels\train_VOC', # 标签xml文件夹存储路径
        yolo_txt_save_path=r'C:\Users\HUANG JIAQI\Desktop\YOLO_Mask\score\labels\train' # 将要生成的txt文件夹存储路径
    )

