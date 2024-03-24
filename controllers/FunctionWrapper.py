class FunctionWrapper:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def __call__(self, *args, **kwargs):
        # Combine the stored arguments with the new arguments
        combined_args = self.args + args
        combined_kwargs = {**self.kwargs, **kwargs}
        self.result = self.func(*combined_args, **combined_kwargs)
        return self.result
