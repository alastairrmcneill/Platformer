"""
This is the Scene Manager, it holds a reference to every scene, what scene is currently active and allows to switch between the current and the coming state.

*** This file should not require modification ***
"""


class Manager:
    def __init__(self):
        """
        Sets up a blank manager
        """
        self.scene_dict = {}
        self.scene_name = None
        self.scene = None
        self.FPS = 30

    def setup_scenes(self, scene_dict, start_scene):
        """
        Sets up the scenes

        Arguments:
            scene_dict {dict} -- Dictionary containing the name of scene and the scene object {"Name": Scene_Object(), "Name2": Scene_Object2()}
            start_scene {string} -- Name of the first scene to show
        """
        self.scene_dict = scene_dict
        self.scene_name = start_scene
        self.scene = self.scene_dict[self.scene_name]
        self.scene.manager = self

    def swap_scenes(self):
        """
        Swaps between the current state and the next state
        """
        previous = self.scene_name
        self.scene_name = self.scene.next
        persist = self.scene.cleanup()
        self.scene = self.scene_dict[self.scene_name]
        self.scene.manager = self
        self.scene.startup(persist)
        self.scene.previous = previous
