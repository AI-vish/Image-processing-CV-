# 🧠 Image Processing Techniques: Essentials for ML Engineers

**Practice codes while I was exploring Digital Image Processing in my 3rd year of university.**  
This repository includes essential image processing and computer vision techniques that are crucial for most ML tasks.

---

## 📁 Repository Structure

image_io_and_display/
color_space_conversion/
image_enhancement/
filtering_and_smoothing/
edge_and_contour_detection/
morphological_operations/
thresholding_and_segmentation/
feature_extraction/
image_transformation/
data_augmentation/


---

## ⚙️ Techniques Overview

### 🖼️ Image I/O and Display  
Reading and writing images using **OpenCV** or **PIL**, displaying with **matplotlib**, resizing, cropping, rotating, and manipulating color channels.

### 🎨 Color Space Conversion  
Conversions between **RGB**, **Grayscale**, **HSV**, and **LAB**; normalization and histogram equalization for better color correction.

### ✨ Image Enhancement  
Contrast stretching, histogram equalization, **CLAHE (adaptive histogram)**, and gamma correction for improving image quality.

### 🧹 Filtering and Smoothing  
Applying **mean**, **Gaussian**, **median**, and **bilateral** filters to reduce noise, and sharpening filters for edge enhancement.

### ⚡ Edge and Contour Detection  
Using **Sobel**, **Laplacian**, and **Canny** detectors; finding contours and drawing bounding boxes around objects.

### 🧩 Morphological Operations  
Performing **erosion**, **dilation**, **opening**, **closing**, **gradient**, and **top-hat / black-hat** operations to refine binary images.

### 🧠 Thresholding and Segmentation  
Applying **global** and **adaptive thresholding**, **Otsu’s method**, **k-means clustering**, and **watershed** algorithms for segmentation.

### 🔍 Feature Extraction  
Extracting descriptors like **SIFT**, **ORB**, **HOG**, and **color histograms**, plus texture analysis using **GLCM**.

### 🔄 Image Transformation  
Performing **affine** and **perspective** transformations, geometric transforms, **Fourier** and **DCT** for frequency domain analysis.

### 🧬 Data Augmentation  
Generating synthetic variations via **flipping**, **rotation**, **scaling**, **cropping**, **color jittering**, and libraries like **Albumentations** or **torchvision**.

---

```bash
pip install opencv-python numpy matplotlib scikit-image pillow albumentations


