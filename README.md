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
