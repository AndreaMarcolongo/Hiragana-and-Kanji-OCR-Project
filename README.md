# Hiragana-and-Kanji-OCR-Project

Repository for my handwritten kanji and hiragana recognition project.

To download the hiragana dataset go here: https://github.com/inoueMashuu/hiragana-dataset

Environment used to test the code: Python 3.9.13


Il primo passo è quello di creare due cartelle. In una va inserito il dataset (scaricato dal link sopra) e nell'altra verrà inserito il dataset finale dopo l'esecuzione del notebook Hiragana Dataset Aumentation.

Il secondo passo è eseguire il notebook Hiragana Dataset Augmentation, che modifica il dataset iniziale con tecniche di data augmentation. Prima di eseguire il codice bisogna modificare le variabili contenenti i path in questo modo: in scr_dir inserire il path della cartella in cui è inserito il dataset iniziale, in destination e dst_dir inserire il path della cartella di destinazione del nuovo dataset.

Il terzo passo è eseguire il notebook CNN Model, che esegue il training e testa una CNN usando il dataset creato in precedenza. Prima di eseguire il codice modificare dataset_path con il path della cartella contenente il dataset finale.
