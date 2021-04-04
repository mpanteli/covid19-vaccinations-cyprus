<head>
	<meta name="description" CONTENT="COVID19 Vaccinations Cyprus, dataset and visualisation. Source: Official data published by http://pio.gov.cy/coronavirus/ and aggregated by the COVID19 Vaccinations Cyprus project.">
	<meta name="google-site-verification" content="-vzF49g2tzy9DFe2Y81uQ8StmDZWwe7mi-sDCutMMag" />
</head>

# COVID19 Vaccinations Cyprus

Data and visualisations for COVID-19 vaccinations in Cyprus. 

Data aggregated from: 
- [official reports published by the Cyprus Press and Information Office](https://www.pio.gov.cy/coronavirus/categories/emvoliasmoi-kata-tou-koronoiou) [in Greek]
- [ECDC - Data on COVID-19 vaccination in the EU/EEA](https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea)

## Visualisations

- See details of the vaccination progress in Cyprus in [these graphs](https://mpanteli.github.io/covid19-vaccinations-cyprus/)
- See how Cyprus compares with other EU countries in [this graph by Our World In Data](https://ourworldindata.org/coronavirus-data-explorer?zoomToSelection=true&time=latest&country=AUT~BEL~BGR~CYP~CZE~DEU~DNK~ESP~EST~FIN~FRA~GRC~HRV~HUN~IRL~ITA~LTU~LUX~LVA~MLT~NLD~POL~PRT~ROU~SVK~SVN~SWE~EuropeanUnion&region=World&vaccinationsMetric=true&interval=total&perCapita=true&smoothing=0&pickerMetric=total_vaccinations_per_hundred&pickerSort=desc)

## Datasets and schemas

- **Vaccination doses administered** [[CSV](data/Cyprus.csv) | [schema](data/Cyprus_schema.csv)]: Tracks the number of vaccination doses administered in Cyprus. 
- **Weekly vaccination capacity** [[CSV](data/vaccination_capacity.csv) | [schema](data/vaccination_capacity_schema.csv)]: Tracks the number of active vaccination units and vaccination doses administered every week. 
- **Vaccination eligibility by age group** [[CSV](data/vaccination_by_population_age.csv) | [schema](data/vaccination_by_population_age_schema.csv)]: Tracks the number of people eligible for vaccination based on age group criteria. 
- **Vaccination doses delivered** [[CSV](data/Cyprus_ecdc.csv) | [schema](data/Cyprus_ecdc_schema.csv)]: Tracks the number of doses delivered to Cyprus. 

## Scripts

Get the latest numbers for Cyprus from ECDC Data:
```
python scripts/ecdc.py --country-name Cyprus --output-path data/Cyprus_ecdc.csv
```

## License

The data and visualisations created by the COVID19 Vaccinations Cyprus project are licensed under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/). 