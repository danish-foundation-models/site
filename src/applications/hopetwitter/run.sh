# Logs of what have been run an in what order

echo "Preprocessing Twitter to be readable by HF datasets"
python src/applications/hopetwitter/flatten_ndjson.py

echo "Apply quality filter to DA tweets"
python src/applications/hopetwitter/quality_filter.py
# remove temporary files
rm /work/twitter_cleaned/*_flatten.ndjson

echo "Deduplicate Tweets"
