## Faster RCNN
#### Ren, S., He, K., Girshick, R., & Sun, J. (2015). In Advances in neural information processing systems (pp. 91-99).

Faster RCNN is composed of two modules. The fist module is a deep fully convolutional network that proposes regions and the second module is the Fast RCNN detector that uses the proposed region.

To improve the bottleneck phenomenon in Fast RCNN, Faster RCNN proposed a new region proposal network. **Region Proposal Network (RPN)** is the keypoint in Faster RCNN.

![faster_rcnn](https://github.com/Oh-Yoojin/Object-detection/blob/master/Faster%20RCNN/pictures/faster_rcnn.png)

###### Region Propasal Network
The output of a region proposal network (RPN) is a bunch of boxes/proposals that will be examined by a classifier and regressor to eventually check the occurrence of objects.
A Region Proposal Network (RPN) takes an image (of any size) as input and outputs a set of rectangular object proposals, each with an objectness score. The ultimate goal of this model is to share computation with a Fast RCNN object detection network.

The RPN quickly and efficiently scans every location in order to assess whether further processing needs to be carried out in a given region. It does that by outputting k bounding box proposals each with 2 scores representing probability of object or not at each location.
The anchor boxes are just references, they are selected to have different aspect ratios and scales in order to accommodate different types of objects, elongated objects like buses, for example, cannot be properly represented by a square bounding box. In Faster R-CNN they used k = 9 representing 3 scales and 3 aspect ratios. Each regressor in the RPN only computes 4 offset values (w, h, x, y) to the corresponding reference anchor box.

* Use more 256 of 3*3 conv
* 1*1 classify layer and 1*1 regression layer for bounding box
* Classify object/non-object classification for each anchor box - 2k scores
* Refression for each bouncing box k - 4k coordinate

###### Anchor box

![anchor](https://github.com/Oh-Yoojin/Object-detection/blob/master/Faster%20RCNN/pictures/anchor.png)

At each sliding-window location, it simultaneously predicts multiple region proposals, where the number of maximum possible proposals for each location is denoted as k. So the reg layer has 4k outputs encoding the coordinates of k boxes, and the cls layer outputs 2k scores that estimate probability of object or not object for each proposal.
The anchor is k proposals parameterized relative to k reference boxes.

* scale (123*123, 256*256, 512*512)
* aspect rations (2:1, 1:1, 1:2)
* k = 9
