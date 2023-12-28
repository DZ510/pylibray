from KMPMatch_Alg import KMPMatch


def main():
    kmpobj = KMPMatch("ABC?ABD")
    kmpobj.buildnextarray()
    print(kmpobj.match("BBC ABCDAB ABCDABCDABDE"))



if __name__ == "__main__":
    main()