import pytest

from cloudvolume.lib import save_images

import cc3d
import numpy as np


def test_2d_cross():
  input_labels = np.zeros( (17,17,1), dtype=np.uint8 )
  input_labels[:] = 1
  input_labels[:,8,:] = 0
  input_labels[8,:,:] = 0

  output_labels = cc3d.connected_components(input_labels).astype(np.uint8)
  output_labels = output_labels[:,:,0]

  ground_truth = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4],
  ], dtype=np.uint8)

  assert np.all(output_labels == ground_truth)

  input_labels[9:,9:,:] = 2
  output_labels = cc3d.connected_components(input_labels).astype(np.uint8)
  output_labels = output_labels[:,:,0]
  assert np.all(output_labels == ground_truth)

def test_2d_cross_with_intruder():
  input_labels = np.zeros( (5,5,1), dtype=np.uint8 )
  input_labels[:] = 1
  input_labels[:,2,:] = 0
  input_labels[2,:,:] = 0
  input_labels[3:,3:,:] = 2
  input_labels[3,3,:] = 1

  output_labels = cc3d.connected_components(input_labels).astype(np.uint8)
  output_labels = output_labels[:,:,0]

  ground_truth = np.array([
    [1, 1, 0, 2, 2],
    [1, 1, 0, 2, 2],
    [0, 0, 0, 0, 0],
    [3, 3, 0, 4, 5],
    [3, 3, 0, 5, 5],
  ], dtype=np.uint8)

  assert np.all(output_labels == ground_truth)



# save_images(input_labels, directory='./save_images/input')
# save_images(output_labels * 25, directory='./save_images/output')