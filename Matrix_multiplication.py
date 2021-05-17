import numpy as np

pts = np.array([(0,0), (4,0), (4,3), (0,3)])
print (pts[None, :].shape, pts[: ,None].shape)
m = pts[None, :] - pts[:, None]
dist_matrix = np.sqrt (np.sum((pts[None, :] - pts[:, None])**2, -1))
print (np.where (dist_matrix > 0))