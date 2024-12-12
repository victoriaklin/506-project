## Project Description
This project aims to evaluate the accuracy of the Terrier Transit app in predicting wait times and how reliably buses adhere to their schedules. We will compare Terrier Transit’s predictive data with live data from the **TransLoc API**, which provides real-time bus locations and capacity information. The project will focus on popular bus routes servicing campus and nearby areas to determine how effectively the app serves the needs of the campus community.

## How to Build
- Start by git cloning this repository
- In the terminal of the cloned repo, run "make install" and "make run"
- Once completed, the console will display the localhost link to the Flask app
- Enter the localhost, and the Flask app will be displayed

## Goals
- Quantitatively assess the Terrier Transit app’s accuracy for:
  - Weekday predictions (Monday through Friday).
  - Common stops from 8 AM to 6 PM, the busiest times on campus.
- Establish metrics to determine how often buses arrive within an acceptable timeframe and identify discrepancies between predicted and actual wait times.

## Test Plan
- **Training Data**: Data collected over a 3-week period in October to establish baseline measurements of transit behavior and app accuracy.
- **Testing Data**: Additional data collected over 3 weeks in November, used to validate the accuracy of Terrier Transit predictions and identify any performance shifts over time.

This approach ensures a robust dataset for testing and evaluating predictive models for wait time and schedule adherence, ultimately helping to improve Terrier Transit’s reliability for users on campus. The preliminary code is available in the project repository for review and iteration as needed.

---

## Data Collection
- **Bus Routes Tracked**:
  - Charles River - Medical Campus (Comm Ave - BU Medical)
  - Fenway route
  - Comm Ave route
- **Collection Times**:
  - Data was gathered during all hours that the BU buses were running. However, only the data from 8am to 6pm were analyzed. Hence avoiding anomalies caused by events like Fenway games or concerts that occur outside our monitoring window. This schedule ensures that our data reflects standard campus traffic conditions.
- **Margin of Error**:
  - An acceptable margin of error for wait time predictions is set to around 3 minutes. This was determined as per the estimated TransLoc bus arrival times. 

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
  - Categorized each delay into three groups: On-Time (±3 min), Early (>3 min), and Late (>3 min).
  - This was done by applying conditional logic to the delay column in the code, creating a new delay_category column.
- **Grouping Data by Bus Type**:
  - Grouped data by the bus_type and time of day in preparation for comparative analysis of bus lines. 
- **Combining All Data**:
  - Concatenated data for all bus lines into a single DataFrame, combined_merged_df enabling us to visualize and compare each bus line’s delay distribution and performance

---

## Data Modeling
We will design a database schema to handle and store the relevant information for in-depth analysis. Key entities in the database will include:
- **Bus Routes**: The specific campus bus routes being analyzed.
- **Bus Stops**: Locations where wait times and arrival adherence will be assessed. This serves as the point of reference for the API visualizations of the routes. 
- **Scheduled Trips**: Planned trip data as per the Terrier Transit app, allowing us to compare expected vs. actual performance.
- **Actual Trips**: Real-time trip data recorded from the TransLoc API.
- **Wait Times**: Predicted vs. observed wait times at each stop to gauge predictive accuracy.
- **Bus Locations**: Real-time bus positions to analyze adherence to planned routes and timing.

---

## Flask App
On our Flask app are the result of our visualizations of the collected data (each bus and route)
- Displays the static geolocations of each stop, and produces a static map of each route
- Overtop, displays the actual API movement data of the bus on the route, indicating if it is off its path as well as any deviation from the schedule 

---

## Data Cleaning

Data to model the bus routes was cleaned by ensuring that the animations produced were only depicting the tracked buses with the highest location accuracy. As location drifting was an issue we experienced. We created an exception point of the Hyatt stop to filter out all night buses (keeping it between 8am-6pm). We also returned the graphs with the lowest overall distance to each stop to ensure accuracy. 

---

## Data Visualization
To interpret the data meaningfully, we will use various visualizations:
- **Histograms**: To visualize the delay distribution of each bus line. 
  - **Y-axis**: The delay in minutes
  - **X-axis**: Frequency distribution of the delays 
  - **Color-coded points**: Each point represents a different bus stop, allowing us to identify trends or outliers at specific locations.

- **Bar Graph**: Shows the average delay in minutes for each bus stop for each bus line
  - **Y-axis**: The mean delay in minutes
  - **X-axis**: The stop names

- **Bar Graph**: Shows a comparison of the average delay in minutes between all three bus lines.
  - **Y-axis**: The average delay in minutes
  - **X-axis**: The bus line names

These visualizations will provide insights into the accuracy and reliability of the Terrier Transit app, highlighting patterns in arrival delays and enabling us to quantify discrepancies between predicted and actual wait times.

## Data Interpretation and Claims

## Histograms
![buhis](https://github.com/user-attachments/assets/5981bd5f-ddbc-4153-971d-a44d8e9fb514)
- **1BU**: Shows a comparison of the average delay in minutes between all three bus lines. 

The histogram shows the frequency of delays in minutes for the 1BU bus route, with a 3-minute threshold (red dashed line). Delays range from -60 minutes to +60 minutes, with the highest frequency of delays slightly before the threshold. The delay distribution is roughly symmetrical around zero, suggesting that the 1BU bus frequently arrives either slightly early or slightly late, and extreme delays/early arrivals are relatively uncommon.

![commhis](https://github.com/user-attachments/assets/3ef09746-a112-4db9-882d-c84465a3a930)
- **Comm. Ave**: Shows a comparison of the average delay in minutes between all three bus lines.

This histogram illustrates the delay frequency for the Comm Ave bus route. Delays are again centered around a 3 minute threshold, with a range from -60 to +60 minutes. The delay distribution appears more irregular than for the 1BU, with peaks across the delay spectrum. This irregularity may indicate inconsistent scheduling or traffic conditions affecting the route. 

![fenwayhis](https://github.com/user-attachments/assets/54c7a6af-6a83-43d4-a4af-34f65198fb36)
- **Fenway**: Shows a comparison of the average delay in minutes between all three bus lines.

The graph shows delays for the Fenway bus route, spanning a range of -60 to +60 minutes. The red dashed line highlights the 3-minute threshold for on-time performance. The Fenway delay distribution demonstrates a relatively flat pattern compared to the other routes, suggesting an even spread of delay times across the spectrum. This could point to persistent challenges in meeting schedule expectations, with fewer sharp peaks indicating consistent delays rather than sporadic ones.

## Bar graphs

![avgdelaybu](https://github.com/user-attachments/assets/c33bd69b-eb1c-40ad-922c-2fcf294ca45d)
- **1BU**: Shows the average delay per stop in minutes 
1BU has a strong performance across most stops, with average delays rarely exceeding 1 minute. Early arrivals at several stops suggest possible padding in the schedule. The few late outliers are concentrated at the beginning of the route. This proficiency can most likely be attributed to the 1BU having a greater number of buses as compared to Fenway (2-3 buses) Comm. Ave (1-2 buses). 

![avgdelaycomm](https://github.com/user-attachments/assets/4eed8147-505a-419a-8d3f-93812f385bb4)
- **Comm. Ave**: Shows the average delay per stop in minutes 
While most Comm Ave stops have average delays under 2 minutes, endpoints like Central/St Mary's and Agganis Arena show larger 3-5 minute lags. Stop-to-stop variability is higher than 1BU, showing some inconsistency.

![avgdelayfenway](https://github.com/user-attachments/assets/6242d06f-386c-4f1e-941b-2f8d982c0705)
- **Fenway**: Shows the average delay per stop in minutes 
Fenway has the highest delays at the stop level, routinely averaging 5-10 minutes behind schedule. Delays worsen progressively along the route, with a 13 minute average at Buick St corner. No early arrivals counterbalance these significant lags.

![avgdelayall](https://github.com/user-attachments/assets/0bddb2ee-2353-466e-a440-0f6aa281ba45)
- **All**: Shows a comparison of the average delay in minutes between all three bus lines.
The route-level comparison of average delays reveals a clear hierarchy in reliability:
1BU: With a slightly negative average delay, 1BU seems to be the most punctual route. Its early arrivals suggest efficient operations and minimal traffic impacts.
Comm Ave: Averaging about 30 seconds behind schedule, Comm Ave demonstrates good reliability. While not quite as precise as 1BU, its delays are minor.
Fenway: Fenway stands out with an average delay nearing 3 minutes. This significant lag indicates systemic issues with timeliness on this route.
The Terrier Transit app appears to predict 1BU and Comm Ave arrivals well, but struggles with Fenway's longer delays.
---

## Conclusion 

This project quantitatively assessed the accuracy of the Terrier Transit app's predictions for weekday bus arrivals at common stops between 8 AM and 6 PM. By comparing real-time TransLoc data to Terrier Transit's schedules, we found that the app's accuracy varied significantly across routes, with 1BU predictions being the most reliable, Comm Ave predictions showing some inconsistency, and Fenway predictions exhibiting the largest discrepancies. Our analysis established that buses on the 1BU route arrived within 3 minutes of their predicted times most often, while Fenway buses frequently exceeded this threshold, especially at later stops. These findings provide a data-driven basis for identifying areas where Terrier Transit's predictions need improvement and where interventions could be targeted to enhance overall bus reliability during peak hours.

