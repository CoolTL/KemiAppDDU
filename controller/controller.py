class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        #self.change_button_names(self.model, self.view)

    # def change_button_names(self, model, view):
    #     """ This method changes the periodic table from having the number to the name """
    #     i = 0
    #     for button in view.buttons:
    #         view.buttons[button].set_text(f"{model.atoms[i]}")
    #         i += 1
