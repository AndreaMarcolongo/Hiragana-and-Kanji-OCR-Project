# Hiragana-and-Kanji-OCR-Project

Repository for my handwritten kanji and hiragana recognition project.

Per ora ho messo solo quello che ti ho detto ieri. Ogni giorno cercherò di aggiornare la repository con i nuovi progressi.

To download the hiragana dataset go here: https://github.com/inoueMashuu/hiragana-dataset

Aggiornamento 7 gennaio 2023:

1.Ho fatto l'upload di Last Hiragana e CNN che sono le ultime versioni prodotte. Ho alcuni dubbi sia riguardo il codice sia riguardo le performance della CNN. In ogni caso sono riuscito a fare data augmentation sul dataset iniziali così da ottenere un dataset di 2000 immagini. Con questo dataset le prestazioni (soprattutto della val_loss) sono migliorate, anche se ancora non so se sono soddisfacienti. Ci sono molti punti del codice da migliorare, soprattutto la parte in cui uso Tensorflow.

2. Ho caricato New CNN in cui credo di aver migliorato le prestazionima sembrano troppo buone per essere vere quindi aspetto di fare il check dello script insieme.

Aggiornamento 8 gennaio:

Credo di aver raggiunto un risultato soddifaciente per quanto riguarda l'OCR per hiragana. I notebook da guardare sono Last Hiragana Dataset(1) e Last CNN.
Per quanto riguarda l'OCR per i kanji, sto avendo molta difficoltà a maneggiare il dataset (non so se ti ricordi, ma in precedenza ti avevo detto di questo dataset molto grosso di cui dovevo fare richiesta da un sito di un ricercatore). In pratica è in un formato un po' particolare e bisogna fare una procedura per utilizzarlo e per ora non sono riuscito, quindi magari questa cosa la guardiamo insieme (la procedura sarebbe scritta qui https://github.com/choo/etlcdb-image-extractor). Alla prossima.
