from Testcases.TestClass import TestCase

test = TestCase() 					# TestCase Object

test.begin(							# Initialize Test
	test_name='Basic_PyUDS_TestScript'
)						

# Step 1
test.preconditions('step_001')		  # Set preconditions: current_step, signals, enviroment variables, etc...

test.step(
	step_title='extended_session_control', # Step title
	custom='10 03',						   # Custom UDS message
	
	expected={
		'response': 'Positive'		# Expected type response (Positive, Negative or No response)
	}
)

test.end()							# End test case - End logs and save them

