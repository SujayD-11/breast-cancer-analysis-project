import requests
url = 'http://127.0.0.1:81/predict'
r = requests.post(url,json={
  "radius_mean": 13.54,
  "texture_mean": 14.36,
  "perimeter_mean": 87.46,
  "area_mean": 566.3,
  "smoothness_mean": 0.09779,
  "compactness_mean": 0.08129,
  "concavity_mean": 0.06664,
  "concave points_mean": 0.04781,
  "symmetry_mean": 0.1885,
  "fractal_dimension_mean": 0.05766
})
print(r.json())