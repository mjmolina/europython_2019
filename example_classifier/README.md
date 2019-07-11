# PyTorch

Website: https://pytorch.org/

## Installation

`pip install pytorch`
also you will need to install Jupyter notebook
to open the files.

## Data

The data was downloaded from:
[kaggle: flowers-recognition](https://www.kaggle.com/alxmamaev/flowers-recognition)


## ML Model

The code comes from this nice [tutorial](https://towardsdatascience.com/how-to-train-an-image-classifier-in-pytorch-and-use-it-to-perform-basic-inference-on-single-images-99465a1e9bf5) from which I only change the input dataset.

You can check out this other tutorial for reference:
[an official PyTorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html).


The original unmodified notebooks can be found [here](https://github.com/cfotache/pytorch_imageclassifier).

## Image size

After unzipping the content of the data in a directory called flower,
execute the command:

```bash
for i in $(find . -type f -name *.jpg);do convert $i -resize 128x128\! $i $i;done
```

That will force all the images to be 128x128 without keeping the aspect
ratio.

## Files

* [Training](Training.ipynb): to train the model using a *resnet50* model.
* [Inference](Inference.ipynb): to use the results of the trained model.
