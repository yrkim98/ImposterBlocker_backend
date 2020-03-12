function [blurscore] = getBlurScore(img)
    blurscore = blurMetric(rgb2gray(imread(img))) * 100;