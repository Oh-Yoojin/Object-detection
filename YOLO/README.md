## You Only Look Once: Unified, real-time object detection
### Proceedings of the IEEE conference on computer vision and pattern recognition. 2016. p. 779-788.

##### Real-time image bounding box detection
##### Accessing Object detection as a regression issue, it is possible to predict where the objects are located from the entire image at once, without need for a separate reconstruction profile
* In RCNN models, the multi-step method of finding the bounding box and performing the classification/regression for each bounding box.
* Perform both regression and detection score (too slow)

![compare](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/01.png)
##### YOLO is more faster but less accurate.

#### YOLO detection system
![system](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/00.png)

Predict objects and location at once.
* Pros
  * Very fast with simple processing
  * Background error (False positives) is low
  * Learn more generalized features about objects

* Cons
  * Relatively low accuracy(especially for small objects)

#### Unified Detection
![structure](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/02.png)

- Devide input image by 𝐒 × 𝐒 grid.
- Each grid cell detects object, grid cell preicts confidence score about B bounding boxes.
  * Score reflects how much object is included in the box and the accuracy of the prediction.
  * Confidence Score: 𝑷𝒓⁡(𝒐𝒃𝒋𝒆𝒄𝒕)∗〖𝑰𝑶𝑼〗(if there is no object, confidence socre is 0)

- Each bounding box consists of 5 prediction values; (x, y, w, h, confidence)
  * (x, y) is the center of the box based on the grid cell.
  * Confidence is an IOU between the predicted box and all ground truth boxes.

- Each grid cell has conditional class probability(C)
  * Conditional Class Probability: 𝑷𝒓⁡(𝑪𝒍𝒂𝒔𝒔 𝒊|𝑶𝒃𝒋𝒆𝒄𝒕)
- 𝐂𝐥𝐬𝐬𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜𝐂𝐨𝐧𝐟𝐢𝐝𝐞𝐧𝐜𝐞𝐒𝐜𝐨𝐫𝐞 =  𝑷𝒓⁡(𝑪𝒍𝒂𝒔𝒔 𝒊|𝑶𝒃𝒋𝒆𝒄𝒕) ∗ 𝑷𝒓⁡(𝑶𝒃𝒋𝒆𝒄𝒕) ∗〖𝑰𝑶𝑼〗=𝑷𝒓⁡(𝑪𝒍𝒂𝒔𝒔 𝒊) ∗〖𝑰𝑶𝑼〗

#### Network design
![network](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/03.png)

It is designed based on GoogleNet model.

Convolutional layer : 24, Fully connected layer : 2, Final output : 7 * 7 * 30 tensor


- Process

![pic1](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/04.png)
![pic2](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/05.png)


#### Loss function
![loss](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/06.png)


#### Experiments (compare detection system)
![pic3](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/07.png)

- Fast YOLO is the fastest detector.
- YOLO and Faster RCNN is similar levels of MAP.
- Using Fast RCNN and YOLO together can complement background error problems.


![pic4](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/08.png)
- The percentage of localization in the top is YOLO and background errors in the top is Fast RCNN.


![pci5](https://github.com/Oh-Yoojin/Object-detection/blob/master/YOLO/images/09.png)
