from database.DB_connect import DBConnect


class DAO():

    def __init__(self):
        pass

    # this function takes the info from the database and mekes object of type nation
    @staticmethod
    def get_all_nodes():
        cn = DBConnect.get_connection()
        cursor = cn.cursor(dictionary = True)

        query = """"""
        row = cursor.execute(query)

        result = []
        for r in row:
            result.append(r)

        cursor.close()
        cn.close()
        return result

