from scene import Scene, Option

class GameEngine:
    def init(self):
        super.__init__()

    def move(self, scene: Scene, option: str) -> Scene:
        for s in scene.get_next_scenes():
            if s.get_option().get_name() == option:
                return s

    def run_game(self, scene: Scene):
        if not scene:
            return

        opt_list = scene.generate_option_list()
        scene.play_scene()

        try:
            opt = int(input('>> '))
        except EOFError:
            return
        except KeyboardInterrupt:
            return
        
        next_scene = self.move(scene, opt_list[opt-1][1])
        self.run_game(next_scene)