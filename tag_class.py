class Tag:

    def __init__(self, dictionary=None):

        if dictionary is None:
            self.__dict__ = {'#': 1, 'Type': '', 'Video time [sec]': '', 'Length': '', 'Electrode': '',
                             'Stimulus #': '', 'Stimulus time [sec]': ''}
        else:
            self.__dict__ = dictionary

    def add_item(self):
        last_subj = self.__dict__.get('#')
        self.__dict__.update({'#': last_subj+1})
        # add exception



if __name__ == '__main__':
    t = Tag()
    t.add_item()
    print(t.__dict__)
