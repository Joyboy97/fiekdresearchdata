import random
import time
import csv

lots = {"LOT 88": .3, "LOT 75": .2, "LOT 19": .1, "Yards": .6}
car_types = {"Sedan": .5, "SUV": .3, "Truck": .15, "Other": .05}
x = "ALABAMA,ALASKA,ARIZONA,ARKANSAS,CALIFORNIA,COLORADO,CONNECTICUT,DELAWARE,DC,FLORIDA,GEORGIA,HAWAII,IDAHO,ILLINOIS,INDIANA,IOWA,KANSAS,KENTUCKY,LOUISIANA,MAINE,MARYLAND,MASSACHUSETTS,MICHIGAN,MINNESOTA,MISSISSIPPI,MISSOURI,MONTANA,NEBRASKA,NEVADA,NEW-HAMPSHIRE,NEW-JERSEY,NEW-MEXICO,NEW-YORK,NORTH-CAROLINA,NORTH-DAKOTA,OHIO,OKLAHOMA,OREGON,PENNSYLVANIA,RHODE-ISLAND,SOUTH-CAROLINA,SOUTH-DAKOTA,TENNESSEE,TEXAS,UTAH,VERMONT,WASHINGTON,WEST-VIRGINIA,WISCONSIN,WYOMING"
states = x.split(",")
state_chance = {
    "DELAWARE": .1,
    "NEW-JERSEY": .38,
    "NEW-YORK": .21,
    "PENNSYLVANIA": .15,
    "MARYLAND": .08,
    "CONNECTICUT": .05,
}

dates = ["3/18/2023", "3/19/2023", "3/20/2023"]
r = [i+1 for i in range(4)]
offcenters = [.1, .1, .3, .2, .2]
nice_scale = [.05, .1, .2, .5, .15]
car_colors = {"blue": .2, "white": .5, "red": .1, "black": .1, }  # other =.1
directions = {"front": .7, "back": .3}

Def biasVal(ref string):

flg = False
start = time.time()
end = time.time()

Val=locals().get(ref)["LOT 88"])
Vals= locals().get(ref+”s”)["LOT 88"])
while (not flg and end-start < 1):
  Val= vals[random.choice(list(Val’s.keys()))]
  if val in vals:
    if 100*vals[val] > random.randint(1,100):
     flg = True
  else:
   if 3*vals[val]>random.randint(1,100):
    flg=True
   end = time.time()
Return val 

print(random.choice(list(lots.keys())))
# with open('parkingdata.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Lot", "Offcenter", "Car_Color", "License_State",
#                     "Parking_Style", "Car_Type", "Nice_Car(1-5)", "Date"])

#     for i in range(100):
#        # lot

#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             lot = lots[random.choice(lots.keys())]
#             if 100*lots[lot] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         # offcenter

#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             offcenter = r[random.choice(r)]
#             if 100*offcenters[offcenter] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         # color
#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             color = car_colors[random.choice(car_colors.keys())]
#             if 100*car_colors[color] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         # state
#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             state = random.choice(states)
#             if state in state_chance:
#                 if 100*state_chance[state] > random.randint(1, 100):
#                     flg = True
#             else:
#                 if 3 > random.randint(1, 100):
#                     flg = True
#             end = time.time()

#         # frontback
#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             frontback = directions[random.choice(directions.keys())]
#             if 100*directions[frontback] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         # cartype
#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             cartype = car_types[random.choice(car_types.keys())]
#             if 100*car_types[cartype] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         # nicescale
#         flg = False
#         start = time.time()
#         end = time.time()
#         while (not flg and end-start < 1):
#             nice = nice_scale[random.choice(nice_scale.keys())]
#             if 100*nice_scale[nice] > random.randint(1, 100):
#                 flg = True
#             end = time.time()

#         writer.writerow([lot, offcenter, color, state, frontback,
#                         cartype, nice, random.choice(dates)])
#         file.close()
