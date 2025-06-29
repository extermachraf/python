from load_image import ft_load


def main():
    try:
        path = "/home/achraf/42-projects/pythonpicine/day01/ex02/images/"
        path += "image.png"
        print(ft_load(path))
    except Exception as e:
        print("An error occurred while loading the image: ", e)


if __name__ == "__main__":
    main()
