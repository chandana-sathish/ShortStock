# ShortStocks

## UI:
  Enter stock name
  Display news
  Helpful/not helpful

## Parser:
  Finds links for stocks - finds articles
  Output - all relevant articles

## Database:
  Read tag coeffs to decide relevancy
  Updates relevancy coeffs based on user input
  
## Algorithm:
  Determines the tag of an article
  Stores (tag, help_val) in Db
  
## ML:
  Consumes (tag, help_val) & trains all of them
  Predicts most relevant tags

## Final:
  Displays articles when a new stock price is entered, but with the pref filter from ML
  
