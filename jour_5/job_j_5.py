class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
    
    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f"Part: {self.name}, Material: {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}
    
    def add_part(self, part):
        self.__parts[part.name] = part
    
    def display_state(self):
        print(f"Ship: {self.name}")
        for part in self.__parts.values():
            print(part)
    
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"Part {part_name} not found in ship.")
    
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
        else:
            print(f"Part {part_name} not found in ship.")
    
    def get_parts(self):
        return self.__parts
    
    def set_parts(self, parts):
        self.__parts = parts

# Example usage
part1 = Part("Engine", "Steel")
part2 = Part("Wing", "Aluminum")
ship = Ship("Titanic")
ship.add_part(part1)
ship.add_part(part2)
ship.display_state()

# Accessing private attribute using getter
print(ship.get_parts())

# Modifying private attribute using setter
new_parts = {"Rudder": Part("Rudder", "Titanium")}
ship.set_parts(new_parts)
ship.display_state()
