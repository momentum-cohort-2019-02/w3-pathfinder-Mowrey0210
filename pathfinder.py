from PIL import ImageColor, ImageDraw, Image

class Map: 

    def __init__(self, filename):

        self.elevations = []
        with open(filename) as file: 
            for line in file: 
                self.elevations.append([int(height) for height in line.split()])

                """
                Need to append each iteration to as an integer to self.elevations.
                Also need to get max and min for each row.         
                """
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])

    def get_elevation(self, x, y):
        """Switch x and y coordinates for readability           
            Are we flipping the axis?        
        """
        return self.elevations[y][x]


    def get_intensity(self, x, y):
        """Get elevation intensity"""
        return self.get_elevation(x, y) / self.max_elevation * 255
        return (self.get_elevation(x, y) - self.min_elevation) / (
            self.max_elevation - self.min_elevation) * 255



class Draw_map:
    """
    draw map
    """

        # def get_map(self, x, y):

    #     im = Image.new('RGBA', (600,600))

    #     im.getpixel((0,0))

    #     for x in range(600):
    #         for y in range(600)
    #         # how do we insert the intensity into the second tupel located inside the putpixel method?
    #             im.putpixel((x,y), ())


    


    
    




if __name__ == "__main__":
    map_data = Map('elevation_small.txt')
    
    print(map_data.max_elevation)
