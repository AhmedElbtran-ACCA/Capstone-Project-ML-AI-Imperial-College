# Data Access Notes

Large datasets should not be uploaded directly to GitHub. Use this file to document where the data came from and how someone can access it.

## Dataset

- Dataset name: [Dataset name]
- Source: [Provider or organisation]
- External link: [URL]
- Licence or access terms: [Licence or terms]
- File format: [CSV, Excel, JSON, database export, etc.]
- Approximate size: [Rows, columns and file size]

## Local File Layout

Recommended local layout:

```text
data/
  raw/          # Original files, not committed if large or restricted
  processed/    # Cleaned files, not committed if large or restricted
  sample/       # Small shareable sample, if licence allows
```

If a small sample is included, explain how it was created and confirm that it is permitted by the dataset licence.

## Reproducibility Notes

- Download the dataset from: [URL]
- Save the raw file as: `data/raw/[filename]`
- Run the notebook: `notebooks/BBO_Capstone_Method_and_Results.ipynb`
