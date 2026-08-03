# Tax Slab Calculator

Calculates income tax owed based on Pakistan's FBR progressive tax slabs 
(FY 2025-26), given an annual or monthly salary.

## How it works
Pakistan uses a progressive tax system — income is taxed in tiers, where 
each portion of your salary is taxed at the rate for the bracket it falls 
into, not your entire income at one flat rate. This calculator takes an 
income (monthly or annual) as input, converts it to annual if needed, and 
applies the correct FBR slab formulas to compute total tax owed, effective 
tax rate, and take-home pay.

## Tax Slabs (FY 2025-26)
| Income Range (Rs.) | Rate |
|---|---|
| 0 – 600,000 | 0% |
| 600,000 – 1,200,000 | 1% of amount exceeding 600,000 |
| 1,200,000 – 2,200,000 | 6,000 + 11% of amount exceeding 1,200,000 |
| 2,200,000 – 3,200,000 | 116,000 + 23% of amount exceeding 2,200,000 |
| 3,200,000 – 4,100,000 | 346,000 + 30% of amount exceeding 3,200,000 |
| 4,100,000+ | 616,000 + 35% of amount exceeding 4,100,000 |

A 9% surcharge applies on top of the calculated tax when income exceeds 
Rs. 10,000,000/year.

## Usage
Run the script and follow the prompts:
\`\`\`
python3 main.py
\`\`\`
You'll be asked for your income, then whether it's monthly or annual.

## Features
- Progressive tax calculation across all 6 FBR brackets
- Monthly or annual income input (auto-converts monthly to annual)
- 9% surcharge for income above Rs. 10,000,000
- Effective tax rate calculation
- Take-home pay calculation
- Input validation for zero/negative income

## Version history
- **v1.2** — Added monthly/annual toggle, 9% surcharge, effective tax rate, 
  and take-home pay
- **v1.1** — Added negative income validation, cleaned up decimal output
- **v1.0** — Initial working version with core tax bracket logic

## Planned improvements
- Graphical UI
- Non-numeric input handling (currently crashes on invalid text input)
- Handle mistyped Monthly/Annual input (currently defaults to Annual if 
  not exactly "M")

## Built with
Python (if/elif/else, operators, input/type conversion)