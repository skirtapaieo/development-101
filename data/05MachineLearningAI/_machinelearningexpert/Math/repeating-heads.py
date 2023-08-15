
def betting_probability(n, x):
    # Compute the probability of getting n consecutive heads in one attempt
    p = 0.5**n

    # Probability of NOT getting n consecutive heads in one attempt
    q = 1 - p

    # Probability of NOT getting n consecutive heads in x attempts
    not_win_probability = q**x

    # Probability of winning at least once in x attempts
    at_least_once = 1 - not_win_probability

    # Compute the payout to break even given unlimited attempts
    payout = 100 + (100 * (1-p) / p)

    return [round(at_least_once*100, 4), round(payout, 4)]

n = 3
x = 10
print(betting_probability(n, x))


