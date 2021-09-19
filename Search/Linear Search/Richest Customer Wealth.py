# https://leetcode.com/problems/richest-customer-wealth/submissions/

def maximumWealth(accounts):
    wealth = 0
    for acc in accounts:
        wealth = max(wealth, sum(acc))

    return wealth