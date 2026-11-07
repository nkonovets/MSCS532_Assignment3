import random


class HashTable:

    def __init__(self, slot_count = 8):         # function to initialize an empty table
        self.slot_count = slot_count
        self.key_count = 0
        self.slots = [[] for _ in range(self.slot_count)]
        self.pick_random_numbers()

    def pick_random_numbers(self):              # random numbers for the universal hash function
        self.prime = 2_147_483_647
        self.random_a = random.randint(1, self.prime - 1)
        self.random_b = random.randint(0, self.prime - 1)

    def get_slot_index(self, key):              # turns the key into the index of its slot
        if isinstance(key, int):
            key_number = key
        else:
            key_number = hash(key)

        return ((self.random_a * key_number + self.random_b) % self.prime) % self.slot_count



    def search(self, key):                      # returns the value of the key, or None if it is not there
        slot = self.slots[self.get_slot_index(key)]

        for key_value_pair in slot:             # loop to find the key in the slot
            if key_value_pair[0] == key:
                return key_value_pair[1]

        return None

    def insert(self, key, value):               # adds the key, or updates it if it already exists
        slot = self.slots[self.get_slot_index(key)]

        for key_value_pair in slot:             # loop to check if the key is already in the slot
            if key_value_pair[0] == key:
                key_value_pair[1] = value
                return

        slot.append([key, value])
        self.key_count += 1

        if self.load_factor() > 0.75:            # make the table bigger when it gets too full
            self.resize(self.slot_count * 2)

    def delete(self, key):                      # removes the key, returns True if it was found
        slot = self.slots[self.get_slot_index(key)]

        for position in range(len(slot)):       # loop to find the key and remove it from the slot
            if slot[position][0] == key:
                slot.pop(position)
                self.key_count -= 1
                return True

        return False


    def resize(self, new_slot_count):           # moves every key into a new bigger table
        old_slots = self.slots

        self.slot_count = new_slot_count
        self.slots = [[] for _ in range(self.slot_count)]
        self.pick_random_numbers()

        for slot in old_slots:                  # loop to go through every slot of the old table
            for key, value in slot:             # loop to move every key from that slot into the new table
                self.slots[self.get_slot_index(key)].append([key, value])


    def load_factor(self):                      # how full the table is
        return self.key_count / self.slot_count



if __name__ == "__main__":

    table = HashTable()

    names = ["Nikita", "Michael", "Anna", "David", "Sofia", "Max", "Emma"]

    for position in range(len(names)):          # loop to insert every name into the table
        table.insert(names[position], position)

    print("search Nikita:", table.search("Nikita"))
    print("delete Michael:", table.delete("Michael"))
    print("search Michael:", table.search("Michael"))
    print("delete Michael again:", table.delete("Michael"))
    print("slots:", table.slot_count, "keys:", table.key_count, "load factor:", round(table.load_factor(), 2))