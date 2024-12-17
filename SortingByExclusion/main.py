# lis algorithm

def sort_by_exclusion(words):
    # check if list is empty
    n = len(words)    
    
    # initialise a list all with 1s
    init = [1] * n
        
    for i in range(1,n):
        for j in range(i):
            if words[j] < words[i] and init[i] < init[j] + 1:
                init[i] = init[j]+1
    
    max_init = max(init)
    
    return n - max_init


import codewars_test as test

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@test.describe('Example Tests')
def example_tests():
    
    @test.it('Regular cases')
    def regular_cases():
        
        test.assert_equals(sort_by_exclusion(["M","O","A"]),1, "Remove A")
        test.assert_equals(sort_by_exclusion(["M","O","Q","A"]),1, "Remove A") 
                           
        test.assert_equals(sort_by_exclusion(["M","O","A","C"]),2, "Remove A, C (or M, O)")
        test.assert_equals(sort_by_exclusion(["M","A","O","C"]),2, "Remove A, C (or M, O)") 
        test.assert_equals(sort_by_exclusion(["M","O","Q","A","C"]),2, "Remove A, C") 

        test.assert_equals(sort_by_exclusion(["M","O","A","C","E"]),2, "Remove M, O") 
        test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E"]),3, "Remove A, C, E (or M, O, Q)") 

        test.assert_equals(sort_by_exclusion(["M","O","N","A","C","E"]),3, "Remove M, O, N")
        test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G"]),3, "Remove M, O, Q") 
        test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G","I","K","M"]),3, "Remove M, O, Q")

        test.assert_equals(sort_by_exclusion(["N","M","O","N","A","C","E"]),4, "Remove N, M, O, N") 
        test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G","I","L","K","M"]),4, "Remove M, O, N, K") 
        
        test.assert_equals(sort_by_exclusion(["ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","LION","EAGLE"]),3,"Remove BEE, LION & EAGLE")
        test.assert_equals(sort_by_exclusion(["ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","EAGLE","LION"]),2,"Remove BEE & ZEBRA")
        test.assert_equals(sort_by_exclusion(["FOX","ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","EAGLE","LION","FOX"]),4,"Remove FOX, BEE, ZEBRA & FOX")
                           
        