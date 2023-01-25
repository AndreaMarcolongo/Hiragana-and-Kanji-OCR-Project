# Hiragana OCR Project

## Introduction
Repository for my handwritten kanji and hiragana recognition project.

To download the hiragana dataset go here: https://github.com/inoueMashuu/hiragana-dataset

Environment used to test the code: Python 3.9.13

## Project files
The repository is composed by 3 notebooks: Hiragana Dataset Augmentations, Label Dictionary, CNN Model
### Hiragana Dataset Augmentations
Code to perform the data augmentation on the initial hiragana dataset.
### Label Dictionary
Code to generate the dictionary for the labels.
### Label Dictionary
Notebook containing the CNN model. The model is trained and evaluated with the dataset created in the Hiragana Dataset Augmentations notebook.

## Instructions

Il primo passo è quello di creare due cartelle. In una va inserito il dataset (scaricato dal link sopra) e nell'altra verrà inserito il dataset finale dopo l'esecuzione del notebook Hiragana Dataset Aumentation.

Il secondo passo è eseguire il notebook Hiragana Dataset Augmentation, che modifica il dataset iniziale con tecniche di data augmentation. Prima di eseguire il codice bisogna modificare le variabili contenenti i path in questo modo: in scr_dir inserire il path della cartella in cui è inserito il dataset iniziale, in destination e dst_dir inserire il path della cartella di destinazione del nuovo dataset.

Il terzo passo è eseguire il notebook CNN Model, che esegue il training e testa una CNN usando il dataset creato in precedenza. Prima di eseguire il codice modificare dataset_path con il path della cartella contenente il dataset finale.
