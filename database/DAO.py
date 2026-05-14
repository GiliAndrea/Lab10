from database.DB_connect import DBConnect
from model.country import Country


class DAO():

    def __init__(self):
        pass

    # this function takes the info from the database and mekes object of type nation
    @staticmethod
    def get_all_nodes(year: int) -> list[Country]:
        cn = DBConnect.get_connection()
        cursor = cn.cursor(dictionary = True)

        query = """select distinct(c.stato), c.statocod 
                from (select c2.state2ab as stato, c2.state2no as statocod, c2.`year` 
	                  from contiguity c2
	                  having c2.`year` = %s or c2.`year` < %s) as c
                order by c.stato"""
        cursor.execute(query, (year, year, ))

        result = []
        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        cn.close()
        return result

    # this function takes the info from the database and mekes object of type nation
    @staticmethod
    def get_all_edges(year: int):
        cn = DBConnect.get_connection()
        cursor = cn.cursor()

        query = """select c.state1ab , c.state2ab, c.`year`, c.conttype
                from contiguity c
                where (c.`year` < %s or c.`year` = %s) 
                and c.conttype = 1 and c.state1ab < c.state2ab"""
        cursor.execute(query, (year, year, ))

        result = []
        for row in cursor:
            # country 1 Abb - country 2 Abb
            result.append([row[0], row[1]])

        cursor.close()
        cn.close()
        return result

