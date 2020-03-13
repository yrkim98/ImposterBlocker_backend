function [a] = savepic(image)
    a = "done"
    imwrite(image, 'testingpic.png')
    return
end