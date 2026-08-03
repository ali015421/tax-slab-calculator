# Project Journal — Tax Slab Calculator

## Session 1

**What I did:**
Started practically playing around with Python. Chose a tax slab 
calculator since most of the Pakistani awam doesn't even know what taxes 
are.

**Concepts learned:**
- Progressive tax logic. Only the part of your income above a threshold 
  gets taxed at that bracket's rate, not the whole income
- if/elif/else chains
- Operator precedence
- input() always gives you text, int() turns it into a number

**Challenges:**
- The biggest challenge was turning the tax slab percentages into actual 
  working formulas. Figuring out how to write "11% of amount exceeding 
  1,200,000" as `(income-1200000)/100*11` wasn't obvious at first
- Copy pasted bracket 3's formula into bracket 2's branch by mistake. 
  Caught it by comparing each branch against the table again
- Forgot the colon on else. Simple syntax mistake

**Design decisions:**
- Used if/elif/else instead of a loop since I don't know loops yet. One 
  branch per bracket, using the shortcut formulas from the FBR table 
  instead of manually working out each bucket in code

**Future improvements:**
- Want a proper graphical interface instead of just typing into the 
  terminal
- Round off the trailing .0 in the output
- Handle the 9% surcharge for income above 10 million
- Check for negative or non numeric input

## Session 2
- Added input validation for negative income and cleaned up the decimal 
  output using int()
- Tagged as v1.1
- Noticed I keep losing track of which branch I'm on before committing. 
  Need to run git branch as a habit before every commit

## Session 3

**What I added:**
- A monthly or annual income toggle that converts monthly income into 
  annual automatically
- A 9% surcharge for income above Rs. 10,000,000
- Effective tax rate calculation
- Take home pay calculation

**Challenges:**
- Had to learn how to actually trace through the code step by step to 
  find where a small error was coming from instead of just guessing at 
  fixes
- Fixing one part of the code, like reordering the monthly or annual 
  question, kept breaking something else that used to work fine, like the 
  tax rate logic and a duplicate print statement. Learned that changing 
  one part means checking everything downstream of it, not just the part 
  I touched
- Need to work on remembering concepts better between sessions instead of 
  relearning them every time

**Future improvements:**
- Add comments through the code explaining what each part does
- Graphical interface, still carried over from session 1
- Handle non numeric input, right now it crashes on invalid text
- Handle a mistyped Monthly or Annual answer, right now it just defaults 
  to Annual if you don't type M exactly