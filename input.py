import pandas as pd
from cashflower import ModelPointSet

assumption = {
  "INTEREST_RATE": 0.005,
  "DEATH_PROB": 0.003
}


policy = ModelPointSet(data=pd.DataFrame({
    "sum_assured": [100_000]
}))
