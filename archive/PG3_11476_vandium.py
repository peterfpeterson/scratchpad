PG3_11476 = LoadEventNexus(Filename="PG3_11476_event.nxs")
PG3_11476 = AlignAndFocusPowder(InputWorkspace=PG3_11476,
                                CalFileName='/SNS/PG3/2013_1_11A_CAL/PG3_ILL_d12007_2013_01_09.cal',
                                ResampleX=-3000,TMin=300,TMax=16667, PreserveEvents=False)
