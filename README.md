# 506-project

## Project Description
We aim to measure the accuracy of the Terrier Transit app in predicting wait times and how well the buses follow their schedules. This project will compare Terrier Transit data with live data from the **TransLoc API**, which provides real-time bus locations.

---

## Goals
- Quantify the accuracy of the Terrier Transit app for:
  - Any given day (Monday through Friday)
  - Any given stop from 8 AM to 6 PM (most active times on campus)

---

## Data Collection
- **Bus Routes Tracked**:
  - Charles River - Medical Campus
  - Fenway
  - Comm Ave
- **Collection times**:
  - Our data will be collected during regular school hours, when class is in session, so there should be no anomalies in the data since major events will happen outside of our selected time frame.
  - e.g. Fenway games are suspended for the rest of the season and concerts happen later at night
 
- **Margin of Error**:
  - Acceptable margin of error for wait time is around 5 minutes
  - Considering the minimum time between classes being 15 minutes, this margin of error allows the bus to be late but arrive to the next stop within that timeframe

- **Data Sources**:
  - **TransLoc API**: Bus locations and bus capacity
  - **Terrier Transit App**: Wait times and bus schedules
  
 
---

## Data Modeling
We will design a database schema that includes:
- Bus Routes
- Bus Stops
- Scheduled Trips
- Actual Trips
- Wait Times
- Bus Locations

---

## Data Visualization
We will use a scatter plot to compare predicted vs. actual wait times at each stop:
- **X-axis**: Predicted time
- **Y-axis**: Actual time
- **Color-coded points**: Represent individual stops

---

## Test Plan
- **Training Data**: Gathered over 3 weeks in October
- **Testing Data**: Collected during 3 weeks in November
