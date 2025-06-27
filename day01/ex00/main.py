import give_bmi


def main():
    try:
        BMI = give_bmi.give_bmi([2.71, 1.15], [165.3, 38.4])
        print(BMI)
        limit = give_bmi.apply_limit(BMI, 26)
        print(limit)
    except Exception as error:
        print(error)
        
    
if __name__ == "__main__":
    main()