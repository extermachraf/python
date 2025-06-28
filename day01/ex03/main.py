from load_image import ft_load
from zoom import zoom

def main():
    try:
        img = ft_load("/home/achraf/42-projects/pythonpicine/images/animal.jpeg")
        zoomed = zoom(img, 0, 800, 200, 300)
    except Exception as e:
        print("An error occurred while loading the image: ", e)
    
if __name__ == "__main__":
    main()