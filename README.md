# schw2tyd
Tool to convert Charles Schwab portfolio CSV export into Track Your Dividends CSV import format.

## Installation

1. Clone the repo
```
git clone https://github.com/j0021/schw2tyd.git
```
2. Change directory
```
cd schw2tyd
```
3. Run the setup script
``` 
python setup.py install
```

## Usage

```
schw2tyd <schwab csv export file>
```

This will generate ***tyd_import.csv*** file that can be used to bulk upload to Track Your Dividends.

**NOTE**: Positions settings must include ***Symbol***, ***Quantity***, ***Cost/Share***, and ***Dividend Yield** columns before exporting from Charles Schwab. 
