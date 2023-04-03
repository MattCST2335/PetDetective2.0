from Model import Model
from View import View

class Controller:
    """
    The Controller class of my Pet Detective application.
    Creation date: February 10, 2023
    @author: Matt Ramey

    Attributes
    ------
    petDetective : Controller
        The controller object is the controller part
        of the MVC for the Pet Detective application.
    model : Model
        The model object is the model part of the
        MVC for the Pet Detective application.
    view : View
        The view object is the view part of the MVC
        for the Pet Detective application.

    Methods
    ------
    search(size, sound_level, activity_level, hair_length, affection_level)
        Searches the database for pets that match the parameters.
    """

    def __init__(self):
        """
        Parameters
        ------
        model : Model
            The model object is the model part of the
            MVC for the Pet Detective application.
        view : View
            The view object is the view part of the MVC
            for the Pet Detective application.
        """

        self.model = Model()
        # Passing self as a parameter enables two way
        # with the view window.
        self.view = View(self)

    def main(self):
        """ This opens the homepage. """

        self.view.main()

    def search(self, size, sound_level, activity_level, hair_length, affection_level):
        """ Searches the database for pets that match the parameters.

        Parameters
        ------
        size : str
            Desired pet size.
        sound_level : str
            Desired pet noise level.
        activity_level : str
            Desired pet activity level.
        hair_length : str
            Desired pet hair or feather length.
        affection_level : str
            Desired pet affection level.
        """

        return self.model.retrieve_pets(size, sound_level, activity_level, hair_length, affection_level)

if __name__ == "__main__":
    # This creates the necessary controller object.
    petDetective = Controller()
    # This starts the application.
    petDetective.main()
