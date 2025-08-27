# Problem 19: Counting Sundays

## Problem Description

You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,April, June and November. All the rest have thirty-one,\
  Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

## Solution

The most straightforward way to solve this is to simulate the calendar month by month, keeping track of the day of the week. We don't need to check every single day; we only need to know the day of the week for the first day of each month.

The core of our simulation requires two key variables:

1. A counter to store the number of Sundays that fall on the first of the month.
2. A tracker variable that always knows the day of the week for the first day of the current month.

### Step-by-Step Breakdown

#### 1. Representing the Day of the Week

To make calculations easy, we can represent the days of the week with numbers. A common convention is:

* Sunday = 0
* Monday = 1
* Tuesday = 2
* ...
* Saturday = 6

This numbering allows us to use modular arithmetic (`% 7`) to cycle through the days of the week seamlessly.

#### 2. Finding the Starting Point

The problem specifies the range from **1 Jan 1901** to **31 Dec 2000**. We are given a reference point: **1 Jan 1900 was a Monday**. We must first calculate the day of the week for our actual start date, 1 Jan 1901.

* The year 1900 is divisible by 100 but not by 400, so it is **not** a leap year. It has 365 days.
* The number of days in a week is 7. We can find how much the day of the week shifts over a year by calculating `365 % 7`, which equals 1.
* This means a 365-day year shifts the day of the week forward by one day.
* Since 1 Jan 1900 was a Monday (1), 1 Jan 1901 must have been a **Tuesday (2)**. This is our initial value for the day-of-the-week tracker.

#### 3. The Simulation Loop

We set up nested loops to iterate through every month in the specified century:

* An outer loop for the `year`, from 1901 to 2000.
* An inner loop for the `month`, from 1 (January) to 12 (December).

#### 4. Logic Inside the Loop

For each month, we perform two main actions:

**A. Check the First Day** At the beginning of the inner loop, we check our day-of-the-week tracker. If its value is 0 (Sunday), we increment our `sunday_count`.

**B. Advance to the Next Month** Next, we need to calculate the day of the week for the start of the _next_ month. To do this, we add the number of days in the _current_ month to our tracker.

* **Days in Month:** This requires a set of rules:
  * 30 days for April, June, September, November.
  * 31 days for all the rest, except for February.
  * February has 29 days in a leap year and 28 otherwise. A leap year is a year divisible by 4, unless it is a century year not divisible by 400.
* **Update the Tracker:** We update our tracker using this formula: `new_day = (current_day + days_in_current_month) % 7`

After the loops have processed every month from January 1901 to December 2000, the `sunday_count` variable will hold the final answer.

## Code

```python
def counting_sundays(start_year, end_year):
    # --- Step 1: Determine the day of the week for Jan 1st of the start_year ---
    # We use Jan 1, 1900 (a Monday) as our reference point.
    # We represent days as: Sunday=0, Monday=1, Tuesday=2, ..., Saturday=6
    day_of_week = 1  # Jan 1, 1900 was a Monday
    
    # Loop from 1900 to the year before start_year to find the starting day
    for year in range(1900, start_year):
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_year = 366 if is_leap else 365
        day_of_week = (day_of_week + days_in_year) % 7

    # --- Step 2: Iterate through each month in the specified range and count Sundays ---
    sunday_count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Check if the first day of this month is a Sunday (0)
            if day_of_week == 0:
                sunday_count += 1
            
            # Determine the number of days in the current month
            if month in [4, 6, 9, 11]:  # 30-day months
                days_in_month = 30
            elif month == 2:  # February
                is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                days_in_month = 29 if is_leap else 28
            else:  # 31-day months
                days_in_month = 31
            
            # Update day_of_week to be the first day of the *next* month
            day_of_week = (day_of_week + days_in_month) % 7
            
    return sunday_count

# This block runs the code and tests it when the script is executed directly
if __name__ == "__main__":
    # Define test cases for validation: (start_year, end_year, expected_result)
    test_cases = [
        (1943, 1946, 6),
        (1995, 2000, 10),
        (1901, 2000, 171)
    ]
    
    print("--- Running Test Cases ---")
    for start, end, expected in test_cases:
        result = counting_sundays(start, end)
        status = "Passed" if result == expected else "Failed"
        print(f"Test for {start}-{end}: Expected={expected}, Got={result} -> {status}")
    
    print("\n--- Original Project Euler Problem Answer ---")
    final_answer = counting_sundays(1901, 2000)
    print(f"The number of Sundays on the first of the month during the 20th century (1901-2000) is: {final_answer}")
```
