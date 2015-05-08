import subprocess
import sys

class ProcWrapper:
	def __init__(self, process):
		self.process = process
		self.enc = sys.getdefaultencoding()
		
	def write(self, str):
		self.process.stdin.write((str + "\n").encode(self.enc))
		self.process.stdin.flush()
	
	def read(self):
		return self.process.stdout.readline().decode(self.enc).strip()

def run_test():
	enc = sys.getdefaultencoding()
	
	process = subprocess.Popen(["client.exe"], executable="client.exe", stdin=subprocess.PIPE,
		stdout=subprocess.PIPE)
	print("Client started.")
	
	wrapper = ProcWrapper(process)
	
	first = wrapper.read()
	assert(first == "READY")
	print("Client ready.")
	
	N = 1000
	for i in range(N):
		wrapper.write("REQ")
		number = int(wrapper.read())
		assert(number == i)
		wrapper.write("INC")
	print("Communication complete.", N, "numbers requested and received.")
	
	wrapper.write("QUIT")
	print("QUIT sent, waiting for termination.")
	
	process.wait()
	print("Process terminated.")
	
	print("Test complete.")

if __name__ == "__main__":
	run_test()