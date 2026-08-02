# Project Journal — Tax Slab Calculator

## Day 1

**What I did:**
Starting to practically play around with Python. Chose tax slab calculator 
since most of Pakistani awam doesn't even know what taxes are.

**Concepts learned:**
- Progressive/marginal tax logic: only the portion of income above a 
  threshold gets taxed at that bracket's rate, not the whole income
- if/elif/else chains
- Operator precedence
- input() always returns text, int() converts it to a number

**Challenges:**
- Biggest challenge was turning the tax slab ratios/percentages into actual 
  working formulas in code translating "11% of amount exceeding 
  1,200,000" into `(income-1200000)/100*11` wasn't obvious at first
- Copy-pasted bracket 3's formula into bracket 2's branch by mistake, 
  caught it by comparing each branch against the table again
- Forgot the colon on `else:` simple syntax miss

**Design decisions:**
- Used if/elif/else instead of a loop since I don't know loops yet so one 
  branch per bracket, using the shortcut cumulative formulas from the FBR 
  table instead of manually re-deriving bucket-by-bucket in code

**Future improvements:**
- Would like a proper graphical UI instead of just terminal input/output
- Round off the trailing .0 in the output
- Handle the 9% surcharge for income above 10 million
- Validate against negative or non-numeric input