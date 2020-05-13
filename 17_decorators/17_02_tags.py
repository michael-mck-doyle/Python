'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''


# 1 - adding html tags - decorator practice
def wrap_up(initial_func):
    def wrapper_func():
        print(f"<p>{initial_func()}<p> ...it's a wrap!")
    return wrapper_func()


@wrap_up
def publish(html_input=input("Enter a headline: ")):
    return html_input
