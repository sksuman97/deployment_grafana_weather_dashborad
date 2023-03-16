# Live_grafana_weather_dashborad
---
This project aims to build a live Grafana dashboard using TimescaleDB as the database. To populate the database, an API script was run. The project utilizes containers to run three different processes and uses Docker Compose to streamline the development and deployment process. This is an end-to-end project that covers everything from development to deployment, allowing for a smooth transition between stages. By using containers and Docker Compose, the project ensures consistency and repeatability throughout the entire process, making it easier to manage and scale in the future. With the Grafana dashboard, users will be able to visualize data in real-time, providing valuable insights and helping to make data-driven decisions. Overall, this project is a great example of how to build a scalable, end-to-end system that is both efficient and effective


It consists of 3 components:
---

1. Timescale_DB --> Used for storing live weather data locally
2. Weather data fetching API --> It fetches weather data and populates DB
3. Live Grafana dashboard  --> It takes data from DB and plots interactive dashboard

All the 3 processes are deployed independently.

Sample Dashboard
---
![image](https://user-images.githubusercontent.com/64405940/225702029-ac51a41d-5365-428d-9072-d1938b6e644e.png)
