🏥 Physics-Informed AI for Low-Dose CT Image Enhancement
📌 Overview

Computed Tomography (CT) is widely used in medical imaging, but reducing radiation dose—critical for patient safety—often results in noisy and low-quality images.

This project presents a hybrid physics + AI system that enhances low-dose CT reconstructions by combining:

Radon Transform & Filtered Back Projection (FBP) (physics-based reconstruction)
Deep Learning (CNN) for image enhancement

🔬 This work demonstrates how AI can improve diagnostic image quality while maintaining low radiation exposure.

🎯 Problem

There is a key trade-off in CT imaging:

Lower radiation dose → safer for patients
Lower dose → degraded image quality

This limits diagnostic reliability, especially in low-resource healthcare environments.

💡 Solution

We propose a two-stage reconstruction pipeline:

Physics-Based Reconstruction
Radon Transform → simulate projections
Filtered Back Projection → initial reconstruction
AI Enhancement Layer
CNN-based residual model
Learns to remove noise and restore structure
🔄 System Pipeline
Phantom → Sinogram → Noisy Sinogram → FBP → AI Enhancement → Final Image
📊 Results
🔍 Performance Comparison
Metric	Before AI	After AI
MSE	0.00168	✅ 0.00027
PSNR	27.73 dB	✅ 35.64 dB
SSIM	0.803	✅ 0.939
🧠 Interpretation

The AI-enhanced reconstruction significantly improves image quality across all evaluation metrics.

Higher PSNR → better signal quality
Lower MSE → closer to ground truth
Higher SSIM → improved structural preservation

These results demonstrate the effectiveness of combining physics-based reconstruction with deep learning for enhancing low-dose CT images.

🌍 Real-World Impact

This system has strong relevance for low-resource healthcare settings:

Improves image quality without expensive hardware upgrades
Supports radiologists in diagnosis
Reduces need for repeat scans (lower radiation exposure)
🤖 AI Component

A lightweight CNN-based residual model is used to:

Remove noise
Preserve anatomical structures
Enhance reconstructed images
⚖️ Responsible AI Considerations

While AI improves image quality, it may introduce subtle artifacts.

Careful validation is required before clinical deployment to ensure diagnostic reliability.

🛠️ Technologies
Python
NumPy
Matplotlib
scikit-image
TensorFlow / Keras
🚀 Future Work
Real CT dataset integration
Advanced deep learning models (U-Net)
Clinical validation studies
Deployment as a web-based tool
🧠 Author

Building AI-powered solutions for medical imaging and computational medical physics, with a focus on impactful applications in low-resource environments.
