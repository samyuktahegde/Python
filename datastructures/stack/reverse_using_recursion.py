def insert_at_bottom(stack, item):
    if is_empty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insert_at_bottom(stack, item)
        push(stack, temp)

def reverse(stack):
    if not is_empty(stack):
        temp = pop(stack)
        reverse(stack)
        insert_at_bottom(stack, temp)