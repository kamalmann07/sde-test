# SDE Online Assessment

Solution: 
I have used Python to develop my solution. My solution will accept 2 arguments at run time. I have put some validations to ensure program runs smoothly. For example, if more than 2 valid arguments are given then code will generate exceprions. If data inside the input file is not present, then program will raise exception.

Once these validations are met, all the eligible corporate bonds(who are having non-null yield values) will be compared against goverment bonds. For all valid corporate to goverment bond combinations, we will get absolute tensor difference. Out of the possible combinations idenitified in earlier stpes, the combination with minimum tensor difference will be selected and spread_to_benchmark will be calculated for this combination. The data for all such combinations will be given back in form of a json.

Solution can be tested locally using following command:
python sde-test-solution.py 'input_file.json' 'output_test.json'

Complexity:
Though I have tried to reduce run time complexity of program by using caching, it still be around o(n^2) because I could not avoid using nested loop for one operation during algorithm implimentation. Space complexity of the program is O(n).

Docker:
I have put my Dockerfile along with executable file inside "/submissions" folder. Entrypoint has been intialized as executable script. 