import flet as ft

from model.country import Country


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # value that are received from the user
        self.year = None
        self.source_country = None

    def handleCalcola(self, e):
        self._view._txt_result.clean()
        # I have to control the info that are given from the user
        if not self.controlYear(self._view._txtAnno.value):
            return

        # creation of the graph
        self._model.create_graph(self.year)
        # info that are given to the user
        self._view._txt_result.controls.append(
            ft.Text(value = "The graph is come out well", color = "blue")
        )
        # info of the linked component
        self._view._txt_result.controls.append(
            ft.Text(value = f"The graph has {self._model.get_number_linked_component()} linked component",
                    color="blue")
        )
        # info about the nodes of the graph
        self._view._txt_result.controls.append(
            ft.Text(value = "Below there are the info regard the nodes")
        )
        for info in self._model.get_nodes_info():
            self._view._txt_result.controls.append(
                ft.Text(value = f"{info[0]} -- {info[1]} vicini.")
            )

        # when the graph is present, the search control of the view are be able to be allowed
        self._view._DDBCountry.disabled = False
        self.fill_DDBCountry()
        self._view._buttonCountrySource.disabled = False

        self._view.update_page()

    # this is the control for the first version of the function search_country...
    def search_country_reachable(self, e):
        self._view._txt_result.clean()
        country_reachable = self._model.search_leaked_country_source(self.source_country)

        # info about the nodes reachable
        self._view._txt_result.controls.append(
            ft.Text(value="Below there are the info regard the nodes reachable")
        )
        for country in country_reachable:
            self._view._txt_result.controls.append(
                ft.Text(value=f"{country}")
            )

        self._view.update_page()

    # this is the control for the second version of the function search_country...
    def search_country_reachable_version_2(self, e):
        self._view._txt_result.clean()
        country_reachable = self._model.search_leaked_country_source_version_2(self.source_country)

        # info about the nodes reachable
        self._view._txt_result.controls.append(
            ft.Text(value="Below there are the info regard the nodes reachable")
        )
        for country in country_reachable:
            self._view._txt_result.controls.append(
                ft.Text(value=f"{country}")
            )

        self._view.update_page()

    def fill_DDBCountry(self):
        for n in self._model.get_nodes():
            self._view._DDBCountry.options.append(ft.dropdown.Option( key = n.stato,
                                                                      data = n,
                                                                      on_click = self.get_source_country)
        )

    def get_source_country(self, e):
        self.source_country = e.control.data

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
