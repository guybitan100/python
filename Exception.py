while True:
    try:
        number = int(input("What's is your fav number hoss? \n"))
        print(18 / number)
        break
    except ValueError:
        print("Make sure and enter a number.")
    except ZeroDivisionError:
        print("Dont pick zero number")
    except:
        break
    finally:
        print("loop complete")
