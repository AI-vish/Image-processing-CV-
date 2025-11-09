{
  "title": "🧠 Image Processing Techniques — Essentials for ML Engineers",
  "description": "Practice codes while I was exploring Digital Image Processing in my 3rd year of university. This repo includes essential image processing and computer vision techniques.",
  "repository_structure": [
    "image_io_and_display",
    "color_space_conversion",
    "image_enhancement",
    "filtering_and_smoothing",
    "edge_and_contour_detection",
    "morphological_operations",
    "thresholding_and_segmentation",
    "feature_extraction",
    "image_transformation",
    "data_augmentation"
  ],
  "techniques": {
    "image_io_and_display": "Reading and writing images using OpenCV or PIL, displaying with matplotlib, resizing, cropping, rotating, and color channel manipulation.",
    "color_space_conversion": "RGB to Grayscale, HSV, and LAB conversions, normalization, and histogram equalization for color correction and enhancement.",
    "image_enhancement": "Contrast stretching, histogram equalization, CLAHE (adaptive histogram), and gamma correction to improve image quality.",
    "filtering_and_smoothing": "Applying mean, Gaussian, median, and bilateral filters to reduce noise, plus sharpening filters for edge enhancement.",
    "edge_and_contour_detection": "Using Sobel, Laplacian, and Canny edge detectors; finding contours and drawing bounding boxes around objects.",
    "morphological_operations": "Performing erosion, dilation, opening, closing, gradient, and top-hat/black-hat operations to refine binary images.",
    "thresholding_and_segmentation": "Applying global and adaptive thresholding, Otsu’s method, k-means clustering, and watershed algorithms for segmentation.",
    "feature_extraction": "Extracting image descriptors like SIFT, ORB, HOG, and color histograms, plus texture analysis with GLCM.",
    "image_transformation": "Performing affine and perspective transforms, geometric transformations, Fourier and DCT for frequency domain analysis.",
    "data_augmentation": "Creating synthetic data variations via flipping, rotation, scaling, cropping, color jittering, and using libraries like Albumentations or torchvision."
  },
  "dependencies": [
    "opencv-python",
    "numpy",
    "matplotlib",
    "scikit-image",
    "pillow",
    "albumentations"
  ],
  "references": [
    "OpenCV Documentation - https://docs.opencv.org/",
    "Scikit-Image Docs - https://scikit-image.org/docs/stable/",
    "Albumentations Library - https://albumentations.ai/",
    "PyImageSearch Tutorials - https://pyimagesearch.com/"
  ]
}
