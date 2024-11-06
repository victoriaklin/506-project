# 506 Project Proposal

## Project Description
This project aims to evaluate the accuracy of the Terrier Transit app in predicting wait times and how reliably buses adhere to their schedules. We will compare Terrier Transit’s predictive data with live data from the **TransLoc API**, which provides real-time bus locations and capacity information. The project will focus on popular bus routes servicing campus and nearby areas to determine how effectively the app serves the needs of the campus community.

---

## Goals
- Quantitatively assess the Terrier Transit app’s accuracy for:
  - Weekday predictions (Monday through Friday).
  - Common stops from 8 AM to 6 PM, the busiest times on campus.
- Establish metrics to determine how often buses arrive within an acceptable timeframe and identify discrepancies between predicted and actual wait times.

---

## Data Collection
- **Bus Routes Tracked**:
  - Charles River - Medical Campus (Comm Ave - BU Medical)
  - Fenway route
  - Comm Ave route
  - We have yet to properly parse the unique ID for the Comm Ave Bus as it requires attentive live tracking of specific route coordinates (the Comm Ave loop does not have unique stops as its route is a subset of all bus routes).
- **Collection Times**:
  - Data will be gathered during regular school hours on weekdays, avoiding anomalies caused by events like Fenway games or concerts that occur outside our monitoring window. This schedule ensures that our data reflects standard campus traffic conditions.
- **Margin of Error**:
  - An acceptable margin of error for wait time predictions is set to around 5 minutes. This benchmark allows for minor delays while still providing students enough time to get to the next stop within the 15-minute class transition period.
- **Data Sources**:
  - **TransLoc API**: Provides real-time bus location data, including capacity metrics, which will help in analyzing trends during peak hours.
  - **Terrier Transit App**: Used to gather data on predicted wait times and official bus schedules, facilitating a direct comparison with live metrics from TransLoc.

---

## Data Modeling
We will design a database schema to handle and store the relevant information for in-depth analysis. Key entities in the database will include:
- **Bus Routes**: The specific campus bus routes being analyzed.
- **Bus Stops**: Locations where wait times and arrival adherence will be assessed.
- **Scheduled Trips**: Planned trip data as per the Terrier Transit app, allowing us to compare expected vs. actual performance.
- **Actual Trips**: Real-time trip data recorded from the TransLoc API.
- **Wait Times**: Predicted vs. observed wait times at each stop to gauge predictive accuracy.
- **Bus Locations**: Real-time bus positions to analyze adherence to planned routes and timing.

---

## Data Visualization
To interpret the data meaningfully, we will use various visualizations:
- **Scatter Plot**: To compare predicted vs. actual wait times at each stop.
  - **X-axis**: Predicted wait time by the Terrier Transit app.
  - **Y-axis**: Actual observed wait time based on TransLoc data.
  - **Color-coded points**: Each point represents a different bus stop, allowing us to identify trends or outliers at specific locations.

- **Box Plot (Whisker Plot)**: To show the distribution of arrival delays for each bus route, helping us understand consistency in delays.
  - Each bus route will have a separate box plot for clarity, visualizing the median, interquartile range, and potential outliers in arrival times.

These visualizations will provide insights into the accuracy and reliability of the Terrier Transit app, highlighting patterns in arrival delays and enabling us to quantify discrepancies between predicted and actual wait times.
![image](https://github.com/user-attachments/assets/6a3dd499-ca30-4486-b67c-bf017709798c)
![image](https://github.com/user-attachments/assets/32c67e4d-4e90-4994-83b4-42dc896ae53d)
![image](https://github.com/user-attachments/assets/badca230-e53d-44b6-b83c-011a937c239f)
![image](https://github.com/user-attachments/assets/27901b0b-9637-48e1-bd08-02e799b2a93d)
![image](https://github.com/user-attachments/assets/29e420df-066f-4665-a518-11da5612ce65)
![image](https://github.com/user-attachments/assets/238d0f85-0c3b-4bbb-8b5e-c97f8df0398c)
![image](https://github.com/user-attachments/assets/54b583c0-8156-46cf-88bd-15a698807f01)
![image](https://github.com/user-attachments/assets/398165d4-bb15-48f4-8458-4159598d2675)
![image](https://github.com/user-attachments/assets/3e5563c1-77f5-48b5-8383-e90ffb4ebb14)



---

## Test Plan
- **Training Data**: Data collected over a 3-week period in October to establish baseline measurements of transit behavior and app accuracy.
- **Testing Data**: Additional data collected over 3 weeks in November, used to validate the accuracy of Terrier Transit predictions and identify any performance shifts over time.

This approach ensures a robust dataset for testing and evaluating predictive models for wait time and schedule adherence, ultimately helping to improve Terrier Transit’s reliability for users on campus. The preliminary code is available in the project repository for review and iteration as needed.
