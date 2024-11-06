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

## Data Processing
- **Filtering by Route ID**:
  - Extracted data for each bus line by filtering based on specific route_id values so we can isolate each bus line's data for analysis.
- **Timestamp Conversion**:
  - Each bus arrival record included a timestamp, which we converted to a datetime format using pd.to_datetime so we can make comparisons and calculations
- **Delay Calculation**:
  - Calculated delays by subtracting the scheduled arrival time from the actual arrival time for each record, creating the delay column representing the delay in minutes.
- **Categorizing Delays**:
  - Categorized each delay into three groups: On-Time (±5 min), Early (>5 min), and Late (>5 min).
  - This was done by applying conditional logic to the delay column in the code, creating a new delay_category column.
- **Grouping Data by Bus Type**:
  - Grouped data by the bus_type and time of day in preparation for comparative analysis of bus line. 
- **Combining All Data**:
  - Concatenated data for all bus lines into a single DataFrame, combined_merged_df enabling us to visualize and compare each bus line’s delay distribution and performance

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

This histogram shows the distribution of delays for the 1BU bus. The x-axis represents the delay time in minutes, and the y-axis shows the frequency of arrivals for each delay range. The peak near 0 indicates that 1BU buses are generally on time, with most arrivals clustered around zero delay. This means the 1BU bus has a reliable schedule with minimal deviations. A slight skew to the right shows that when delays do occur, they tend to be positive (late arrivals), but these are infrequent.

![image](https://github.com/user-attachments/assets/badca230-e53d-44b6-b83c-011a937c239f)

This histogram shows the distribution of delays for the Fenway bus. It has multiple peaks spread across the x-axis, suggesting more erratic arrival pattern. The lack of a dominant peak around zero delay indicates lower reliability compared to 1BU. This suggests external factors may influence their punctuality more heavily.

![image](https://github.com/user-attachments/assets/238d0f85-0c3b-4bbb-8b5e-c97f8df0398c)

This scatter plot compares actual arrival times against scheduled times for each bus type. The x-axis represents the scheduled arrival time in minutes since midnight, while the y-axis represents the actual arrival time. The green dashed line represents an ideal on-time arrival where actual time equals scheduled time. 1BU buses mostly cluster close to the green line, showing consistent on-time arrivals across different times of day. Fenway buses, however, are more spread out around the line, indicating higher variability and deviation from the schedule. This scatter plot visually reinforces that 1BU tends to be more reliable, while Fenway has a wider range of delays.

![image](https://github.com/user-attachments/assets/398165d4-bb15-48f4-8458-4159598d2675)

This bar chart shows the average delay for each bus type. The y-axis represents the average delay in minutes, while the x-axis shows each bus type. 1BU has a slightly negative average delay, meaning it tends to arrive slightly early on average. This slight negative delay may indicate efficient scheduling or less congestion along its route. Fenway has a slightly positive average delay, indicating that it tends to be late more often than early. This aligns with our previous observations of its erratic arrival patterns.

![image](https://github.com/user-attachments/assets/3e5563c1-77f5-48b5-8383-e90ffb4ebb14)

This bar chart categorizes each bus’s performance by delay types (on-time, late, early), with the y-axis being the Percentage of arrivals, and the x-axis the Bus types, with color-coded bars representing each delay category. We saw that nearly 80% of 1BU arrivals are on time, which is a significant portion. This high on-time percentage reinforces that 1BU is highly reliable. On the other hand, Fenway has a more even distribution across categories, with approximately 40% on time, and the remaining split between early and late. This spread shows a lower on-time reliability, with more variability in its arrival performance. This breakdown allows us to quickly see which bus line is most consistent. It shows that 1BU is significantly more reliable in adhering to schedules, while Fenway has room for improvement.

---

## Test Plan
- **Training Data**: Data collected over a 3-week period in October to establish baseline measurements of transit behavior and app accuracy.
- **Testing Data**: Additional data collected over 3 weeks in November, used to validate the accuracy of Terrier Transit predictions and identify any performance shifts over time.

This approach ensures a robust dataset for testing and evaluating predictive models for wait time and schedule adherence, ultimately helping to improve Terrier Transit’s reliability for users on campus. The preliminary code is available in the project repository for review and iteration as needed.
