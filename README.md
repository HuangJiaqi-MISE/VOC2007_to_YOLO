# Conversion of VOC dataset format (VOC format to YOLO as an example)

In the first part of the programming assignment for the pattern recognition course, we used SSD as a deep learning training network for mask recognition. We used labelimg to label each image and stored them in VOC2007 format before conducting the training.

To reduce the amount of data annotation, the annotation files in VOC format can be converted to YOLO format for the following training using the YOLO network.

As a result, the existing VOC annotation files can be converted to YOLO format using the main.py file in this code repository.

```bash
Author：Huang Jiaqi
Created: 2022-05-16
Last updated: 2022-05-18
Function：For converting and pre-processing VOC dataset XML files, use this program to convert VOC 2007 format annotation files into YOLO format annotation files.
```
