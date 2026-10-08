probability_a=.03
probability_b_given_a=.99
probability_b_given_not_a=.02
probability_not_a=1-probability_a
probability_b=(probability_b_given_a*probability_a)+(probability_b_given_not_a*probability_not_a)
probability_a_given_b=(probability_b_given_a*probability_a)/probability_b
print(probability_not_a)
print(probability_b)
print(probability_a_given_b)


"""
Answer to the follow-up questions:
The 99% accuracy assumes the subjects have the disease versus a random sample from the public.
The P(A|B) measures the likelihood that the subject has the disease given that the test came back 
positive. This accounts for the false positive rate.
"""
