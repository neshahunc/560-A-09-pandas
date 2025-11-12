#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "High", "Brown", "Dixon", "Young", "Denis", "Trimble", "Wilson", "Powell"],
          "First Name": ["Armando", "RJ", "Zayden", "James", "Derek", "Jaydon", "Isaiah", "Seth", "Caleb", "Jonathan"],
          "height": [83, 72, 70, 70, 65, 64, 64, 63, 70, 66],
          "weight": [240,180,230,240,200,200,180,200,215,190]}
data = pd.DataFrame(player)

data["bmi"] = ((data["weight"]/2.205)/((data["height"]/39.37)**2)).round(2)

print(data)

data.to_csv("bmi.csv")

