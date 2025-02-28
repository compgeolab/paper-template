# Data used and produced in this project

This folder contains any data used or produced in this study.

<!--
Data should only be stored if they follow the
[FAIR principles](https://www.go-fair.org/fair-principles/) and are distributed
under an open license, like CC-0 or CC-BY, or in the public domain.
The data license should be clearly stated for each dataset hosted here.
-->

The folder structure here is:

* `raw`: Unprocessed data used in the study.
* `processed`: Processed versions of the raw data, usually stored as
  intermediate results.
* `results`: Final results, datasets, and models produced here.

## Datasets included and their licenses

### Global temperature data

These data are a subset of the original data files from
[Berkeley Earth](https://www.berkeleyearth.org) licensed CC-BY-NC.

This archive contains monthly average temperature records for several countries
(see list below). The data for each country is contained in a CSV file with the
year, month, decimal year, temperature (C), and uncertainty (C). The temperature
is the country-wide average for each month of the year. The decimal year assumes
every month is 1/12 of a year and assigns the datum to the middle of the month.

* `raw/temperature-data.zip`: Archive with all of the temperature time series
  data in CSV format.
