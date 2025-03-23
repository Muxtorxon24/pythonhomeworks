# 51. Structured array (x,y) and color (r,g,b)
import numpy as np
dtype = [('position', [('x', float), ('y', float)]), ('color', [('r', int), ('g', int), ('b', int)])]
array = np.zeros(5, dtype=dtype)
array['position']['x'], array['position']['y'] = np.random.rand(5), np.random.rand(5)
array['color']['r'], array['color']['g'], array['color']['b'] = np.random.randint(0, 256, 5), np.random.randint(0, 256, 5), np.random.randint(0, 256, 5)
print(array)

# 52. Compute point-by-point distances
from scipy.spatial import distance
coords = np.random.rand(100, 2)
distances = distance.cdist(coords, coords)
print(distances)

# 53. Convert float32 array to int32 in place
arr = np.random.rand(10).astype(np.float32)
arr.view(np.int32)[:] = arr.astype(np.int32)
print(arr)

# 54. Read a file with missing values
from io import StringIO
data = "1, 2, 3, 4, 5\n6,  ,  , 7, 8\n ,  , 9,10,11"
arr = np.genfromtxt(StringIO(data), delimiter=",", dtype=np.float32)
print(arr)

# 55. NumPy equivalent of enumerate
arr = np.array([[1, 2], [3, 4]])
for index, value in np.ndenumerate(arr): print(index, value)

# 56. Generate a 2D Gaussian-like array
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
gaussian = np.exp(-(x**2 + y**2))
print(gaussian)

# 57. Randomly place p elements in a 2D array
arr = np.zeros((10, 10))
p = 5
indices = np.unravel_index(np.random.choice(arr.size, p, replace=False), arr.shape)
arr[indices] = 1
print(arr)

# 58. Subtract mean of each row
matrix = np.random.rand(5, 5)
result = matrix - matrix.mean(axis=1, keepdims=True)
print(result)

# 59. Sort array by nth column
arr = np.random.randint(0, 10, (5, 5))
sorted_arr = arr[arr[:, 2].argsort()]
print(sorted_arr)

# 60. Check if a 2D array has null columns
arr = np.array([[1, 0, 3], [0, 0, 2], [0, 0, 1]])
null_columns = np.all(arr == 0, axis=0)
print(null_columns)

# 61. Find nearest value in an array
arr = np.random.rand(10)
val = 0.5
nearest = arr[np.abs(arr - val).argmin()]
print(nearest)

# 62. Compute sum of (1,3) and (3,1) arrays with iterator
a, b = np.arange(3).reshape(1,3), np.arange(3).reshape(3,1)
it = np.nditer([a, b, None])
for x, y, z in it: z[...] = x + y
print(it.operands[2])

# 63. Create an array class with a name attribute
class NamedArray(np.ndarray):
    def __new__(cls, arr, name="array"):
        obj = np.asarray(arr).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.name = getattr(obj, "name", "array")
arr = NamedArray(np.arange(10), "my_array")
print(arr.name, arr)

# 64. Add 1 to elements indexed by another vector
arr = np.zeros(10, dtype=int)
indices = np.array([1, 2, 2, 3, 3, 3])
np.add.at(arr, indices, 1)
print(arr)

# 65. Accumulate elements based on an index list
X, I = np.array([1, 2, 3, 4, 5]), np.array([0, 1, 2, 1, 0])
F = np.zeros(3)
np.add.at(F, I, X)
print(F)

# 66. Count unique colors in (w,h,3) image
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
unique_colors = np.unique(image.reshape(-1, 3), axis=0).shape[0]
print(unique_colors)

# 67. Sum over last two axes of a 4D array
arr = np.random.rand(2, 3, 4, 5)
sum_result = arr.sum(axis=(-2, -1))
print(sum_result)

import numpy as np

# 68. Compute means of subsets
D, S = np.random.rand(10), np.random.randint(0, 3, 10)
means = np.bincount(S, weights=D) / np.bincount(S)
print(means)

# 69. Get diagonal of a dot product
A, B = np.random.rand(3, 3), np.random.rand(3, 3)
diag = np.einsum('ij,ji->i', A, B.T)
print(diag)

# 70. Interleave 3 consecutive zeros
vec = np.array([1, 2, 3, 4, 5])
result = np.zeros(len(vec) + (len(vec) - 1) * 3)
result[::4] = vec
print(result)

# 71. Multiply (5,5,3) by (5,5)
A, B = np.random.rand(5, 5, 3), np.random.rand(5, 5)
result = A * B[..., None]
print(result)

# 72. Swap two rows
A = np.arange(25).reshape(5, 5)
A[[0, 1]] = A[[1, 0]]
print(A)

# 73. Find unique line segments from triangles
T = np.random.randint(0, 10, (10, 3))
edges = np.vstack([T[:, [0, 1]], T[:, [1, 2]], T[:, [0, 2]]])
edges = np.sort(edges, axis=1)
unique_edges = np.unique(edges, axis=0)
print(unique_edges)

# 74. Generate array A from bincount C
C = np.array([3, 0, 2, 1])
A = np.repeat(np.arange(len(C)), C)
print(A)

# 75. Compute sliding window averages
Z, n = np.random.rand(10), 3
window_means = np.convolve(Z, np.ones(n)/n, mode='valid')
print(window_means)

# 76. Generate 2D shifted array
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, 4)
print(R)

# 77. Negate a boolean or change float sign in place
B = np.array([True, False, True])
B[:] = ~B
F = np.array([1.0, -2.5, 3.4])
F *= -1
print(B, F)

# 78. Compute distance from a point to lines
P0, P1 = np.random.rand(5, 2), np.random.rand(5, 2)
p = np.random.rand(2)
dist = np.abs(np.cross(P1 - P0, P0 - p)) / np.linalg.norm(P1 - P0, axis=1)
print(dist)

# 79. Compute distances from points to lines
P = np.random.rand(4, 2)
D = np.abs(np.cross(P1[:, None] - P0[:, None], P[None] - P0[:, None])) / np.linalg.norm(P1 - P0, axis=1)[:, None]
print(D)

# 80. Extract subpart with fixed shape centered at an element

def extract_subarray(arr, center, shape, fill_value=0):
    """ Berilgan array ichidan (center) koordinatasi atrofidagi 
        (shape) o‘lchamdagi kichik qismni kesib oladi.
        Agar chegaradan chiqib ketsa, u joylar fill_value bilan to‘ldiriladi.
    """
    h, w = arr.shape
    sh, sw = shape
    ch, cw = center

    # Kesib olinadigan qismning chegaralarini hisoblash
    top, bottom = ch - sh // 2, ch + sh // 2 + 1
    left, right = cw - sw // 2, cw + sw // 2 + 1

    # Natijaviy massiv
    result = np.full((sh, sw), fill_value, dtype=arr.dtype)

    # Matritsaning haqiqiy chegaralarini aniqlash
    top_valid, bottom_valid = max(0, top), min(h, bottom)
    left_valid, right_valid = max(0, left), min(w, right)

    # Natijaviy massivning mos qismiga haqiqiy ma'lumotlarni joylash
    result[(top_valid - top):(bottom_valid - top), (left_valid - left):(right_valid - left)] = arr[top_valid:bottom_valid, left_valid:right_valid]

    return result

# Sinov uchun massiv yaratamiz
A = np.arange(100).reshape(10, 10)

# (5,5) markaz atrofidan 3x3 sub-massivni olish
print(extract_subarray(A, (5, 5), (3, 3)))


# 81. Generate overlapping subarrays
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, 4)
print(R)

# 82. Compute matrix rank
M = np.random.rand(4, 4)
rank = np.linalg.matrix_rank(M)
print(rank)

# 83. Find most frequent value
Z = np.random.randint(0, 10, 100)
most_freq = np.bincount(Z).argmax()
print(most_freq)

# 84. Extract contiguous 3x3 blocks
A = np.random.rand(10, 10)
blocks = np.lib.stride_tricks.sliding_window_view(A, (3, 3))
print(blocks)

# 85. Create symmetric 2D array subclass
class SymmetricArray(np.ndarray):
    def __setitem__(self, idx, value):
        super().__setitem__(idx, value)
        super().__setitem__((idx[1], idx[0]), value)
Z = np.zeros((5, 5)).view(SymmetricArray)
Z[1, 2] = 5
print(Z)

# 86. Compute sum of p matrix products
M, V = np.random.rand(3, 4, 4), np.random.rand(3, 4, 1)
result = np.einsum('pij,pjk->ik', M, V)
print(result)

# 87. Compute block sum (4x4)
A = np.random.rand(16, 16)
block_sum = A.reshape(4, 4, 4, 4).sum(axis=(1, 3))
print(block_sum)

# 88. Implement Conway's Game of Life
def game_of_life_step(grid):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0))
    return (neighbors == 3) | ((grid == 1) & (neighbors == 2))

# 89. Get n largest values
Z, n = np.random.rand(10), 3
largest = Z[np.argpartition(Z, -n)[-n:]]
print(largest)

# 90. Compute Cartesian product
arrays = [np.array([1, 2]), np.array([3, 4])]
cartesian = np.array(np.meshgrid(*arrays)).T.reshape(-1, len(arrays))
print(cartesian)

# 91. Create record array
A = np.array([(1, 2, 3), (4, 5, 6)], dtype=[('x', int), ('y', int), ('z', int)])
print(A)

# 92. Compute Z³ using 3 methods
Z = np.random.rand(10)
print(Z**3, np.power(Z, 3), np.einsum('i,i,i->i', Z, Z, Z))

# 93. Find rows in A containing elements of each row in B
A, B = np.random.randint(0, 5, (8, 3)), np.random.randint(0, 5, (2, 2))
mask = np.all(np.isin(A[:, None], B), axis=-1)
print(A[mask.any(1)])

# 94. Extract rows with unequal values
M = np.random.randint(0, 5, (10, 3))
unique_rows = M[M.max(axis=1) != M.min(axis=1)]
print(unique_rows)

# 95. Convert ints to binary matrix
V = np.array([1, 2, 3, 4])
binary = ((V[:, None] & (1 << np.arange(8))) > 0).astype(int)
print(binary)

# 96. Extract unique rows
A = np.random.randint(0, 5, (10, 3))
unique_rows = np.unique(A, axis=0)
print(unique_rows)

# 97. Einsum equivalents
A, B = np.random.rand(4), np.random.rand(4)
print(np.einsum('i,i->', A, B), np.einsum('i,j->ij', A, B), np.einsum('i->', A), np.einsum('i,i->i', A, B))

# 98.
import numpy as np

# Berilgan yo'l
X = np.cumsum(np.random.rand(10))  # X koordinatalari
Y = np.cumsum(np.random.rand(10))  # Y koordinatalari

# Yo'l uzunligi va namunalar soni
distances = np.sqrt(np.diff(X)**2 + np.diff(Y)**2)
cumulative_distances = np.insert(np.cumsum(distances), 0, 0)
num_samples = 20
sample_points = np.linspace(0, cumulative_distances[-1], num_samples)

# Interpolatsiya orqali yangi nuqtalarni topish
X_sampled = np.interp(sample_points, cumulative_distances, X)
Y_sampled = np.interp(sample_points, cumulative_distances, Y)

print(np.column_stack((X_sampled, Y_sampled)))

# 99. 
X = np.random.randint(0, 10, (10, 4))  # Tasodifiy butun sonli matritsa
n = 20  # Belgilangan qiymat

# Shartga mos qatorlarni tanlash
valid_rows = X[np.all(X == X.astype(int), axis=1) & (X.sum(axis=1) == n)]
print(valid_rows)

#100. 
# Berilgan ma'lumotlar
X = np.random.randn(1000)  # Normal taqsimlangan tasodifiy sonlar
N = 1000  # Namunalash takrorlari

# Bootstrap namunalarini olish va ularning o‘rtacha qiymatlarini hisoblash
means = np.array([np.mean(np.random.choice(X, size=len(X), replace=True)) for _ in range(N)])

# 95% ishonchlilik oraliqlari
conf_int = np.percentile(means, [2.5, 97.5])
print("95% ishonchlilik oraliqlari:", conf_int)




# 1. 1 dan 10 gacha bo'lgan butun sonlardan iborat massiv yaratish
arr = np.arange(1, 11)

# 2. Har bir elementning kvadratini hisoblash
squared_arr = arr ** 2

# 3. Kvadratlangan massivning yig‘indisi, o‘rtacha qiymati va standart og‘ishini topish
sum_sq = np.sum(squared_arr)
mean_sq = np.mean(squared_arr)
std_sq = np.std(squared_arr)

# Natijalarni chiqarish
print("Original array:", arr)
print("Squared array:", squared_arr)
print("Sum of squared elements:", sum_sq)
print("Mean of squared elements:", mean_sq)
print("Standard deviation of squared elements:", std_sq)
