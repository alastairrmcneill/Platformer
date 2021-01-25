"""
This is the default scene class that all others should inherit from. There should be no instances of this class directly in the application
"""

class Scene:
    def __init__(self):
        """
        Sets some default properties every scene should have
        """
        self.done = False
        self.next = None
        self.previous = None
        self.manager = None
        self.persist = {}

    def startup(self, persist):
        """
        This method gets run every time the managers swaps to this scene

        Arguments:
            persist {dict} -- Dictionary containing the information that needs to be passed to this scene

        Raises:
            NotImplementedError: This method should be overwritten in every scene
        """
        raise NotImplementedError

    def cleanup(self):
        """
        This method runs every time the manager switches to the next scene.

        Returns:
            persist {dict} - Dictionary containing the information that needs to be passed to the next scene

        Raises:
            NotImplementedError: This method should be overwritten in every scene
        """
        raise NotImplementedError

    def handle_event(self, event):
        """
        The event handling method for every scene. Determine what to do for any specific event that comes in

        Arguments:
            event {pygame.event} -- Event from the pygame module

        Raises:
            NotImplementedError: This method should be overwritten in every scene
        """
        raise NotImplementedError

    def update(self):
        """
        Update the scene every frame of the game

        Raises:
            NotImplementedError: This method should be overwritten in every scene
        """
        raise NotImplementedError

    def draw(self, screen):
        """
        Draw the current scene to the main screen

        Arguments:
            screen {pygame.surface} -- The screen to draw to

        Raises:
            NotImplementedError: This method should be overwritten in every scene
        """
        raise NotImplementedError
