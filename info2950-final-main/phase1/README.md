# Phase 1: Project Brainstorming

## Group Name
AAH

## Project Workspace

https://github.coecis.cornell.edu/asy28/info2950-final

## Project Ideas

### 1. Food Recalls and Foodborne Outbreaks

#### Research Question

How have FDA food recalls and CDC-reported foodborne outbreaks changed over time, and how do these patterns differ across pathogens and recall classifications?

#### Short Description of the Dataset

We are interested in comparing food recalls with foodborne disease outbreaks in the United States.

The FDA data contains information about food recalls, including recall dates, companies, products, reasons for recall, recall classifications, and recall status. The CDC data contains information about reported foodborne outbreaks.

We are especially interested in pathogens such as Salmonella, Listeria, and E. coli because they appear in both sources. Combining the datasets would allow us to compare how recall activity and outbreak activity vary across pathogens and over time.

#### Data Availability and Sources

Our first source is the FDA Enforcement Reports API (iRES):

- FDA Enforcement Reports API:
  https://www.accessdata.fda.gov/scripts/ires/apidocs/

- FDA Enforcement Report API Definitions:
  https://www.fda.gov/safety/enforcement-reports/enforcement-report-api-definitions

The API provides fields such as recall initiation date, company name, product description, reason for recall, recall classification, recall status, recall number, recall event ID, and product ID.

We obtained FDA API credentials and successfully retrieved 39,833 food recall records.

Our second source is CDC National Outbreak Reporting System (NORS) data, available through the CDC BEAM Dashboard:

- CDC BEAM Dashboard:
  https://www.cdc.gov/beam/dashboard/

- CDC NORS Dataset:
  https://data.cdc.gov/dataset/NORS/5xkq-dg7x

CDC makes the NORS data available for download. We would use the historical outbreak information to examine foodborne outbreak activity by time and pathogen.

#### Data Collection Method

For the FDA data, we used Python and the FDA Enforcement Reports API. The API requires an approved email address as the Authorization-User and an FDA-generated Authorization-Key. We successfully obtained credentials and authenticated with the API. The FDA documentation does not list a fee for API use.

Because the API limits the number of records returned in one request, we used pagination to retrieve the records in multiple batches and combined them into a Pandas DataFrame.

For the CDC data, we would download the NORS data provided through CDC's BEAM data page and select the variables needed for our analysis.

#### Plan for Combining the Datasets

We would not attempt to match each FDA recall to one specific CDC outbreak because a recall and an outbreak are different types of events.

Instead, we would aggregate the two datasets using the shared variables:

- year
- pathogen

For example, we could compare the number of FDA recalls involving Salmonella in a given year with the number of CDC-reported Salmonella outbreaks during that year.

Combining the datasets would allow us to compare regulatory recall activity with reported outbreak activity, which neither dataset can show on its own.

#### Data Cleaning Plan

During Phase II, we would standardize dates and pathogen names across both datasets.

The FDA data does not contain a separate structured pathogen variable, so we would identify pathogens such as Salmonella, Listeria, and E. coli from the reason-for-recall text.

We would also check for missing values, duplicate records, inconsistent pathogen names, and differences in date coverage before aggregating the data by year and pathogen.

#### Data Trustworthiness

The FDA recall data is collected and maintained by the U.S. Food and Drug Administration. Because the records come directly from the federal agency responsible for maintaining FDA recall information, we consider it a reliable primary source.

The CDC outbreak data is collected through the National Outbreak Reporting System and made available by the Centers for Disease Control and Prevention. The CDC is the federal public-health agency responsible for tracking and investigating disease outbreaks, making it an appropriate source for foodborne outbreak information.

#### Data Quality and Accuracy Concerns

The FDA and CDC datasets capture different types of information. An FDA recall is a regulatory action involving a product, while a CDC outbreak represents reported illnesses investigated by public-health agencies. Therefore, we would not assume that every recall corresponds to an outbreak or that every outbreak results in a recall.

The FDA data also does not provide pathogen type as a separate structured variable, so our pathogen categories would be derived from the reason-for-recall text. We would manually review a sample of these classifications to check their accuracy.

We would also examine missing values, duplicate records, unusual dates, and differences in reporting coverage before conducting our analysis.

### 2. Homeless Population and Housing Costs

#### Research Question

How is the rate of homelessness associated with rental housing costs across U.S. states, and has this relationship changed over time?

#### Short Description of the Dataset

We are interested in determining whether states with higher median rents also tend to have higher rates of homelessness. We could also examine whether increases in rent within a state are associated with increases in its homelessness rate over time.

The first dataset would contain the annual Point-in-Time estimates of homelessness published by the U.S. Department of Housing and Urban Development. These data report the number of people experiencing homelessness on a single night in January. The estimates include the total homeless population as well as subgroups such as sheltered and unsheltered people, families, veterans, and chronically homeless individuals.

The second dataset would come from the U.S. Census Bureau’s American Community Survey. It would provide annual state-level estimates of median gross rent and total population. Gross rent includes rent and certain utility costs, making it a useful measure of the housing costs faced by renters.

#### Data Availability and Sources

Our first source is HUD’s Point-in-Time and Housing Inventory Count data: https://www.huduser.gov/portal/datasets/ahar.html 

HUD provides downloadable spreadsheets containing annual PIT estimates from 2007 onward. The files contain estimates at the national, state, and Continuum of Care levels. We would use the state-level records so that they can be matched consistently with Census data.

Our second source is the Census Bureau’s American Community Survey five-year estimates:
- ACS Five-Year Data and API Information: https://www.census.gov/data/developers/data-sets/acs-5year.html
- 2024 ACS API: https://api.census.gov/data/2024/acs/acs5.html
- ACS Median Gross Rent: https://api.census.gov/data/2024/acs/acs5/groups/B25064.html
- ACS Total Population: https://api.census.gov/data/2024/acs/acs5/groups/B01003.html

The ACS API provides annual 5-year estimates for all states. We would retrieve median gross rent (B25064_001E) and total population (B01003_001E) from the ACS API.

#### Data Collection Method

We would download the annual state-level PIT spreadsheets from HUD and combine the files using Python and Pandas. We would retain variables such as year, state, total homeless population, sheltered population, and unsheltered population.

We would collect ACS data using the Census API. The Census API requires an API key, which can be requested free of charge from the Census Bureau.

#### Plan for Combining the Datasets

We would join the datasets based on state and year. Because states differ substantially in population, we would calculate a homelessness rate rather than compare only raw counts: homelessness rate per 10,000 residents = (PIT homeless population / ACS total population) × 10,000 

The resulting dataset would have one observation for each state-year. Possible variables would include: state, year, median gross rent, total population, total homeless population, sheltered homeless population, unsheltered homeless population, homelessness rate per 10,000 residents, percentage of the homeless population that is unsheltered, etc. This would let us compare homelessness rates with rent across states and examine changes within states over time.

#### Data Cleaning Plan

We would standardize state names, abbreviations, and year variables across the HUD and ACS files. We would check whether the datasets include Washington, D.C. and U.S. territories and decide whether to retain them. We would convert rent, population, and homelessness variables to numeric values and check for missing or suppressed estimates. We would also inspect duplicate state-year observations and confirm that each observation represents the same geographic area.

Because rent changes over time partly due to inflation, we may convert rents into constant dollars using the Consumer Price Index or limit our main analysis to comparisons within the same year. We would also examine the 2021 PIT data separately because COVID-19 disrupted that year’s homelessness count.

#### Data Trustworthiness

The PIT data are published by HUD, the federal agency responsible for coordinating national housing and homelessness programs. Local Continuums of Care collect the underlying information and submit it to HUD. HUD then reviews and compiles the results. HUD is therefore a trustworthy primary source.

The ACS data are collected and published by the U.S. Census Bureau. The ACS uses established probability-sampling and weighting methods and publishes margins of error for its estimates. Because the Census Bureau documents its methodology and conducts extensive quality review, we consider it a trustworthy source for state-level population and housing estimates.

The PIT estimates are also published and discussed in HUD’s Annual Homeless Assessment Report to Congress. We would cite the relevant annual reports when interpreting trends in the data.

#### Data Quality and Accuracy Concerns

The PIT count is an estimate of homelessness on a single night rather than a count of everyone who experiences homelessness during an entire year. Unsheltered homelessness is especially difficult to measure because individuals may be in locations that volunteers cannot find or access. Counting methods and available resources may also differ across states and Continuums of Care.

The COVID-19 pandemic disrupted the 2021 PIT count. HUD did not require all communities to conduct the usual unsheltered count that year, so 2021 may not be directly comparable with other years. We would either exclude 2021 from the main analysis or clearly identify it as an unusual year.

ACS figures are also estimates rather than exact counts. The five-year ACS combines responses collected over a five-year period, so it does not represent conditions at one exact moment.

Finally, an association between rent and homelessness would not prove that rent increases directly caused homelessness. Other factors may influence both variables, such as income, housing supply, unemployment, climate, and local homelessness policies.

### 3. Food Access and Health by Census Tract

#### Research Question

Does low food access go along with worse health, even among tracts with similar income levels?

#### Short Description of the Dataset

A food desert is a neighborhood where residents can't reach affordable, nutritious food because the nearest full-service grocery store is too far away. To see how food access connects to health, we're using two datasets.

The first dataset is the USDA Economic Research Service’s Food Access Research Atlas. Each row covers one U.S. census tract, about 72,000 in total, and shows whether the tract counts as low-income and low-access, how far residents live from a supermarket, and how many households lack a car.

The CDC publishes the second, CDC PLACES, on data.cdc.gov, and we're using its 2023 tract release. Each row there also covers one census tract, with estimated rates of obesity, diabetes, high blood pressure, and other health measures.

#### Data Availability and Sources

We'll get the Food Access Research Atlas from the USDA's Economic Research Service website (https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data), where you can download the full dataset for free as an Excel file.

CDC PLACES 2023 lives on data.cdc.gov, with its catalog listing at https://catalog.data.gov/dataset/places-census-tract-data-gis-friendly-format-2023-release, and it downloads for free as a CSV.

#### Data Collection Method

Neither source requires an account, so we can click download and start working with both files right away.

#### Plan for Combining the Datasets

The Atlas tells us where food access is poor but says nothing about health, and PLACES tells us where health is poor but says nothing about food access. By matching the two on tract ID, we can ask a question neither one answers alone: does low food access go along with worse health, even among tracts with similar income levels?

#### Data Cleaning Plan

We'll keep only the columns we need, rebuild both tract IDs as 11-digit text so leading zeros line up, and join the datasets on that ID. Tracts that fail to match would signal a boundary mismatch, so we'll count them. We'll also drop rows missing key income or health values, review small-population tracts and confidence intervals to check how reliable the PLACES estimates are, and run summary statistics and histograms to identify unusual values before analysis.

#### Data Trustworthiness

The USDA's Economic Research Service, a federal agency, built the Atlas and publishes its full methods, so anyone can check how it defines low access and low income. ERS builds its 2019 supermarket list from SNAP retailer records and a commercial directory of grocery stores, then pairs it with Census population and income data.

The CDC produces PLACES, publishes its methods, and compared its model-based estimates with direct survey estimates to evaluate their accuracy.

#### Data Quality and Accuracy Concerns

The Large Retailer Access Map uses 2019 store data, so it may not reflect stores that opened or closed after 2019. USDA also provides a newer SNAP-based retailer dataset, so we would clearly state which food-access dataset we use.
PLACES health measures are model-based estimates. The CDC builds each one with a statistical model that combines a national phone survey with Census data, and that model gives less reliable numbers for tracts with small populations.

## Questions for Reviewers
- Are any of our research questions too broad or too narrow for the scope of the final project? 
- Do our proposed dataset combinations seem appropriate for the type of analysis expected in this course?
- Are there any major methodological issues with comparing data collected by different agencies or across different time periods?
- Are there any limitations in our current data sources that would make one of these ideas difficult to carry through the full project?
- Are there any issues with our chosen unit of analysis that could affect the results later?
- Are there any risks in our current plans that could make the analysis difficult to complete or interpret later?
- Are there any decisions we should make now that would be difficult to change once we start Phase II?
- Would you recommend changing how we combine any of the datasets?
- Are there any datasets we are using that you would recommend replacing with a stronger source?
- Are any of our research questions framed in a way that could make the final analysis too descriptive rather than analytical?
