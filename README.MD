# Image out painting using keras
Implementation based on ![repo](https://github.com/bendangnuksung/Image-OutPainting)

The model for trained on kaggle GPU kernel for 300 epochs

### Requirements (tested on)

- tensorflow==1.8.0
- opencv-python==3.4.0.12
- Keras==2.1.6
- keras-contrib==2.0.8
- Pillow==4.4.0
- numpy==1.14.0

### Get Started
1. Prepare data:
	run `prepare_data.ipynb`

2. Build Model:
	run `OutPaint.ipynb`

### Note
- Data is not generalized since in some of the images the missing parts lack relation with the maksed part. Can be improved by changing `MASK_PERCENTAGE` in code but will also need to change the `img_size = 256`
- Hence, after many epochs it tends to overfit as we see that model learns those representations which it should not like hills in below image which is missing in case of masked image.


![](data/cdmc848.jpg)
