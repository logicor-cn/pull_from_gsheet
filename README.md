### Description

This script is originally created for (supposedly) convenient retrieval of translate text of Chinese localization of Meeple Station from Google Sheet.  But it can easily be used to retrieve any SINGLE COLUMN data from Google Sheet by modifying configuration file feed to the script.

### Prerequisites

- Google Developer account with Google Sheet API and API KEY (Currently free as of Jan 2019).
- Python3

### Instructions

#### Google Developer Account Setup

Refer to https://stackoverflow.com/a/46583300

#### Install Python3

For Windows Users only, you probably do not need instructions if you are not using Windows.

- Go to https://www.python.org/downloads/release and download python3, preferrably 3.6.x
- Install python3, make sure to check "Add python to PATH".

#### Using the script

- Clone the git repository or download the script file directly.
- [Windows only] Open command prompt and change the current directory to where you saved the script
- Run the script in the following format:
```
python pull_from_gsheet.py <config_file> <api_key>
```
`api_key` is the key you generated from your Google Developer Console.

For example:
```
python pull_from_gsheet.py sample_conf/meeple_station.zh_cn.json <api_key>
```
for retrieving Meeple Station zh-cn localiztion files from Google Sheet.
