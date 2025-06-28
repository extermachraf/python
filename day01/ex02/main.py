from load_image import ft_load

def main():
    try:
        print(ft_load("/home/achraf/42-projects/pythonpicine/day01/ex02/images/image.png"))
    except Exception as e:
        print("An error occurred while loading the image: ", e)
    
if __name__ == "__main__":
    main()