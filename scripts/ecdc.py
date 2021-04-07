import argparse
from datetime import datetime

import pycountry
import pandas as pd

VACCINE_MAPPER = {
    'COM': 'Pfizer/BioNTech',
    'MOD': 'Moderna',
    'CN': 'CNBG',
    'SIN': 'Sinovac',
    'SPU': 'Sputnik V',
    'AZ': 'AstraZeneca',
    'UNK': 'UNKNOWN'
}
CSV_URL = ('https://opendata.ecdc.europa.eu/'
           'covid19/vaccine_tracker/csv/data.csv')
SOURCE_URL = ('https://www.ecdc.europa.eu/en/publications-data/'
              'data-covid-19-vaccination-eu-eea')


def filter_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """ Filter rows for specific country """
    df_sub = df.loc[(df['ReportingCountry'] == country)
                    & (df['TargetGroup'] == 'ALL')]

    df_sub.loc[:, 'people_vaccinated'] = df_sub['FirstDose'].cumsum()
    df_sub.loc[:, 'people_fully_vaccinated'] = df_sub['SecondDose'].cumsum()

    total = df_sub['people_vaccinated'] + df_sub['people_fully_vaccinated']
    df_sub.loc[:, 'total_vaccinations'] = total

    df_sub.loc[:, 'date'] = [
        min(
            datetime.strptime(week + '-7', '%G-W%V-%u').date(),
            datetime.today().date()) for week in df_sub['YearWeekISO']
    ]
    df_sub.loc[:, 'total_received'] = (
        df_sub['NumberDosesReceived'].cumsum().astype('int'))
    df_sub.loc[:, 'location'] = pycountry.countries.get(alpha_2=country).name
    df_sub.loc[:, 'vaccine'] = [
        VACCINE_MAPPER.get(vaccine, 'UNKNOWN') for vaccine in df_sub['Vaccine']
    ]
    df_sub.loc[:, 'source_url'] = SOURCE_URL
    df_filtered = df_sub[[
        'location', 'date', 'vaccine', 'source_url', 'total_vaccinations',
        'people_vaccinated', 'people_fully_vaccinated', 'total_received'
    ]]
    return df_filtered


def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    """ Aggregate data per week """
    df_agg = df.groupby(['location', 'date', 'source_url']).agg({
        'vaccine':
        lambda x: ','.join(sorted(x.unique())),
        'total_vaccinations':
        'max',
        'people_vaccinated':
        'max',
        'people_fully_vaccinated':
        'max',
        'total_received':
        'max'
    })
    return df_agg.reset_index()


def main(country_name: str, output_path: str) -> None:
    """ Get country data and write output """
    df = pd.read_csv(CSV_URL)
    country_code = pycountry.countries.get(name=country_name).alpha_2
    df_country = aggregate_data(filter_data(df, country_code))
    df_country.to_csv(output_path, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Aggregate ECDC Data - COVID-19 vaccination in the EU/EEA')
    parser.add_argument('--country-name', help="Country name")
    parser.add_argument('--output-path', help="Path to output file")
    args = parser.parse_args()
    main(country_name=args.country_name, output_path=args.output_path)
