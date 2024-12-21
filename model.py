from cashflower import variable
from input import assumption, policy, runplan
from settings import settings


@variable()
def survival_rate(t):
    if t == 0:
        return 1 - assumption["DEATH_PROB"]
    return survival_rate(t-1) * (1-assumption["DEATH_PROB"])


@variable()
def expected_benefit(t):
    if t == 0:
        return 0
    return survival_rate(t-1) * assumption["DEATH_PROB"] * policy.get("sum_assured")


@variable()
def net_single_premium(t):
    i = assumption["INTEREST_RATE"]
    i *= (1 + runplan.get("interest_rate_stress"))

    if t == settings["T_MAX_CALCULATION"]:
        return expected_benefit(t)
    return expected_benefit(t) + net_single_premium(t+1) * 1/(1+i)
