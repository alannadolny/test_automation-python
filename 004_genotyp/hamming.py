class Hamming:
    def distance(self, firstStrand, secondStrand):
        if len(firstStrand) != len(secondStrand):
            raise ValueError('Incorrect strands length')
        else:
            distance = 0
            for i in range(0, len(firstStrand)):
                if list(firstStrand)[i] != list(secondStrand)[i]:
                    distance += 1
            return distance


hamming = Hamming()
