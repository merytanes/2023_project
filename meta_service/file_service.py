import os
#Constans: konstans változó, értéke nem vált.
#FOLDER_PATH = r"D:\Rita\Python\project\movies"

class FileService:
    #folder_path = r"D:\Rita\Python\project\movies"
    meta_folder='meta_daata'
    poster_folder='posters'

    def __init__(self):
        self.create_folders()

    def create_folders(self):
        if not os.path.exists(self.meta_folder):
            os.mkdir(self.meta_folder)
        if not os.path.exists(self.poster_folder):
            os.mkdir(self.poster_folder)

    @staticmethod
    def write_image(image_path, image_url):
        with open(image_path, "wb") as f:
            f.write(image_url.read())

    @staticmethod
    def write_json_data(json_path, data):
        import json
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def get_data_from_folder(folder_path): 
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"A megadott folder: {folder_path} \n NEM létezik")
        
        temp = []
        for item in os.listdir(folder_path):
            temp.append(item[0:-4])

        return temp
        
        
        """try:
            movies = os.listdir(folder_path)
        except Exception as e:
            raise e
        
        return movies
        """


if __name__ == '__main__':
    from config import MOVIES_PATH
    from api_service import ApiService

    test = FileService()
    api = ApiService()

    movies = test.get_data_from_folder(MOVIES_PATH)

    for item in movies:
        movie = api.get_meta_data(item)
        json_path = f"{test.meta_folder}/{item}.json"
        test.write_json_data(data=movie, json_path=json_path)
        image_path = f"{test.poster_folder}/{item}.jpg"
        image_url = api.get_image_url(movie['poster_path'])
        test.write_image(image_path=image_path, image_url=image_url)