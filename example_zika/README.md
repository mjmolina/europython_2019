# NetworkX

Website: https://networkx.github.io/

## Zika Data

The data set was downloaded from: https://www.kaggle.com/cdc/zika-virus-epidemic
Then it was filtered with the following command:
`cat cdc_zika.csv | grep "confirmed" | grep "\"Brazil"  | grep -v "\"0\""  >> zika_brazil_nonzero.csv`

## Installation

`pip install networkx`

## Execution

`python zika.py` and an animation will start.
