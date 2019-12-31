class ShapedList(list):
    def __init__(self, shape : list, default_value=None, *args, **kwargs):
        super().__init__()
        smallest_el = [default_value for i in range(shape[-1])]
        dims = list(shape[:-1])
        for dim_size in dims[::-1]:
            self.clear()
            for _ in range(dim_size):
                self.append(smallest_el.copy())
            smallest_el = self.copy()

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
    sh = (3, 2, 2, 1, 4)
    l = ShapedList(shape=sh, default_value=0.)
    
    print(l.get_shape())
