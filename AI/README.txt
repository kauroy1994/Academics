*************IMPORTANT************
Execute all the commands in a linux terminal
If you want to run in windows install cygwin and then run
python version used 2.7.*
install nltk python library before starting the process using:
sudo pip install -U nltk
^^^try without sudo first because sudo will require password
*************IMPORTANT************
Extract the lviMain zip folder and enter it
1. To get preprocessing, run the command same as before:
   navigate to the lvi folder using cd lvi and then run:
   java -jar Tool.java docs500 -truth
2. Generating examples for training:
	To generate positive and negative examples run:
	java -jar Tool.jar docs500 <target> <exampleType>
	^^ Here target can be "primary" or "secondary" (without quotes)
	   and exampleType can be "positive" or "negative" (without quotes)
	Example: java -jar Tool.jar docs500 primary positive
3. Redirect output of the command in step 2 to an output file like so:
	Example: java -jar Tool.jar docs500 primary positive > posEx.txt
	similarly for negative redirect to negEx.txt
	DO NOT USE ANY OTHER FILE NAME OTHER THAN posEx.txt and negEx.txt
	You can, in a new terminal window open the files to check progress using the command:
	Example: tail -f posEx.txt
4. Move the txt files both posEx.txt and negEx.txt to the nlpUnit folder using the command:
	mv posEx.txt negEx.txt ../nlpUnit/
5. Generating training files:
	To generate training files navigate to the nlpUnit folder using:
	cd ../nlpUnit/
	and then run the command:
	python makeTrainPredicates.py
6. Navigate to RDN-Boost folder using command:
	cd RDN-Boost
7. Run the following command for training the model:
	java -jar RDNBoost-w2v-adv.jar -l -train data/train -target sentenceContainsTarget -trees 25 -aucJarPath . > trainOutput.txt 2>&1 &
	Can check progress on training in the trainOutput.txt file
	the trainOutput.txt file will show Total learning time when done.
8. Navigate back to nlpUnit folder using command:
	cd ..
====================================================TRAINING COMPLETE========================================================================
9. Generating testing files:
	To generate testing files run the command:
	python makeTestPredicates.py
10. Navigate to RDN-Boost folder using command:
	cd RDN-Boost
11. Run the following command for testing the test files against the model learned:
	java -jar RDNBoost-w2v-adv.jar -i -model data/train/models -test data/test/ -target sentenceContainsTarget -trees 25 -aucJarPath . > testOutput.txt 2>&1 &
	Testing is complete when the testOutput.txt file shows Total inference time
12. Now, run the following three commands:
	1. mv data/test/results_sentenceContainsTarget.db ../../nlpUnit/;cd ../../nlpUnit/
	2. sed -i '/^$/d' results_sentenceContainsTarget.db
	3. mv results_sentenceContainsTarget.db Results.db
13. Run python makeResults.py to get final output
14. Output file is called PredictionResults.txt 
