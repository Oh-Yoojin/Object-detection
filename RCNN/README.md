## Region-based Convolutional Network (R-CNN)
#### Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2016). Region-based convolutional networks for accurate object detection and segmentation. IEEE transactions on pattern analysis and machine intelligence, 38(1), 142-158.

R-CNN is the first study to apply CNN to object detection.
The goal of R-CNN is to take in an image, and correctly identify where the main objects (via a bounding box) in the image.

But how does it find out where these bounding boxes are? **It propose a bunch of boxes in the image and see if any of them actually correspond to an object.**

R-CNN create these bounding boxes or region proposals using **selective search** method developed by J.R.R. Uijlings and al.(2012). It initializes small regions in an image and merges them with a hierarchical grouping. Thus the final group is a box containing the entire image.

##### R-CNN Architecture

![rcnn_architecture](https://github.com/Oh-Yoojin/Object-detection/blob/master/RCNN/pictures/rcnn_architecture.png)

The above picture is the most famous picture explaning the **concept of R-CNN.**

![rcnn_architecture2](https://github.com/Oh-Yoojin/Object-detection/blob/master/RCNN/pictures/rcnn_architecture2.png)

As you go through the figure,
  1. Generate a set of proposals for bounding boxes.
  2. Run the images in the bounding boxes through a pre-trained AlexNet and finally an SVM to see what object the image in the box is.
  3. Run the box through a linear regression model to output tighter coordinates for the object has been classified.

###### Key point
* The First object detection method Using CNN
* Region proposal + CNN
* Use selectie search method to obtain the region proposal 
* Calculate each proposal independently; requires more calcuations
In this paper, there are 2000 region proposals. So it conducts 2000 times of CNN. It requires a more calculations and time.
* Increased detection accuracy with bounding box regression

###### Problem
* Test time is too slow.
  * Recalculation of all CNN paths for all region proposals
  * 13 seconds per sheet on GPU(K40)
  * 53 seconds per sheet on CPU
