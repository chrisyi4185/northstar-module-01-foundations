# Brainstorm: Crescent Bakery Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for
a small fictional bakery client.

Task: Brainstorm analytical questions I should consider asking of the dataset
described below. I'm at the Define stage of the analytics lifecycle and need
a candidate list of questions before I start writing any code.

Context: The dataset is for Crescent Bakery, a fictional regional bakery.
50 rows, one row per customer. Columns:

- customer_id: string, unique identifier per customer (nominal)
- region: categorical, one of {Downtown, North Side, South Side, West End} (nominal)
- first_visit_year: integer year between 2018 and 2025 inclusive (interval)
- satisfaction: integer 1 to 5, customer satisfaction rating (ordinal)
- total_spent_usd: continuous, total dollars the customer has spent (ratio)
- visits_last_year: integer, number of visits in the last year (ratio)

The bakery is interested in understanding customer behavior to inform
marketing and product decisions.

Constraints:
1. Only suggest questions that can be answered from the columns listed above.
   Don't invent additional columns.
2. For each suggested question, identify which columns would be used and
   what statistical method would be appropriate.
3. Make sure the statistical methods you propose are appropriate for the
   data type of each column (mean for ratio, mode for nominal, etc.).

Output Format: A numbered list of 8 to 12 analytical questions. For each:
- The question (one sentence)
- The columns involved
- The recommended statistical or visualization method

## Tool 1: Claude output

Here are 11 candidate questions. I've added a short "why this method" note on each, since the method depends on each column's measurement level.

Quick refresher: the data type decides which summaries are legitimate.

Nominal (region): counts, proportions, mode only.
Ordinal (satisfaction): median, mode and percentiles are safe. The gaps between ratings aren't guaranteed equal, so treat means with caution.
Interval (first_visit_year): differences are meaningful (2023 is 3 years after 2020), but ratios aren't.
Ratio (total_spent_usd, visits_last_year): everything works, including means and ratios.
How are customers distributed across the four regions?
Columns: region
Method: frequency table with proportions, a bar chart, and the mode. Optionally a chi-square goodness-of-fit test against an even split.
Why: nominal data only supports counting.
What does typical customer satisfaction look like?
Columns: satisfaction
Method: frequency table, bar chart, median, mode and IQR.
Why: median and mode respect the ordinal scale. Report the mean only as a secondary figure, if at all.
How is total spending distributed, and are there outliers?
Columns: total_spent_usd
Method: histogram, boxplot, mean, median, standard deviation and skewness.
Why: ratio data allows the full toolkit. A mean far above the median signals a few big spenders.
Does total spending differ by region?
Columns: region, total_spent_usd
Method: side-by-side boxplots, then mean and median per region. For testing, use ANOVA if the data look roughly normal, otherwise Kruskal-Wallis.
Why: this compares a ratio outcome across nominal groups.
Does satisfaction differ by region?
Columns: region, satisfaction
Method: 100% stacked bar chart, median per region, and Kruskal-Wallis.
Why: the outcome is ordinal, so use rank-based tests rather than ANOVA.
Do more satisfied customers visit more often?
Columns: satisfaction, visits_last_year
Method: boxplot of visits by rating, plus Spearman rank correlation.
Why: Spearman handles an ordinal variable correctly, whereas Pearson assumes interval-or-better.
Do more satisfied customers spend more?
Columns: satisfaction, total_spent_usd
Method: boxplot of spend by rating, plus Spearman correlation.
How strongly are visit frequency and total spending related?
Columns: visits_last_year, total_spent_usd
Method: scatterplot with a trend line, Pearson correlation (Spearman as a robustness check), and simple linear regression.
Why: both are ratio variables, so this is the classic case for Pearson and regression.
Do longer-standing customers spend or visit more?
Columns: first_visit_year, total_spent_usd, visits_last_year
Method: scatterplots, Pearson or Spearman correlation, and mean spend by first-visit year.
Why: year is interval, so talk about "years earlier or later," not "twice as long."
How has customer acquisition changed over time, and does it vary by region?
Columns: first_visit_year, region
Method: bar chart of new customers per year, a region-by-year cross-tab with a grouped bar chart, and Fisher's exact test or collapsed year bands if cells are sparse.
Why: it shows growth or decline and whether certain regions are driving it.
What does a high-value customer look like?
Columns: all of them
Method: define the top quartile of total_spent_usd, then compare that group against everyone else on region (proportions), satisfaction (median), visits (mean or median) and first-visit year. Use side-by-side summary tables and grouped plots.
Why: this turns the earlier findings into a profile that marketing can act on.

Caveats to settle at the Define stage:

Small sample: with 50 rows, each region has roughly 12 customers. Treat the tests as exploratory, and expect sparse cells in cross-tabs.
Different time windows: total_spent_usd looks like a lifetime figure while visits_last_year covers one year, so avoid combining them (e.g., "spend per visit") without flagging the mismatch. Tenure also confounds lifetime spend, because older customers have had more time to spend.
Association, not causation: none of these questions can show that satisfaction drives spending, only that they move together.

I'd start with 1-3 as the foundation (cleaning, distributions), then 4-8 for relationships, and finish with 11 as the business-facing synthesis.

## Tool 2: ChatGPT output

Which region has the highest average customer spending?
Columns involved: region, total_spent_usd
Recommended method: Group customers by region and compare the mean and median total_spent_usd; use a box plot to visualize the distribution by region. Median is useful because spending may be skewed.
Which region has the highest average number of visits in the last year?
Columns involved: region, visits_last_year
Recommended method: Calculate the mean and median visits by region and visualize with a box plot or bar chart of mean visits.
Is customer satisfaction associated with total spending?
Columns involved: satisfaction, total_spent_usd
Recommended method: Use a Spearman rank correlation, since satisfaction is ordinal and spending is continuous; visualize with a box plot of spending across satisfaction levels.
Is customer satisfaction associated with how frequently customers visit?
Columns involved: satisfaction, visits_last_year
Recommended method: Use Spearman rank correlation and compare the distribution of visits across satisfaction levels with box plots.
Do customers who visit more frequently tend to spend more overall?
Columns involved: visits_last_year, total_spent_usd
Recommended method: Calculate Spearman correlation and create a scatter plot with a fitted trend line. Both variables are ratio-scale, but the small sample and possible nonlinearity make Spearman a useful starting point.
How does customer spending differ across satisfaction levels?
Columns involved: satisfaction, total_spent_usd
Recommended method: Compare median and mean spending for each satisfaction level and use a box plot. If formally testing differences across all five ordinal groups, consider the Kruskal–Wallis test.
Are customers in different regions similarly satisfied?
Columns involved: region, satisfaction
Recommended method: Compare the median satisfaction and the distribution/proportion of each rating by region; use a stacked bar chart. For an inferential test, a chi-square test of independence can assess association between the two categorical variables.
Do customers who have been visiting the bakery longer tend to spend more?
Columns involved: first_visit_year, total_spent_usd
Recommended method: Calculate Spearman correlation between first-visit year and spending and use a scatter plot. Because an earlier year represents a longer customer relationship, interpret the direction carefully.
Do customers who have been visiting longer tend to visit more frequently?
Columns involved: first_visit_year, visits_last_year
Recommended method: Use Spearman correlation and a scatter plot. Treat first_visit_year as an ordered numeric variable rather than a nominal category for this question.
How are customers distributed across the four regions?
Columns involved: region
Recommended method: Calculate counts and percentages for each region and visualize with a bar chart. The mode can identify the most common region.
What does the overall customer satisfaction profile look like?
Columns involved: satisfaction
Recommended method: Calculate the median, mode, and frequency/percentage of each rating; use a bar chart. Because satisfaction is ordinal, avoid treating the mean as the primary summary.
Are customers who visit more frequently concentrated in particular regions?
Columns involved: region, visits_last_year
Recommended method: Compare mean and median visits across regions using a box plot; optionally use Kruskal–Wallis to test whether visit distributions differ across regions.

Scoping note: With only 50 customers, I would treat these primarily as exploratory questions. In the Define stage, I'd prioritize questions that connect directly to a business decision—for example, whether particular regions or customer satisfaction levels are associated with higher spending or engagement—rather than trying to answer all 12.

## Verification

| Check | # | Question | Source |
| ----- | --- | -------- | ------ |
| ✓ | 1 | How are customers distributed across the four regions? | Both |
| ✓ | 2 | What does typical customer satisfaction look like? | Both |
| ✓ | 3 | How is total spending distributed, and are there outliers? | Claude |
| ✓ | 4 | Does total spending differ by region? | Both |
| ✓ | 5 | Does satisfaction differ by region? | Both |
| ✓ | 6 | Do more satisfied customers visit more often? | Both |
| ✓ | 7 |Do more satisfied customers spend more? | Both |
| ✓ | 8 | How strongly are visit frequency and total spending related? | Both |
| ✓ | 9 | Do longer-standing customers spend or visit more? | Both |
| ? | 10 | How has customer acquisition changed over time and does it vary by region? | Claude |
| ✓ | 11 | What does a high-value customer look like? | Claude |
| ✓ | 12 | Which region has the highest average customer spending? | ChatGPT |
| ✓ | 13 | Which region has the highest average number of visits in the last year? | ChatGPT |
| ✓ | 14 | Do customers who have been visiting longer tend to visit more frequently? | ChatGPT |




## Verified question list
| # | Question |
| --- | -------- |
| 1 | How are customers distributed across the four regions? |
| 2 | What does typical customer satisfaction look like? |
| 3 | How is total spending distriguted, and are there outliers? |
| 4 | Does total spending and satisfaction differ by region? |
| 5 | Do more satisfied customers visit more often or spend more? |
| 6 | How strongly are visit frequency and total spending related? |
| 7 | Do longer standing customers spend or visit more? |
| 8 | What does a high value customer look like? |
| 9 | Which region(s) have the most visits and spending? |
 