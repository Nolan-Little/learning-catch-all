class Ex:
    @property
    def test(self):
        return self.__test

    @property
    def __test(self):
        return "private"

if __name__ == '__main__':
    test = Ex()
    print(test.test)
    print(test.__test)