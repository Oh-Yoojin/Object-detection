## Fast Region-based Convolutional Network (Fast R-CNN)
#### Girshick, R. (2015). Fast r-cnn. In Proceedings of the IEEE international conference on computer vision (pp. 1440-1448).

R-CNN needs many proposals to be accurate and many regions overlap with each other. The big problems of R-CNN is slow in training and inference. Because if we have 2,000 proposals, each of them is processed by a CNN separately, we repeat feature extractions 2,000 times.

Fast R-CNN is to reduce the time consumption related to the high number of models necessary to anlyse all region proposals. So It adopts **Regions of Interest (RoI) Pooling**.

##### Fast R-CNN Architecture

![fast_rcnn_archi](https://github.com/Oh-Yoojin/Object-detection/blob/master/Fast%20RCNN/pictures/fast_rcnn_archi.png)

Fast R-CNN also uses a selective search to find its initial RoI. However, do not convert each RoI every time, **convert the entire image only once**. It warps the region proposals to a fixed size using ROI pooling and feed them to fully connected layers for classification and localization (detecting the location of the object). This is the big changes compared with R-CNN.

##### RoI pooling
In Fast R-CNN uses RoI pooling to warp the variable size RoIs into in a predefined size shape.

![pooling](https://github.com/Oh-Yoojin/Object-detection/blob/master/Fast%20RCNN/pictures/pooling.png)

Region of interest pooling is a neural-net layer used for object detection tasks. It maintains a high detection accuracy. The layer takes two inputs.
1) A fixed-size feature map obtained from a deep convolutional network with several convolutions and max pooling layers.
2) An N x 5 matrix of representing a list of regions of interest, where N is a number of RoIs. The first column represents the image index and the remaining four are the coordinates of the top left and bottom right corners of the region.

For every region of interest from the input list, it takes a section of the input feature map that corresponds to it and scales it to some pre-defined size.

* The keypoint of RoI Pooling
  * It allows us to reuse the feature map from the convolutional network.
  * It can significantly speed up both train and test time.
  * It allows to train object detection systems in an end-to-end manner.

