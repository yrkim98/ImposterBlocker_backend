function [score] = foundLogo(logo, siteSnap)
    logoWide = imread(logo);
    logoWide = rgb2gray(logoWide);

    site = imread(siteSnap);
    site = rgb2gray(site);

    points_logo = detectSURFFeatures(logoWide);
    points_site = detectSURFFeatures(site);

    [features_logo, valid_points_logo] = extractFeatures(logoWide, points_logo);
    [features_site, valid_points_site] = extractFeatures(site, points_site);

    indexPairs = matchFeatures(features_logo, features_site, 'MaxRatio', .9);

    matchedPoints1 = valid_points_logo(indexPairs(:,1),:);
    matchedPoints2 = valid_points_site(indexPairs(:,2),:);
    score = (size(indexPairs, 1) / 50) * 100;