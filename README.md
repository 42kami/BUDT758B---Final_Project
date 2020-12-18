# BUDT758B---Final_Project
# Real Face Image to Anime Style Translation Using CycleGAN

## Intro:
This is an individual work for course BUDT758B's final project contributed by Chongwen Sun. Basically, it focuses on implementing cycleGAN method on converting real face images to anime style images.

## Content of this repo:

## How to run:
### Data processing
Use image_format_process.py to resize and crop your images

### neural-style-transfer train: 
    python neural-style-transfer/neural_style.py train --dataset 'your dataset location' --style-image 'yourlocation' --save-model-dir 'your model location' --epochs 100 --cuda 1
### neural-style-transfer test: 
    python neural-style-transfer/neural_style.py eval --content-image 'your style image location'  --model 'your model location'  --output-folder 'your output folder' --cuda 1
### cyclegan train:
    python cyclegan/train.py --dataroot 'your datasets' --name cyclegan --model cycle_gan
### cyclegan test:
    python cyclegan/test.py --dataroot 'your datasets' --name cyclegan --model cycle_gan

## Models
### The neural-style-transfer model 
The neural-style-transfer model is forked from https://github.com/floydhub/fast-neural-style
### The cyclegan model 
The cyclegan model is forked from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

## Datasets
### Training dataset 
The training dataset is a subset of the Anime-Face-Dataset: https://github.com/bchao1/Anime-Face-Dataset
### Testing dataset
The testing dataset is a subset of the Large-scale CelebFaces Attributes (CelebA) Dataset: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
