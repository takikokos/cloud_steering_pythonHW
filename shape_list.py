class ShapedList(list):
    def __init__(self, shape : list, default_value=None):
        super().__init__()
        if len(shape) == 1:
            for _ in range(shape[0]):
                self.append(default_value)
            return
        for _ in range(shape[0]):
            self.append(ShapedList(shape[1:], default_value))

    def get_shape(self):
        '''
            suppose elements among each axis have same len
        '''
        try:
            res = [len(self)]
        except TypeError:
            return []
        res += ShapedList.get_shape(self[0])
        return res


if __name__ == "__main__":
    sh = (2, 1, 3, 4, 2)
    l = ShapedList(shape=sh, default_value=0)
    print(l)
    print(l.get_shape())
