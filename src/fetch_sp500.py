import pandas as pd
import requests

def fetch_sp500_table(url: str) -> pd.DataFrame:
    response = requests.get(url)
    return pd.read_html(response.text)[0]

def write_to_csv(file_path: str, table: pd.DataFrame):
    with open(file_path, 'w') as f:
        f.write('Symbol,Company Name\n')
        for row in table.itertuples():
            f.write(f'{row.Symbol},{row.Security}\n')

def main():
    ## Extract
    URL: str = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table: pd.DataFrame = fetch_sp500_table(URL)

    ## Transform
    # eliminate commas in company names by add double quotes
    sp500_table['Security'] = sp500_table['Security'].apply(lambda x: f'"{x}"')

    ## Load
    write_to_csv('sp500.csv', sp500_table)

if __name__ == '__main__':
    main()
