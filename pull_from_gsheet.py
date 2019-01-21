import json
import urllib.request

def pull_from_gsheet(config, api_key):
    gsheet_pattern='https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{tab_name}!{range}?key={api_key}'

    sheet_id = config['sheet_id']
    for file_name, params in config['file_list'].items():
        tab_name = params['tab_name']
        cell_range = params['range']

        full_url = gsheet_pattern.format(sheet_id=sheet_id, tab_name=tab_name, range=cell_range, api_key=api_key)
        print("Retrieving data from URL [%s]" % (full_url))
        resp = urllib.request.urlopen(full_url)
        data = json.loads(resp.read())
        entries = [ val[0].encode('utf-8') if len(val) > 0 else b'' for val in data['values'] ]
        with open(file_name, 'wb') as fp:
            fp.write(b'\n'.join(entries))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Pull translation from Google Drive using REST API')
    parser.add_argument('config_file', type=str, nargs=1, help='Configuration file for the retrieval')
    parser.add_argument('api_key', type=str, nargs=1, help='Your Google Sheet API KEY')
    args = parser.parse_args()
    with open(args.config_file[0]) as fp:
        config = json.load(fp)
    api_key = args.api_key[0]

    pull_from_gsheet(config, api_key)
