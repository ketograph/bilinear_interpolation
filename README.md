# Bilinear interpolation

This is an simple implementation of the bilinear interpolation for educational purposes.

Around one pixel to interpolate (`p`) are four pixels `p1, p2, p3, p3`. The pixel value `p` can be calculated in two steps:
1. interpolate `p1` and `p2` as well as `p3` and `p4` to get the intermediate pixels `p'` and `p''`
2. interpolate `p'` and `p''`

```
  |            |
-p1---p'------p2--
  |            |  
  |            |
  |---p        |
  |   |        |
-p3---p'' ----p4--
  |            |
```

An example is given at [Wikipedia](https://en.wikipedia.org/wiki/Bilinear_interpolation#Application_in_image_processing):

![Example for bilinear interpolation](https://upload.wikimedia.org/wikipedia/commons/a/a7/Bilin3.png)
