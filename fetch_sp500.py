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

def fetch_existing_sp500_table(file_path: str):
    pass

def write_to_file(file_path: str, table: pd.DataFrame):
    pass

def main():
    URL: str = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table: pd.DataFrame = fetch_sp500_table(URL)

    existing_sp500_table = fetch_existing_sp500_table('sp500.csv')

    df = pd.read_csv('sp500.csv', on_bad_lines='warn')

    # sp500_table_diff = sp500_table[~sp500_table.Symbol.isin(existing_sp500_table.Symbol)]

    # print(sp500_table_diff)

    # write_to_csv('sp500.csv', sp500_table)
    # write_to_markdown('README.md', sp500_table)

if __name__ == '__main__':
    main()
