#!/bin/bash
cd C:\Users\HP\Downloads\oil_spill\oil_spill

echo "🔍 Checking conda environment..."
if conda env list | grep -q "oil_spill"; then
    echo "✅ Environment exists"
    conda activate oil_spill
else
    echo "📦 Creating environment..."
    conda env create -f environment.yml
    conda activate oil_spill
fi

echo "🔍 Verifying installation..."
python -c "import streamlit; import ultralytics; print('✅ Packages OK')" || {
    echo "❌ Missing packages, installing..."
    pip install -r requirements.txt
}

echo "🚀 Starting application..."
streamlit run app.py