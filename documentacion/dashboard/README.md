# 📊 Telco Customer Churn Prediction Dashboard

Interactive Streamlit dashboard for analyzing and predicting customer churn.

## 🎯 Features

### 📊 Overview
- General project statistics
- Churn trends over time
- Customer distribution analysis
- Key insights and recommendations

### 🎯 Risk Analysis
- Individual customer churn prediction
- Interactive input form
- Real-time probability calculation
- Risk level classification
- Visual probability gauge

### 📈 Model Metrics
- Performance metrics (ROC-AUC, Precision, Recall, F1)
- Confusion matrix visualization
- ROC curve
- Feature importance analysis
- Model information

### 💰 ROI Simulator
- Calculate retention campaign ROI
- Scenario analysis
- Cost-benefit breakdown
- Financial recommendations

### 🔍 Model Monitoring
- Performance tracking over time
- Prediction volume monitoring
- Data drift detection
- Alerts and warnings

## 🚀 Installation

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the dashboard:
```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `dashboard/app.py` as the main file
5. Deploy!

### Configuration

No special configuration needed. The dashboard automatically loads the model from `../models/`.

## 📁 File Structure

```
dashboard/
├── app.py                          # Main page (Home)
├── pages/
│   ├── 1_📊_Overview.py           # Overview page
│   ├── 2_🎯_Risk_Analysis.py      # Risk prediction page
│   ├── 3_📈_Model_Metrics.py      # Model metrics page
│   ├── 4_💰_ROI_Simulator.py      # ROI calculator page
│   └── 5_🔍_Model_Monitoring.py   # Monitoring page
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🎨 Usage

### Predicting Churn Risk

1. Navigate to **🎯 Risk Analysis**
2. Fill in customer information:
   - Demographics (gender, age, etc.)
   - Services (phone, internet, etc.)
   - Account details (tenure, charges, etc.)
3. Click **Predict Churn Risk**
4. View results:
   - Churn probability
   - Risk level
   - Visual gauge

### Calculating ROI

1. Navigate to **💰 ROI Simulator**
2. Enter campaign parameters:
   - Customer base size
   - Current churn rate
   - Campaign costs
   - Expected results
3. View ROI analysis:
   - Net benefit
   - ROI percentage
   - Scenario comparison

## 📊 Sample Data

The dashboard uses sample data for demonstration purposes. In production:
- Connect to your database
- Load real customer data
- Track actual predictions
- Monitor real performance

## 🔧 Customization

### Adding New Pages

1. Create a new file in `pages/` with format: `N_Icon_Name.py`
2. Use Streamlit components to build your page
3. The page will automatically appear in the sidebar

### Modifying Visualizations

All visualizations use Plotly. To customize:
- Edit the `plotly.graph_objects` or `plotly.express` code
- Adjust colors, layouts, and styles
- Add new charts as needed

## 📝 License

MIT

