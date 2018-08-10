from xml.etree.ElementTree import parse
import cv2
import numpy as np


def extract_box(path_dir):
    # bnd_box
    tree = parse(path_dir)
    obj = ['xmax', 'xmin', 'ymax', 'ymin']

    xmax = [int(x.text) for x in tree.findall('./object/bndbox/' + obj[0])]
    xmin = [int(x.text) for x in tree.findall('./object/bndbox/' + obj[1])]
    ymax = [int(x.text) for x in tree.findall('./object/bndbox/' + obj[2])]
    ymin = [int(x.text) for x in tree.findall('./object/bndbox/' + obj[3])]

    boundingbox = [[a, b, c, d] for a, b, c, d in zip(xmin, xmax, ymin, ymax)]

    bndbox_center = []
    for i in range(len(boundingbox)):
        x_center = (boundingbox[i][0] + boundingbox[i][1]) / 2
        y_center = (boundingbox[i][2] + boundingbox[i][3]) / 2
        bndbox_center.append({'box_{}_center'.format(i + 1): (x_center, y_center)})


    return xmin,xmax,ymin,ymax,bndbox_center




def image_triming(img_path,xmin,xmax,ymin,ymax,bndbox_center,folder):

    img = cv2.imread(img_path)
    width = int(img.shape[0])
    height = int(img.shape[1])

    new_bndbox = []
    for ii in range(len(bndbox_center)):
        x_center = list(bndbox_center[ii].values())[0][0]
        y_center = list(bndbox_center[ii].values())[0][1]

        for aa in range(9):
            st_w = int(x_center) - np.random.randint(300, 500)
            fi_w = int(x_center) + np.random.randint(300, 500)

            st_h = int(y_center) - np.random.randint(300, 400)
            fi_h = int(y_center) + np.random.randint(300, 400)

            if st_w > 0 and fi_w < width and st_h > 0 and fi_h < height:
                img_trim = img[st_h:fi_h, st_w:fi_w]
                cv2.imwrite('./{path}/{}/pic{}_({}).png'.format(folder,ii + 1, aa + 1), img_trim)

                new_xmin = xmin[ii] - st_w
                new_xmax = xmax[ii] - st_w
                new_ymin = ymin[ii] - st_h
                new_ymax = ymax[ii] - st_h

                new_bndbox.append({'pic{}_({})'.format(ii + 1, aa + 1): [new_xmin, new_xmax, new_ymin, new_ymax]})
    return new_bndbox



annotation_path = r"{path}.xml"
img_dir = r"{path}\safari.png"

xmin,xmax,ymin,ymax,center = extract_box(annotation_path)

new_bndbox = image_triming(img_dir,xmin,xmax,ymin,ymax,center,'sample')

