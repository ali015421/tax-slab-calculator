# Tax Slab Calculator

Calculates income tax owed based on Pakistan's FBR progressive tax slabs 
(FY 2025-26), given an annual salary.

## How it works
Pakistan uses a progressive tax system — income is taxed in tiers, where 
each portion of your salary is taxed at the rate for the bracket it falls 
into, not your entire income at one flat rate. This calculator takes an 
annual income as input and applies the correct FBR slab formulas to 
compute total tax owed.

## Tax Slabs (FY 2025-26)
| Income Range (Rs.) | Rate |
|---|---|
| 0 – 600,000 | 0% |
| 600,000 – 1,200,000 | 1% of amount exceeding 600,000 |
| 1,200,000 – 2,200,000 | 6,000 + 11% of amount exceeding 1,200,000 |
| 2,200,000 – 3,200,000 | 116,000 + 23% of amount exceeding 2,200,000 |
| 3,200,000 – 4,100,000 | 346,000 + 30% of amount exceeding 3,200,000 |
| 4,100,000+ | 616,000 + 35% of amount exceeding 4,100,000 |

## Usage
Run the script and enter your annual income when prompted:
\`\`\`
python3 main.py
\`\`\`

## Features
- Progressive tax calculation across all 6 FBR brackets
- Input validation for negative income
- Clean integer output (no stray decimals)

## Version history
- **v1.1** — Added negative income validation, cleaned up decimal output
- **v1.0** — Initial working version with core tax bracket logic

## Planned improvements
- Graphical UI
- Handle the 9% surcharge for income above Rs. 10,000,000
- Non-numeric input handling (currently crashes on invalid text input)

## Built with
Python (if/elif/else, operators, input/type conversion) 
