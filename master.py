import streamlit as st
import sklearn
import joblib
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.header("Dominant Colour Extraction")

st.subheader("Input Image")
img = st.file_uploader("Choose an Image")

if img is not None:
    st.header("Original Image")
    st.image(img)

    # KMEANS CODE

    print(type(img))
    img = plt.imread(img)

    n = img.shape[0]*img.shape[1]
    all_pixels = img.reshape((n, 3))

    model  = KMeans(n_clusters = 5)
    model.fit(all_pixels)

    centers = model.cluster_centers_.astype('uint8')

    new_img = np.zeros((n, 3), dtype='uint8')

    for i in range(n):
        group_idx = model.labels_[i]
        new_img[i] = centers[group_idx]

    new_img = new_img.reshape(*img.shape)

    st.header("Modified Image")
    st.image(new_img)
