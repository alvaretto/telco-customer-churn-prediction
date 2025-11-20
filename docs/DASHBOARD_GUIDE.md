# 📊 Dashboard User Guide

Complete guide for using the Telco Customer Churn Prediction Dashboard.

## 🚀 Accessing the Dashboard

### Local Development
```bash
cd dashboard
streamlit run app.py
```

Open your browser at: `http://localhost:8501`

### Production (Streamlit Cloud)
Visit your deployed URL: `https://your-app.streamlit.app`

## 📱 Dashboard Pages

### 1. 🏠 Home (Main Page)

**Purpose:** Overview of the project and model information

**Features:**
- Model performance metrics (ROC-AUC, Recall, Precision, F1-Score)
- Project description
- Quick start guide
- List of all model features

**How to Use:**
1. Review the key metrics at the top
2. Read the project description
3. Check the model features list
4. Use the sidebar to navigate to other pages

---

### 2. 📊 Overview

**Purpose:** General statistics and visualizations

**Features:**
- Total customers and churn statistics
- Monthly churn rate trends
- Customer distribution (retained vs churned)
- Churn analysis by segment (contract type, internet service)
- Key insights and recommendations

**How to Use:**
1. Review the KPIs at the top (Total Customers, Churned, Churn Rate)
2. Analyze the churn trend chart
3. Compare customer distribution over time
4. Examine churn rates by different segments
5. Read the key insights for actionable recommendations

---

### 3. 🎯 Risk Analysis

**Purpose:** Predict churn risk for individual customers

**Features:**
- Interactive input form with 25 customer attributes
- Real-time churn prediction
- Probability calculation
- Risk level classification
- Visual probability gauge

**How to Use:**

1. **Enter Customer Demographics:**
   - Gender
   - Senior Citizen status
   - Partner status
   - Dependents

2. **Enter Service Information:**
   - Phone Service
   - Multiple Lines
   - Internet Service type
   - Online Security
   - Online Backup
   - Device Protection
   - Tech Support
   - Streaming TV
   - Streaming Movies

3. **Enter Account Details:**
   - Tenure (months with company)
   - Contract type
   - Paperless Billing
   - Payment Method
   - Monthly Charges
   - Total Charges

4. **Click "Predict Churn Risk"**

5. **Interpret Results:**
   - **Prediction**: HIGH RISK or LOW RISK
   - **Churn Probability**: Percentage likelihood of churn
   - **Risk Level**: Low (🟢), Medium (🟡), High (🟠), or Critical (🔴)
   - **Gauge Chart**: Visual representation of churn probability

**Example Use Case:**
```
Customer Profile:
- Female, not senior, has partner, no dependents
- Fiber optic internet, no security/backup
- Month-to-month contract
- 12 months tenure
- $70/month charges

Result: 77% churn probability → CRITICAL RISK
Action: Immediate retention campaign recommended
```

---

### 4. 💰 ROI Simulator

**Purpose:** Calculate return on investment for retention campaigns

**Features:**
- Campaign parameter inputs
- ROI calculation
- Financial breakdown
- Scenario analysis (Conservative, Moderate, Optimistic)
- Recommendations based on ROI

**How to Use:**

1. **Enter Customer Base Parameters:**
   - Total Customers
   - Current Churn Rate (%)
   - Average Customer Lifetime Value ($)

2. **Enter Campaign Parameters:**
   - Campaign Cost per Customer ($)
   - Expected Churn Reduction (%)
   - Campaign Success Rate (%)

3. **Review Results:**
   - Customers at Risk
   - Potential Saves
   - Net Benefit
   - ROI (%)

4. **Analyze Scenarios:**
   - Compare Conservative, Moderate, and Optimistic scenarios
   - Review ROI comparison chart

5. **Read Recommendations:**
   - Green: Excellent ROI (>100%) → Proceed immediately
   - Blue: Good ROI (50-100%) → Proceed with campaign
   - Yellow: Marginal ROI (0-50%) → Optimize first
   - Red: Negative ROI → Reconsider strategy

**Example Calculation:**
```
Input:
- 7,000 customers
- 26.5% churn rate
- $1,500 customer value
- $50 campaign cost per customer
- 30% churn reduction
- 70% success rate

Output:
- 1,855 customers at risk
- 389 potential saves
- $533,500 net benefit
- 1,067% ROI → EXCELLENT!
```

---

### 5. 🔍 Model Monitoring

**Purpose:** Track model performance over time

**Features:**
- Current status metrics
- Performance trends (last 30 days)
- Prediction volume tracking
- Data drift detection
- Alerts and warnings
- Monitoring recommendations

**How to Use:**

1. **Check Current Status:**
   - Review Accuracy, Precision, Recall, F1-Score
   - Look for green (improving) or red (declining) deltas

2. **Analyze Performance Trends:**
   - Examine the multi-line chart
   - Look for sudden drops or unusual patterns
   - Compare metrics over time

3. **Monitor Prediction Volume:**
   - Check daily prediction counts
   - Identify usage patterns

4. **Review Alerts:**
   - Green: Model healthy, no action needed
   - Yellow/Red: Performance degradation detected

5. **Check Data Drift:**
   - Review feature drift scores
   - Features with drift > 0.2 need attention
   - Features with drift > 0.1 should be monitored

6. **Follow Recommendations:**
   - Daily: Monitor volume and check for anomalies
   - Weekly: Analyze trends and review errors
   - Monthly: Full evaluation and potential retraining

---

## 🎨 Tips and Best Practices

### For Risk Analysis
- Always fill in all fields accurately
- Use actual customer data for best results
- Focus on high-risk customers (>70% probability)
- Combine with ROI simulator for campaign planning

### For ROI Simulator
- Start with conservative estimates
- Test multiple scenarios
- Consider customer lifetime value carefully
- Factor in campaign execution costs

### For Monitoring
- Check daily for production systems
- Set up alerts for metric drops > 5%
- Investigate data drift scores > 0.2
- Retrain model if performance degrades consistently

## 🔧 Troubleshooting

**Dashboard won't load:**
- Check that all dependencies are installed
- Verify model files exist in `../models/`
- Check console for error messages

**Prediction fails:**
- Ensure all 25 features are provided
- Check data types match expected format
- Verify model files are not corrupted

**Charts not displaying:**
- Refresh the page
- Check browser console for JavaScript errors
- Try a different browser

## 📞 Support

For issues or questions:
1. Check this guide first
2. Review the API documentation
3. Check the GitHub repository issues
4. Contact the development team

