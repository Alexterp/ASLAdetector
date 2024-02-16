# **Welcome to ASL alphabet detector**


## **Table of contents**
1. [Abstract](#abstract)
2. [Description of repository](#description-of-repository)
   1. [Training package](#dor1)
   2. [Detector Package](#dor2)
3. [Requirements](#req)
4. [Inference](#infr)
   1. [Pipeline](#pipe)
   2. [Use](#use)
5. [Reference](#ref)
6. [Contact](#cont)


## **Abstract**

This project aims to train and deploy models for the detection of American Sign Language Alphabet letters based on hand landmarks predicted by MediaPipe.

<img src="[!demo](https://github.com/Alexterp/ASLAdetector/assets/61559126/2590d1e1-f742-4280-9612-d19a5d11ae33)" width="400" height="300">

Once an image is received from a live camera feed, MediaPipe predicts the coordinates of the key points of the hand, which are then fed into a custom dense neural network model. The model predicts the letter of the alphabet, which is then displayed on the screen.


## **Description of repository**
This repository is divided into two packages:


### 1. **training** contains: <a id="dor1"></a>
 - all necessary code to create, prepare and deploy the dataset
 - ipynb file for model training
 - trained models

### 2. **detector** contains: <a id="dor2"></a>
- the inference application real time detector and files. 

## **Requirements** <a id="req"></a>
This project was developed using Python 3.10.9 on Windows platform. Other libraries required are:

- mediapipe 0.9.1.0
- OpenCV 4.7.0
- tensorflow 2.11.0
- numpy 1.24.2
- pandas 1.5.3
- natsort 8.3.1
- Pillow 9.4.0
- protobuf 3.11 or later 


## **Inference** <a id="inf"></a>
- ### **Pipeline** <a id="pipe"></a>

<img src=".\img\aslaD_pipeline.png" >

- ### **Use** <a id="use"></a>
To run the inference application cd into project directory and run:

        python .\detector\asla_detector.py

The app will automatically use the webcam of your pc.

## **References** <a id="ref"></a>
- [MediaPipe](https://developers.google.com/mediapipe)

## **Contact** <a id="cont"></a>

**name:** Alex Terpinas

**email:**  alexterpns@gmail.com

## **License** <a id="lic"></a>
ASLAdetctor is under Apache License 2.0