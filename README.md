# Hiragana OCR Project

## Introduction
Repository for my handwritten hiragana recognition project.

To download the initial hiragana dataset: https://github.com/inoueMashuu/hiragana-dataset

Environment used to test the code: Python 3.9.13

## Description
Creation, training and evaluation of CNN model used to recognize handwritten hiragana characters (46 base characters + 4 with dakuten).


Initial dataset: 1000 images, 83x84 resolution

<img src="[https://user-images.githubusercontent.com/16319829/81180309-2b51f000-8fee-11ea-8a78-ddfe8c3412a7.png](https://github.com/AndreaMarcolongo/Hiragana-and-Kanji-OCR-Project/blob/main/Description%20images/orig_img.jpg)" width=50% height=50%>

Augmented dataset: 10000 images, 84x84 resolution, divided in 50 classes

![alt text](https://github.com/AndreaMarcolongo/Hiragana-and-Kanji-OCR-Project/blob/main/Description%20images/aug_img.jpg)

## Project files
The rproject is composed of 3 notebooks: Hiragana Dataset Augmentations, Label Dictionary, CNN Model
### Hiragana Dataset Augmentations
Code to perform the data augmentation on the initial hiragana dataset.
### Label Dictionary
Code to generate the dictionary for the labels.
### CNN Model
Notebook containing the CNN model. The model is trained and evaluated using the dataset created in the Hiragana Dataset Augmentations notebook.

## Instructions
1. Download the initial hiragana dataset

2. Create two folders: in the first one insert the initial hiragana dataset files, the second one will store the new dataset created by performing data augmentaion on the initial dataset.

3. Insert the two folders' paths in 'Hiragana Dataset Augmentations' notebook: the path of the folder containing the initial dataset in 'src_dir' and the other folder path in 'dst_dir'.

4. Run the notebooks in this order: Hiragana Dataset Augmentations --> Label Dictionary --> CNN Model.

## Conclusions

These are the performance obtained by the model on the augmented dataset:

| | Training set | Validation set | Test set |
| ------------- | ------------- |-------------- | -------- |
| `Accuracy`  | 1.0000  | 0.9945 | 0.9929 |
| `Loss`  | 0.0015  | 0.0223 | 0.0236 |
| `F1 Score` | X | X | 0.9930 |

Confusion matrix:

![alt text](https://github.com/AndreaMarcolongo/Hiragana-and-Kanji-OCR-Project/blob/main/Description%20images/confusion%20matrix.jpg)

Prediction confidence:

![alt text](https://github.com/AndreaMarcolongo/Hiragana-and-Kanji-OCR-Project/blob/main/Description%20images/prediction%20confidence.jpg)
