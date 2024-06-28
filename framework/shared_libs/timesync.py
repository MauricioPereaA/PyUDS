from dependencies.CANoe import CANTool
import time, sys, argparse

parser = argparse.ArgumentParser(description='TimeSync Increment')

parser.add_argument('-d', '--delay_ms',
					type=int, 
					metavar='Delay between each increment for TimeSync',
					help='Please specify an int type value for Delay between each increment for TimeSync')

parser.add_argument('-i', '--iterations',
					type=int, 
					metavar='Number of iterations for TimeSync incrementation',
					help='Please specify an int type value, for Number of iterations for TimeSync incrementation')

parser.add_argument('-m', '--message',
					type=str, 
					metavar='Message where TimeSync is transmitted',
					help='Please specify a str type value, containing Message where TimeSync is transmitted')

args = parser.parse_args()

class TimeSync(CANTool):

	def __init__(self, delay_ms=1000, iterations=10, timesync_message='CGM_CAN1_PDU06'):
		CANTool.__init__(self)
		self.delay_ms = float(delay_ms)/1000
		self.iterations = int(iterations)
		self.message = timesync_message

	def set_timesync(self, value=0):
		try:
			self.set_signal('TmSyncMsg', self.message, int(value))
			return True
		except Exception as error:
			print(__name__, type(error).__doc__, error)
			return False
	
	def run(self):
		try:
			for i in range(self.iterations):
				self.set_timesync(i)
				print(__name__, 'TimeSync', i)
				time.sleep(self.delay_ms)
		except Exception as error:
			print(__name__, type(error).__doc__, error)
			return False

ts = TimeSync(delay_ms=args.delay_ms, iterations=args.iterations,
				timesync_message=args.message)
ts.run()