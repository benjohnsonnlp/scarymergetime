for i in range(1000):
    print("if this is even, I have a thing here: {}".format("thing" if not i % 2 else ""))


print(str([dog[0] for dog in ["charlie", "snoopy"]]))


# Below is some code
good_stuff = {"stuff 1", "stuff 3", " stuff 2"}
not_good_stuff = {" not stuff 5", "stuff 3", " not good stuff 2"}
good_stuff |= not_good_stuff
print(good_stuff)
