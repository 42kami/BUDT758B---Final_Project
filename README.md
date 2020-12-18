# BUDT758B---Final_Project
# Real Face Image to Anime Style Translation Using CycleGAN

## Intro:
    This is an individual work for course BUDT758B's final project contributed by Chongwen Sun. Basically, it focuses on implementing cycleGAN method on converting real face images to anime style images.

## Content of this repo:

## How to run:
### neural-style-transfer train: 
python neural-style-transfer/neural_style.py train --dataset 'your dataset location' --style-image 'yourlocation' --save-model-dir 'your model location' --epochs 100 --cuda 1
### neural-style-transfer test: 
python neural-style-transfer/neural_style.py eval --content-image 'your style image location'  --model 'your model location'  --output-folder 'your output folder' --cuda 1
### cyclegan train:
python cyclegan/train.py --dataroot 'your datasets' --name cyclegan --model cycle_gan
### cyclegan test:
python cyclegan/test.py --dataroot 'your datasets' --name cyclegan --model cycle_gan
