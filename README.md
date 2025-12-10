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

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8480e1ec-5607-4801-9d85-0bd33ffecace" />   
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/62375481-d869-4ca4-b58a-2e0789881d8c" />






Code_4:

Input: Image file path

Output: Four windows showing original and flipped images; error if loading fails.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/5ed5a597-11b3-4549-825b-daac1616f473" />

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/fb7b4c90-939d-479e-88d0-df11228bfc7a" />     <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/699ab9e1-269a-4128-922b-7b5ebcf93e27" />        <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/4d6cbb2f-9d2f-41b2-8177-cb9f3e65773c" />       <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/103e0e1f-bfa1-441a-b8ec-c63d11601414" />





Code_5:

Input: Image file path

Output: Shows original and resized 300x300 image; saves resized as resized_output.jpg.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/2fe5f5a8-2476-459b-86f5-08e939bf3c15" />

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/42162e4b-bcba-400c-82ac-4ee9447187aa" />         <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/d1ed8874-9275-4f3f-9db1-31056a99a887" />





Code_6:

Input: Image file path

Output: Shows original and grayscale images; saves grayscale as grayscale_output.jpg.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8dc2f347-9ee9-4520-986c-8a89ba5786b1" />

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/3b62b907-8fe6-47bc-ad13-263ccfb9840c" />            <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/3bbe5f72-3878-4f7b-b11a-934e651a5ec6" />





Code_7:

Input: Image file path

Output: Displays original and Gaussian-blurred images; saves blurred as blurred_output.jpg.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/868a2706-34b3-4196-b693-f2e78bf3c6f0" />

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/7a4ce91a-ecb9-4914-b59c-bb7820b53c2a" />          <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/ea425190-2c38-4503-82ed-461591c0e792" />





Code_8:

Input: No input

Output: Displays a 500x500 black image with a line, rectangle, circle, and text.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/8ac28943-616d-4ff1-b06b-89dbcb633329" />



Code_9:

Input: Image file path

Output: Shows grayscale image and its binary thresholded version.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/82455f37-30f3-438b-b4a3-b0aaf88a4e93" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/767c5205-3d2d-4835-ac2e-8545177278c1" />            <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/55e38f51-3521-49d2-8740-c6539236adb7" />



Code_10:

Input: Image file path

Output: Displays Canny edge-detected image in a window titled "Edges".

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/bfdc29c3-db61-4dc9-a8a9-9f58b348ca3b" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/3bd701fe-296b-414a-a265-8044bde4a0fd" />


Code_11:

Input: Image file path

Output: Shows image with blue rectangles around detected faces.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/636fa658-6710-4a97-bd70-fe3f6f88a5ec" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/992199f1-ded6-4d63-abab-3d0b2c16b5d9" />


Code_12:

Input: Image file path

Output: Displays image with detected contours highlighted in green.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/61efa18e-66e1-4fd8-8ba4-cf8e79f3484e" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/0b3a0230-46e5-432c-97c6-cb553c8678a1" />



Code_13:

Input: Image file path

Output: Shows original image, blue mask, and filtered blue regions.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/7bbad383-35f9-4871-8184-b89462c59836" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/c458259e-1397-46d8-96fb-65b16098d0fc" />                  <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/c96fef11-7453-4e6f-ab02-878e4ea66a0c" />                  <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/9dc08371-0bf1-49c9-a42a-de4ddf760478" />




Code_14:

Input: Image file path

Output: Displays extracted foreground in a window.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/4b92ca5e-26ca-4849-a8d4-8dd62a043e41" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/95cb4d79-3fb4-4fec-ad0e-490091a832fc" />                   <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/04cc3eaa-265d-4d4b-b26b-274cc4645736" />





Code_15:

Input: No input

Output: Live webcam feed highlighting blue-colored regions in real time.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/2ffc32d8-16f7-4f8b-8eba-8d99b05ef447" />
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/4ba601af-7f77-4eda-a488-e20c2e6f8144" />                  <img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/d599a81d-5bc0-405b-a14a-e60270522585" />






Code_16:

Input: Image file path

Output: Displays thresholded, eroded, and dilated images.

<img width="871" height="447" alt="image" src="https://github.com/user-attachments/assets/846567de-35ef-4cfa-a2f2-ec1e897d95af" />
<img width="610" height="414" alt="image" src="https://github.com/user-attachments/assets/380e87bd-1c64-4a12-8d22-7e28d3ceefb2" />                    <img width="507" height="402" alt="image" src="https://github.com/user-attachments/assets/bf7bcc76-62f3-41f0-8ef3-9e9f661e2892" />                  <img width="746" height="460" alt="image" src="https://github.com/user-attachments/assets/a9ecdd69-092b-42f1-9a26-cf554823cb57" />





Code_17:

Input: Text string

Output: List of cleaned, tokenized, lemmatized words.

<img width="940" height="121" alt="image" src="https://github.com/user-attachments/assets/ef8a1ba9-2404-41d7-ad56-8703301284e5" />




Code_18:

Input: List of sentences

Output: Classification report, confusion matrix, predictions, and class probabilities.

<img width="943" height="386" alt="image" src="https://github.com/user-attachments/assets/ce7977bf-2962-45f4-baa8-92021ce04224" />




Code_19:

Input: List of sentences

Output: Best parameters, best CV F1 score, and a sample prediction.

<img width="938" height="90" alt="image" src="https://github.com/user-attachments/assets/5b5dbb1e-1b17-4458-b69c-6f3114d81577" />



Code_20:

Input: List of sentences

Output: Vocabulary list and TF-IDF matrix of the input texts.

<img width="929" height="240" alt="image" src="https://github.com/user-attachments/assets/05b15637-5c9e-4136-9821-ec21137aab32" />



Code_21:

Input: Text string

Output: Named Entities, POS with lemmas, and noun chunks extracted from text.

<img width="938" height="772" alt="image" src="https://github.com/user-attachments/assets/c920e0e9-c63e-44e7-beff-4f0122383581" />
<img width="932" height="318" alt="image" src="https://github.com/user-attachments/assets/918a783b-b498-42c8-bf77-14588f38f60d" />




Code_22:

Input: List of sentences

Output: Classification report for sentiment prediction.

<img width="739" height="364" alt="image" src="https://github.com/user-attachments/assets/0b9232ce-0a04-4e7a-94a9-2305ea605587" />





Code_23:

Input: List of sentences

Output: Cosine similarity matrix showing pairwise similarity scores.

<img width="931" height="198" alt="image" src="https://github.com/user-attachments/assets/80647a53-bff3-402c-8569-8d78b4d21f19" />





Code_24:

Input: List of sentences

Output: Topics discovered with top words and their weights.

<img width="920" height="76" alt="image" src="https://github.com/user-attachments/assets/40ffedfc-4eaf-43f6-af02-fba0e7faf2be" />

## 📧 Support

For issues, questions, or contributions, please refer to the project documentation or create an issue in the repository.

---

**Built with ❤️ for environmental protection and oil spill detection**

