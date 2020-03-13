function [blurscore] = getBlurScore(website_path)
    blurscore = blurMetric(rgb2gray(imread(website_path)));