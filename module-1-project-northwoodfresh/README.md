# Northstar Module 1: Foundations of Data Analytics & Statistics

Module project for Module 1 of Coding Temple's AI Data Analytics Foundations course at Northstar Data Group

## What is This?

Synthetic dataset creation and analysis to prototype methodology in preparation for real data to follow. 

CFO Sven Anderson requests analysis on a 23% decline in the Southwest region. He wishes to know what is causing the Southeast region's revenue decline and what to do about it before the holiday season. 

This synthetic dataset is built to closely simulate actual numbers and prototype the analysis before actual data is available from Northwoodfresh internal servers. 

## What it Does

The initial script defines a dictionary of fictional sales values for 4 regions, then the analysis prints the total, average, max, min, std, and iqr across all regions. From there, revenue distributions are visualized for all regions and specifically the southeast region. Additionally the southeast region has calculations for a 95% CI, a 2 sample t-test, and and effect size.

## How to run

You need python 3.10 or higher. From the terminal, in this folder:

    python generate_northwoodfresh_data.py

(on Mac and Linux you may need `python3` instead of `python`.)

## Files 

`README.md`
`generate_northwoodfresh_data.py`
`northwoodfresh_sales.csv`
`northwoodfresh_analysis.ipynb`
`sven_anderson_memo.md`
`northwoodfresh_sales.xlsx`

## What did I find?

Upon analysis, I found that there is indeed a bimodal distribution for the southeast region that isn't present in the other regions. The difference is roughly 24% below the mean of the baseline, in line with the data that the CFO provided with a 95% CI of 21%-27%. 

## AI Use Disclosure

I used AI 4 times in this project. First, my generation script produced errors because I hadn't formatted the integration of the baselines properly. I asked Chat GPT to explain how to integrate baselines into my dataset and wrote the code myself from the information it taught me. Secondly, I used ChatGPT to help debug my code when trying to create the histograms and it caught a typo that had resulted in an empty chart. Thirdly, I asked ChatGPT to teach me how to make appearance based changes to my charts like centering titles and changing axis labels. I took it's suggestion and subsequently modified more appearance issues with the charting myself. Lastly, I used ChatGPT to review my executive summary. It suggested I leave out parts that were too speculative for an executive summary and I agreed. It also suggested less confidence in wording seeing as the dataset is synthetic and I agreed there as well. No wording was directly taken from AI and all code was written independently from the AI suggestions.