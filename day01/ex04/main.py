from load_image import ft_load
from rotate import zoom_and_rotate

def main():
    try:
        img = ft_load("/home/achraf/42-projects/pythonpicine/images/animal.jpeg")
        zoom_and_rotate(img, 0, 800, 0, 800, 180)
    except Exception as e:
        print("An error occurred while loading the image: ", e)
    
if __name__ == "__main__":
    main()