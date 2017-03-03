# Image Rearranger

Arrange a mosaic by similarity. Inspired by [this collection](https://twitter.com/JUSTIN_CYR/status/829196024631681024) of pixel art by Justin Cyr.

## Installation and Usage

First, install numpy, scipy, sklearn, matplotlib, [pyLAPJV](https://x.st/code.html#pyLAPJV) using the requirements file:

```
$ pip install -r requirements.txt
```

Note that on MacOS you need to run some special commands to install Multicore-TSNE:

```
$ brew install gcc
$ export CC="/usr/local/Cellar/gcc/6.3.0/bin/gcc-6"
$ export CXX="/usr/local/Cellar/gcc/6.3.0/bin/gcc-6"
$ git clone https://github.com/DmitryUlyanov/Multicore-TSNE.git
$ cd Multicore-TSNE && python setup.py install
```

Then clone this repository and run the example:

```
$ git clone https://github.com/kylemcdonald/ImageRearranger.git
$ cd ImageRearranger
$ jupyter notebook
```