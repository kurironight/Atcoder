
# 美術館のセキュリティ
import numpy as np
from scipy.spatial.distance import cdist


def calculate_dist(locate, camera_locate):
    locate = locate.reshape([1, 2])
    locates = np.concatenate([locate, camera_locate])
    distance = cdist(locates, locates)[0][1:]
    return distance


def calc_degree(locate, camera_locate):
    locate = locate.reshape([1, 2])
    vec = locate-camera_locate
    criterion = np.tile([1, 0], vec.shape[0])
    naiseki = vec*criterion.reshape(-1, 2)
    naiseki = np.sum(naiseki, axis=1)
    dist = calculate_dist(np.array([0, 0]), vec)
    theta = np.arccos(naiseki/dist)*180/np.pi
    theta[vec[:, 1] < 0] = 360-theta[vec[:, 1] < 0]
    return theta


input_line = list(input().split())
input_line = [int(n) for n in input_line]
W, H, M, N = input_line[0], input_line[1], input_line[2], input_line[3]
camera_list = []
for i in range(M):
    line = list(input().split())
    line = [float(n) for n in line]
    camera_list.append(line)

camera_list = np.array(camera_list)

X_list = camera_list[:, 0]
Y_list = camera_list[:, 1]

camera_locate = np.stack([X_list, Y_list], 1)

for j in range(N):
    no_cover = True
    # 位置座標を取得
    line = list(input().split())
    line = [float(n) for n in line]
    X, Y = line[0], line[1]
    locate = np.array([X, Y])
    distance = calculate_dist(locate, camera_locate)

    in_dist = camera_list[:, 4] > distance
    in_dist_camera_list = camera_list[in_dist]
    X_list = in_dist_camera_list[:, 0]
    Y_list = in_dist_camera_list[:, 1]
    in_dist_camera_locate = np.stack([X_list, Y_list], 1)

    theta = calc_degree(locate, in_dist_camera_locate)
    cover = np.logical_and(theta <= in_dist_camera_list[:, 2]+in_dist_camera_list[:, 3]/2,
                           theta >= in_dist_camera_list[:, 2]-in_dist_camera_list[:, 3]/2)
    if np.any(cover):
        print("yes")
        no_cover = False
    if no_cover:
        print("no")
