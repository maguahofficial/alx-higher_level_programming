#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_listvarble = []
    for ix in range(list_length):
        try:
            divvarble = my_list_1[ix] / my_list_2[ix]
        except TypeError:
            print("wrong type")
            divvarble = 0
        except ZeroDivisionError:
            print("division by 0")
            divvarble = 0
        except IndexError:
            print("out of range")
            divvarble = 0
        finally:
            n_listvarble.append(divvarble)
    return n_listvarble
