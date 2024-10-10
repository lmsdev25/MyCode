# опционально чистим глобалсы от _iN-ов (если работаем в интерактивной среде типа Jupyter Notebook)
# %reset -f

# основная загвоздка задачи в том чтобы не использовать слова hello и world нигде, кроме названия самой функции
def HelloWorld(arg):
    return eval(f'{arg}(f"{{list(globals().keys())[-1].replace(\'W\',\', W\')}}!")')
    # return eval(f'{arg}(list(globals().keys())[-1])')   (если нас устраивает вывод HelloWorld)


HelloWorld('print')


# задачка шуточная, но интересная :)
