import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # value that are received from the user
        self.year = None

    def handleCalcola(self, e):
        # I have to control the info that are given from the user
        if not self.controlYear(self._view._txtAnno.value):
            return

        ...
        # creation of the graph
        pass

    def controlYear(self, year: str) -> bool:
        if year == "":
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(
                ft.Text(value = "You have to insert a value at the fild year", color = "red")
            )
            self._view.update_page()
            return False

        try:
            self.year = int(year)
        except ValueError:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(
                ft.Text(value = "You have to insert a number for the fild year", color = "red")
            )
            self._view.update_page()
            return False

        if self.year < 1816:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(
                ft.Text(value = "This DataBase don't have info for the year writen by the user",
                        color = "blue")
            )
            self._view.update_page()
            return False

        if self.year > 2016:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(
                ft.Text(value = "This DataBase don't have enough update info for this result",
                        color = "blue")
            )
            self._view.update_page()
            return False

        # if all controls are passed
        return True