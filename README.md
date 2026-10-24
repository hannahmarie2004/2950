# FDA Recalls vs. CDC Illness Burden

Do FDA food recalls track the illnesses the CDC actually records? This project builds a food × pathogen × year panel to find out.

- **Data:** 39,833 FDA recall records and 66,713 CDC outbreak records (106K+ total), merged into a 1,122-row panel
- **Cleaning:** sorted 16,357 free-text recall descriptions into CDC food categories, making 7,453 recalls comparable to 1,106 outbreaks
- **Analysis:** exploratory analysis with log transforms for skewed counts; 2 preregistered hypotheses tested with regression
- **Tools:** SQL (DuckDB), Python (pandas), Jupyter, matplotlib, seaborn, Git

Built for INFO 2950 (Introduction to Data Science) at Cornell University.
