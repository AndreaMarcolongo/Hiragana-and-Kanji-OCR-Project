# Hiragana OCR Project

## Introduction
Repository for my handwritten hiragana recognition project.

To download the initial hiragana dataset go here: https://github.com/inoueMashuu/hiragana-dataset

Environment used to test the code: Python 3.9.13

## Description
Creation, training and evaluation of CNN model used to recognize handwritten hiragana charachters. 

Initial dataset specifics: 1000 images, 83x84 resolution

Augmented dataset specifics: 10000 images, 84x84 resolution, divided in 50 classes

## Project files
The repository is composed by 3 notebooks: Hiragana Dataset Augmentations, Label Dictionary, CNN Model
### Hiragana Dataset Augmentations
Code to perform the data augmentation on the initial hiragana dataset.
### Label Dictionary
Code to generate the dictionary for the labels.
### Label Dictionary
Notebook containing the CNN model. The model is trained and evaluated with the dataset created in the Hiragana Dataset Augmentations notebook.

## Instructions
1. Download the initial hiragana dataset

2. Create two folders: in the first one insert the initial hiragana dataset files, the second one will store the new dataset created by performing data augmentaion on the initial dataset.

3. Insert in 'Hiragana Dataset Augmentations' notebook the two folders' paths: the path of the folder containing the initial dataset in 'src_dir' and the other folder path in 'dst_dir'.

4. Run the notebooks in this order: Hiragana Dataset Augmentations --> Label Dictionary --> CNN Model.
