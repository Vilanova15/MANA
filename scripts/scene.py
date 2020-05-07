class Scene:
    def __init__(self, name: str='', desc: str=''):
        self.name = name
        self.desc = desc
        self.option: Option = None
        self.next_scenes = {}

    def play_scene(self):
        print(self.desc, "\n")
        print("What will you do? \n")
        self.show_options()

    def show_options(self):
        for option in self.generate_option_list():
            print("[{}] {}".format(option[0], option[1]))

    def display_scene(self):
        print(self.name, ":", self.desc)
        if self.get_option():
            print("Trigger option: ", self.get_option().name)
        else:
            print("Trigger option: ", self.option)
        print("Next scenes:")
        for scene in self.next_scenes.values():
            print(scene.name)
        print()
    
    def modify_scene(self, name, desc):
        self.set_name(name)
        self.set_desc(desc)
    
    def generate_option_list(self) -> list:
        option_list = []
        i = 1
        for scene in self.next_scenes.values():
            option = (i, scene.get_option().name)
            option_list.append(option)
            i += 1
        
        return option_list
    
    def get_name(self) -> str:
        return self.name

    def get_desc(self) -> str:
        return self.desc

    def get_option(self):
        return self.option
    
    def get_next_scenes(self) -> list:
        return self.next_scenes.values()

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc
    
    def set_option(self, option):
        self.option = option

    def add_next_scene(self, scene):
        self.next_scenes[scene.get_name()] = scene

    def remove_next_scene(self, scene_name):
        del self.next_scenes[scene_name]


class Option:
    def __init__(self, name: str='', desc: str=''):
        self.name = name
        self.desc = desc

    def display_option(self):
        print(self.name, "\n", self.desc)

    def modify_option(self, name, desc):
        self.set_name(name)
        self.set_desc(desc)
    
    def get_name(self) -> str :
        return self.name

    def get_desc(self) -> str :
        return self.desc

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc