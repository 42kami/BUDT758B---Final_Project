# Neural-Style-Transfer

Code forked from [fast-neural-style](https://github.com/pytorch/examples/tree/master/fast_neural_style)

## Training

```python
python neural_style/neural_style.py train --dataset </path/to/celebA/images> \
--style-image </path/to/manga/image> --save-model-dir </path/to/save-model/folder> 
--epochs 100 --cuda 1
```

## Evaluation
```python
python neural_style.py eval --content-image </path/to/celebA/image> \
--model </path/to/save-model/folder>  --output-folder </path/to/output/folder> --cuda 1
```