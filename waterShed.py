# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:28:43 2019

@author: alexa
"""

import SimpleITK as sitk
import matplotlib.image as mpimg
import numpy as np
import sys

inputFile = sys.argv[1]
outFile = sys.argv[2]+"/Out/waterShed.jpg"

img = sitk.ReadImage(inputFile)

mpimg.imsave(sys.argv[2]+"/Out/tempws.jpg", np.squeeze(sitk.GetArrayFromImage(img)), cmap="gray")

temp_img = sitk.ReadImage(sys.argv[2]+"/Out/tempws.jpg")

img = sitk.VectorIndexSelectionCast(temp_img,1)

feature_img = sitk.GradientMagnitudeRecursiveGaussian(img, sigma=2)

ws_img = sitk.MorphologicalWatershed(feature_img, level=2, markWatershedLine=True, fullyConnected=False)

#seg = sitk.ConnectedComponent(ws_img!=ws_img[0,256])
final_img = sitk.LabelOverlay(img, ws_img)
mpimg.imsave(outFile, np.squeeze(sitk.GetArrayFromImage(final_img)))