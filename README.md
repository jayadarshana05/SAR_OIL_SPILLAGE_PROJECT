# Leela Kumari_OilSpillageProject_Nov2025
# 🌊 Oil Spill Detection System

An innovative, comprehensive web application for detecting oil spills in images and videos using advanced YOLOv11 deep learning model. Built with Streamlit for an intuitive, user-friendly interface.

## ✨ Features

### 🎯 Core Capabilities
- **📸 Image Detection**: Upload single or multiple images for batch processing
- **🎥 Video Detection**: Process video files frame-by-frame with progress tracking
- **📹 Real-time Camera**: Live detection from webcam with real-time statistics
- **📊 Analytics Dashboard**: Comprehensive statistics, visualizations, and insights
- **⚙️ Customizable Settings**: Adjust confidence thresholds and preferences

### 🚀 Advanced Features
- **Batch Processing**: Handle multiple images simultaneously
- **Interactive Visualizations**: Plotly charts for confidence distributions and timelines
- **Export Options**: Download results in multiple formats (TXT, CSV, JSON)
- **Heatmap Overlays**: Visualize detection density
- **Coverage Analysis**: Calculate spill coverage percentages
- **Detection History**: Track and analyze detection patterns over time
- **Real-time Statistics**: Live metrics during processing
- **GPU Support**: Automatic GPU acceleration when available

## 📋 Requirements

- Python 3.10 or higher
- CUDA-capable GPU (optional, for faster processing)
- Webcam (optional, for real-time detection)

## 🛠️ Installation

### Option 1: Using Conda (Recommended)

1. **Create the conda environment:**
   ```bash
   conda env create -f environment.yml
   ```

2. **Activate the environment:**
   ```bash
   conda activate oil_spill
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

### Option 2: Using pip

1. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv oil_spill_env
   source oil_spill_env/bin/activate  # On Windows: oil_spill_env\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
oil_spill/
├── app.py                      # Main Streamlit application
├── best.pt                     # YOLOv11 trained model
├── pages/                      # Multi-page application pages
│   ├── 1_📸_Image_Detection.py
│   ├── 2_🎥_Video_Detection.py
│   ├── 3_📹_Real-time_Camera.py
│   ├── 4_📊_Analytics_Dashboard.py
│   └── 5_⚙️_Settings.py
├── utils/                      # Utility modules
│   ├── model_loader.py         # Model loading and caching
│   ├── image_processor.py      # Image processing functions
│   ├── video_processor.py      # Video processing functions
│   ├── visualizations.py       # Visualization utilities
│   └── report_generator.py     # Report generation
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment file
└── README.md                   # This file
```

## 🎮 Usage

### Image Detection
1. Navigate to **📸 Image Detection** page
2. Upload one or more images (PNG, JPG, JPEG, BMP, TIFF)
3. Adjust confidence threshold in the sidebar
4. View detection results with bounding boxes
5. Export results in various formats

### Video Detection
1. Navigate to **🎥 Video Detection** page
2. Upload a video file (MP4, AVI, MOV, MKV, etc.)
3. Preview sample frames
4. Process the video (progress bar shows status)
5. Download annotated video and analysis reports

### Real-time Camera
1. Navigate to **📹 Real-time Camera** page
2. Click "Start Camera" button
3. View live detections with real-time statistics
4. Click "Stop Camera" when finished

### Analytics Dashboard
1. Navigate to **📊 Analytics Dashboard** page
2. View comprehensive statistics and visualizations
3. Analyze detection patterns over time
4. Export analytics data

## ⚙️ Configuration

### Model Settings
- **Confidence Threshold**: Adjust detection sensitivity (0.0 - 1.0)
- **Device**: Automatically uses GPU if available, falls back to CPU

### Application Settings
- Customize display preferences
- Configure export formats
- Adjust processing parameters

## 📊 Supported Formats

### Input
- **Images**: PNG, JPG, JPEG, BMP, TIFF
- **Videos**: MP4, AVI, MOV, MKV, FLV, WMV

### Output
- **Annotated Images/Videos**: With bounding boxes and labels
- **Text Reports**: Detailed detection information
- **CSV Files**: Structured data for analysis
- **JSON Files**: Machine-readable results

## 🔧 Technical Details

- **Model**: YOLOv11 (Ultralytics)
- **Framework**: PyTorch
- **Web Framework**: Streamlit
- **Visualization**: Plotly, Matplotlib
- **Image Processing**: OpenCV, PIL
- **Data Handling**: Pandas, NumPy

## 🎨 UI Features

- **Modern Design**: Clean, intuitive interface
- **Responsive Layout**: Works on different screen sizes
- **Custom Styling**: Enhanced visual appearance
- **Progress Indicators**: Real-time processing feedback
- **Interactive Charts**: Plotly visualizations
- **Color-coded Alerts**: Visual feedback for detections

## 🚀 Performance Tips

1. **Use GPU**: Ensure CUDA is available for faster processing
2. **Batch Processing**: Process multiple images together for efficiency
3. **Adjust Thresholds**: Lower confidence threshold for more detections (may include false positives)
4. **Video Resolution**: Lower resolution videos process faster

## 📝 Notes

- The model file (`best.pt`) must be in the project root directory
- First run may take longer as the model loads
- GPU acceleration significantly improves processing speed
- Large videos may take time to process - be patient!

## 🐛 Troubleshooting

### Model not loading
- Ensure `best.pt` exists in the project directory
- Check file permissions

### Camera not working
- Verify camera permissions
- Check if camera is being used by another application

### Slow processing
- Use GPU if available
- Reduce image/video resolution
- Process fewer images at once

### Import errors
- Ensure all dependencies are installed
- Activate the correct conda/virtual environment

## 📄 License

This project is provided as-is for demonstration and research purposes.

## 🙏 Acknowledgments

- YOLOv11 by Ultralytics
- Streamlit for the web framework
- All open-source contributors
## 📝 Practice Code Summaries
  This section contains brief summaries of various practice codes covering image processing, computer vision, and NLP tasks, showing inputs and outputs for each.

Code_1:

Input: No input

Output: Live webcam video feed in a window titled "Camera Stream" until ‘q’ is pressed.
<img width="400" height="200" alt="Screenshot 2025-12-08 202507" src="https://github.com/user-attachments/assets/f6f41b7e-78b3-4e1d-b0c8-b8f6984c0107" />             <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/5427d950-c511-467d-93e6-cbad00c55c97" />


Code_2:

Input: No input

Output: Live webcam feed with each frame saved sequentially in a folder named frames.
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/f3044b03-5d48-407f-aaa3-c161e3e7dd49" />      <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/9067bf0c-b0e1-4211-8ee6-4ae99709a2cc" />


Code_3:

Input: Image file path

Output: Displays the image or prints "Error: Could not read image."
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8480e1ec-5607-4801-9d85-0bd33ffecace" />      <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/62375481-d869-4ca4-b58a-2e0789881d8c" />


Code_4:

Input: Image file path

Output: Four windows showing original and flipped images; error if loading fails.
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/5ed5a597-11b3-4549-825b-daac1616f473" />        <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/fb7b4c90-939d-479e-88d0-df11228bfc7a" />           <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/699ab9e1-269a-4128-922b-7b5ebcf93e27" />       <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/4d6cbb2f-9d2f-41b2-8177-cb9f3e65773c" />         <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/103e0e1f-bfa1-441a-b8ec-c63d11601414" />





Code_5:

Input: Image file path

Output: Shows original and resized 300x300 image; saves resized as resized_output.jpg.
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/2fe5f5a8-2476-459b-86f5-08e939bf3c15" />      <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/42162e4b-bcba-400c-82ac-4ee9447187aa" />      <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/d1ed8874-9275-4f3f-9db1-31056a99a887" />



Code_6:

Input: Image file path

Output: Shows original and grayscale images; saves grayscale as grayscale_output.jpg.
<img width="404" height="281" alt="image" src="https://github.com/user-attachments/assets/8dc2f347-9ee9-4520-986c-8a89ba5786b1" />


Code_7:
Input: Image file path
Output: Displays original and Gaussian-blurred images; saves blurred as blurred_output.jpg.

Code_8:
Input: No input
Output: Displays a 500x500 black image with a line, rectangle, circle, and text.

Code_9:
Input: Image file path
Output: Shows grayscale image and its binary thresholded version.

Code_10:
Input: Image file path
Output: Displays Canny edge-detected image in a window titled "Edges".

Code_11:
Input: Image file path
Output: Shows image with blue rectangles around detected faces.

Code_12:
Input: Image file path
Output: Displays image with detected contours highlighted in green.

Code_13:
Input: Image file path
Output: Shows original image, blue mask, and filtered blue regions.

Code_14:
Input: Image file path
Output: Displays extracted foreground in a window.

Code_15:
Input: No input
Output: Live webcam feed highlighting blue-colored regions in real time.

Code_16:
Input: Image file path
Output: Displays thresholded, eroded, and dilated images.

Code_17:
Input: Text string
Output: List of cleaned, tokenized, lemmatized words.

Code_18:
Input: List of sentences
Output: Classification report, confusion matrix, predictions, and class probabilities.

Code_19:
Input: List of sentences
Output: Best parameters, best CV F1 score, and a sample prediction.

Code_20:
Input: List of sentences
Output: Vocabulary list and TF-IDF matrix of the input texts.

Code_21:
Input: Text string
Output: Named Entities, POS with lemmas, and noun chunks extracted from text.

Code_22:
Input: List of sentences
Output: Classification report for sentiment prediction.

Code_23:
Input: List of sentences
Output: Cosine similarity matrix showing pairwise similarity scores.

Code_24:
Input: List of sentences
Output: Topics discovered with top words and their weights.

## 📧 Support

For issues, questions, or contributions, please refer to the project documentation or create an issue in the repository.

---

**Built with ❤️ for environmental protection and oil spill detection**

