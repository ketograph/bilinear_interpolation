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
