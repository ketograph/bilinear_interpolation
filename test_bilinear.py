#!/usr/bin env python3
# coding=utf-8

import unittest
import numpy as np
import cv2
from bilinear import bilinear_interpolation, interpolate, get_array_value


class TestBilinearInterpolation(unittest.TestCase):
    def setUp(self):
        """Setting up image."""
        self.image = np.arange(0, 9).reshape(3, 3)

    def test_no_interpolation(self):
        """Test that no scaling produces no effect."""
        self.assertEqual(bilinear_interpolation(0, 0, self.image), 0)
        self.assertEqual(bilinear_interpolation(1, 1, self.image), 4)
        self.assertEqual(bilinear_interpolation(2, 2, self.image), 8)

    def test_interpolation_x_direction(self):
        """Test interpolation in x-direction."""
        self.assertEqual(bilinear_interpolation(0.5, 0, self.image), 0.5)
        self.assertEqual(bilinear_interpolation(1.4, 0, self.image), 1.4)
        self.assertEqual(bilinear_interpolation(0.5, 2, self.image), 6.5)
        self.assertEqual(bilinear_interpolation(1.4, 2, self.image), 7.4)

    def test_interpolation_y_direction(self):
        """Test interpolation in y-direction."""
        self.assertEqual(bilinear_interpolation(0, 0.5, self.image), 1.5)
        self.assertEqual(bilinear_interpolation(0, 1.5, self.image), 4.5)
        self.assertEqual(bilinear_interpolation(2, 0.6, self.image), 3.8)
        self.assertEqual(bilinear_interpolation(2, 1.5, self.image), 6.5)

    def test_interpolation_x_y_direction(self):
        """Test interpolation in x- and y-direction."""
        self.assertEqual(bilinear_interpolation(0.5, 0.5, self.image), 2)
        self.assertEqual(bilinear_interpolation(1.5, 0.5, self.image), 3)
        self.assertEqual(bilinear_interpolation(0.5, 1.5, self.image), 5)
        self.assertEqual(bilinear_interpolation(1.5, 1.5, self.image), 6)

        self.assertAlmostEqual(bilinear_interpolation(0.1, 0.1, self.image), 0.4)
        self.assertEqual(bilinear_interpolation(1.9, 1.9, self.image), 7.6)

    def test_interpolation_error_negativ(self):
        """Test if errors are properly raised."""
        with self.assertRaises(ValueError):
            bilinear_interpolation(-1, 0, self.image)
        with self.assertRaises(ValueError):
            bilinear_interpolation(0, -1, self.image)

    def test_interpolation_outside_image(self):
        """Test if error is raised when the position is outside of the image."""
        with self.assertRaises(ValueError):
            bilinear_interpolation(2.1, 0, self.image)
        with self.assertRaises(ValueError):
            bilinear_interpolation(0, 2.1, self.image)

    def test_interpolate(self):
        """Test the interpolate helper function."""
        self.assertEqual(interpolate(0, 1, 0), 0)
        self.assertEqual(interpolate(10, 20, 0), 10)

        self.assertEqual(interpolate(0, 1, 0.1), 0.1)
        self.assertEqual(interpolate(10, 20, 0.1), 11.0)
        self.assertEqual(interpolate(0, 10, 0.1), 1.0)

        self.assertEqual(interpolate(0, 1, 0.9), 0.9)
        self.assertEqual(interpolate(0, 1, 1), 1.0)
        self.assertEqual(interpolate(0, 50, 0.9), 45.0)

    def test_get_array_value(self):
        """Test the array getter."""
        self.assertEqual(get_array_value(0, 0, self.image), 0)
        self.assertEqual(get_array_value(2, 2, self.image), 8)
        self.assertEqual(get_array_value(1, 0, self.image), 1)
        self.assertEqual(get_array_value(0, 1, self.image), 3)

    def test_opencv(self):
        """Test using opencv resize()"""
        np.random.seed(1)
        img_np = np.random.random([3,3])
        img_cv = cv2.resize(img_np,(2,2), interpolation=cv2.INTER_LINEAR)
        self.assertEqual(img_cv[0,0], bilinear_interpolation(0.5, 0.5, img_np))

    def test_wikipedia(self):
        """Test with example values from Wikipedia 

        https://en.wikipedia.org/wiki/Bilinear_interpolation#Application_in_image_processing"""
        data = np.array([[91, 210], [162, 95]])
        self.assertEqual(bilinear_interpolation(0.5, 0, data), 150.5)
        self.assertEqual(bilinear_interpolation(0.5, 1, data), 128.5)
        self.assertAlmostEqual(bilinear_interpolation(0.5, 0.2, data), 146.1)
