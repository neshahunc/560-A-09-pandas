#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "High"],
          "First Name": ["Armando", "RJ", "Zayden"],
          "height": [83, 72, 73],
          "weight": [240,180,180]}
data = pd.DataFrame(player)
print(data)

