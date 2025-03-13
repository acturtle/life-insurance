import pandas as pd
from cashflower import ModelPointSet, Runplan

assumption = {
  "INTEREST_RATE": 0.005,
  "DEATH_PROB": 0.003
}


policy = ModelPointSet(data=pd.DataFrame({
    "sum_assured": [100_000, 20_000, 50_000, 80_000]
}))


runplan = Runplan(data=pd.DataFrame({
    "version": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "interest_rate_stress": [0, 0.1, -0.1, 0.2, -0.2, 0.3, -0.3, 0.4, -0.4, 0.5, -0.5]
}))
