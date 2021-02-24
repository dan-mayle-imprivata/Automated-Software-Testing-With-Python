friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# difference function (Only returns non-duplicates)
local_friends = friends.difference(abroad)  # {"Rolf"}
local_friends2 = abroad.difference(friends)  # set{}

# union function (Adds both sets)
local = {"Rolf"}
abroad2 = {"Bob", "Anne"}

friends = local.union(abroad2)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)  # {"Bob","Jen"}
