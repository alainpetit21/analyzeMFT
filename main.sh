echo "Taking input from ./data/mft.raw"

source ./venv/bin/activate
python3 ./src/analyzeMFT.py

echo "Writing output from ./data/mft.raw.out.csv"
