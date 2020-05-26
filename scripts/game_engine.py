import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'banner'))

import time
# import banner
from banner import banner
# from scene import Scene, Option
from .scene import Scene, Option

class GameEngine:
    def init(self):
        super.__init__()

    def loading_screen(self):
        banner.printbyline(("./banner/logo.txt", "./banner/banner.txt"))

    def game_over(self):
        banner.printbyline(("./banner/game.txt", "./banner/over.txt"))

    def move(self, scene: Scene, option: str) -> Scene:
        for s in scene.get_next_scenes():
            if s.get_option().get_name() == option:
                print(s.get_option().get_desc(), "\n")
                return s

    def run_game(self, scene: Scene):
        if not scene:
            return

        opt_list = scene.generate_option_list()

        if len(opt_list)==0:
            if len(scene.get_next_scenes()) == 0:
                print(scene.get_desc())
                time.sleep(4)
                self.game_over()
                return
            print(scene.get_desc(), "\n")
            self.run_game(scene.get_next_scenes()[0])
            return

        scene.play_scene()

        try:
            opt = int(input('>> '))
        except EOFError:
            return
        except KeyboardInterrupt:
            return
        
        next_scene = self.move(scene, opt_list[opt-1][1])
        self.run_game(next_scene)