def enforce(*types):

    def decorator(fn):

        def new_func(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)

        return new_func

    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for _ in range(times):
        print(msg)


repeat_msg("hello", '5')


@enforce(float, float)
def divide(a, b):
    print(a / b)


divide('1', '4')
