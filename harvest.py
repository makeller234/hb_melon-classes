############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairing = []

        # Fill in the rest

    def add_pairing(self, pairings):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        test = []
        #self.pairing = pairing.append(pairing)
        for pairing in pairings:
            test.append(pairing)
        self.pairing = test

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.new_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing(["mint"])

    casaba = MelonType("cas", 2003, "orange", False, None, "Casaba")
    casaba.add_pairing(["strawberries", "mint"])
    

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing(["prosciutto"])

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing(["ice cream"])

    all_melon_types.append(muskmelon)
    all_melon_types.extend([casaba, crenshaw, yellow_watermelon])
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f'{melon.name} pairs with ')
        for pair in melon.pairing:
            print(f'- {pair}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}
    # Fill in the rest
    for melon in melon_types:
        melon_dictionary[melon.code] = melon_dictionary.get(melon.code)
        melon_dictionary[melon.code] = {'name': melon.name, 'First Harvest': melon.first_harvest, 'color': melon.color, 'pairs': melon.pairing, 'seedless': melon.is_seedless, "bestseller": melon.is_bestseller}

    return melon_dictionary

melons1 = make_melon_types()
# print_pairing_info(melons)
# print(make_melon_type_lookup(melons))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rate, color_rate, field_harvest, who_harvest):
       
        self.melon_type = melon_type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.field_harvest = field_harvest
        self.who_harvest = who_harvest

    
    def is_sellable(self):
        if self.shape_rate >5 and self.color_rate >5 and not self.field_harvest == 3:
            return True
        else:
            return False
        
def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Michael')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5,
                   melon_6, melon_7, melon_8, melon_9])

    return melons
   

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.who_harvest} from {melon.field_harvest} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.who_harvest} from {melon.field_harvest} (NOT SELLABLE)')

melons = make_melons(melons1)
get_sellability_report(melons)

