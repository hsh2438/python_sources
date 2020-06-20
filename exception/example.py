try:
    print(1/0)
except:
    print('error')
else:
    print('no error')
finally:
    print('hi')

# >> error
# >> hi

try:
    print(1/1)
except:
    print('error')
else:
    print('no error')
finally:
    print('hi')

# >> error
# >> hi



# specific exception
try:
    x = [10]
    print(x[5])
except ZeroDivisionError:
    print('zero division problem')
except IndexError:
    print('index problem')
except:
    print('no zero division or index problem')

# print error message
try:
    x = [10]
    print(x[5])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)


# custom error
class NotEvenError(Exception):
    def __init__(self):
        super().__init__('not even number')

try:
    x = 3
    if x % 2 != 0:
        raise NotEvenError
    print(x)
except Exception as e:
    print('Exception:', e)
 
