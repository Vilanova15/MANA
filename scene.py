class Scene:
    def __init__(self, name='', desc=''):
        self.name = name
        self.desc = desc
        self.option = None
        self.next_scenes = {}

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def get_option(self):
        return self.option
    
    def get_next_scenes(self):
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
    def __init__(self, name='', desc=''):
        self.name = name
        self.desc = desc

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc