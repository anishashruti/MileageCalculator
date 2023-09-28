# Mileage Calculator

This application takes 2 images of a car dashboard in the start and end of the trip
and using this image we can extract essential data to calculate the mileage of the car

My father has been collecting this data manually and maintaining in an excel so why not 
try to automate it.

## Phase 1

Just a mock app to get the inputs to calculate the mileage 
and just print it
<img title="phase 1" width="500" height="500" src="https://github.com/anishashruti/MileageCalculator/blob/master/window.PNG">

## Pre-processing image
I have taken one of the dashboard image 
<img title="dashboard" width="500" height="500"  src="https://github.com/anishashruti/MileageCalculator/blob/master/car_dashboard.jpg">

### First stage of preprocessing
1. Did some grayscalling and then found ROI
<img title="preprocess1"  width="500" height="500" src="https://github.com/anishashruti/MileageCalculator/blob/master/preprocess_1.PNG">

### Order of preprocessing:
1. original image
2. getting ROI
3. Thresholding
4. grayscale
   
<img title="preprocess2" width="500" height="500" src="https://github.com/anishashruti/MileageCalculator/blob/master/preprocess2.PNG">
