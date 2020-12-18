#!/bin/bash

for i in `seq 1 1 9`
do
    echo ${i}
    python neural_style.py eval --content-image ../../preprocessed/CelebA-copy/img/00000${i}.jpg --model saved-model/Celeb-to-manga/epoch_100_Mon_Nov__5_18\:13\:07_2018_100000.0_10000000000.0.model --output-folder ./output/ --cuda 1
done

for i in `seq 10 1 99`
do
    echo ${i}
    python neural_style.py eval --content-image ../../preprocessed/CelebA-copy/img/0000${i}.jpg --model saved-model/Celeb-to-manga/epoch_100_Mon_Nov__5_18\:13\:07_2018_100000.0_10000000000.0.model --output-folder ./output/ --cuda 1
done

echo "100"
python neural_style.py eval --content-image ../../preprocessed/CelebA-copy/img/000100.jpg --model saved-model/Celeb-to-manga/epoch_100_Mon_Nov__5_18\:13\:07_2018_100000.0_10000000000.0.model --output-folder ./output/ --cuda 1

