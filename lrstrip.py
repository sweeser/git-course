# Отчистка текста от лишних пробелов в тексте слева и справа

l_message = " name"
r_message = "name "
print(l_message.lstrip())
print(r_message.rstrip())
l_message = l_message.lstrip()
print(l_message)

# Отчистка лишних пробелов с обеих сторон

lr_message = " name "
print(lr_message.strip())