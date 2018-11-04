'''
Author: Shawn
Date:	2018-8-8
Description: The implement of visa communications.
'''

import visa
import const

const.KEITHLEY2450='USB0::0x05E6::0x2450::04336741::INSTR';
const.KEITHLEY2400='GPIB0::24::INSTR';

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

class Visa_Bridge:
	def __init__(self): #The init function of the class
		self.rm=visa.ResourceManager()
		self.rlist=self.rm.list_resources()
		self.online_status={'KEITHLEY2450':False,'KEITHLEY2400':False};
		self.check_online()

		self.KEITHLEY2400_INST=None
		self.KEITHLEY2450_INST=None

		self.connect_inst()

		self.inst_init()
		#print("Init OK")


	def check_online(self): #Check the instrument is/not online
		self.rlist=self.rm.list_resources()
		#print(self.rlist)
		if const.KEITHLEY2450 in self.rlist:
			self.online_status['KEITHLEY2450']=True
		else:
			self.online_status['KEITHLEY2450']=False

		if const.KEITHLEY2400 in self.rlist:
			self.online_status['KEITHLEY2400']=True
		else:
			self.online_status['KEITHLEY2400']=False
		
		return self.online_status

	def connect_inst(self):
		if self.online_status['KEITHLEY2450']==True:
		    self.KEITHLEY2450_INST=self.rm.open_resource(const.KEITHLEY2450)
		    print('2450 is connected')
		    print(self.KEITHLEY2450_INST.query('*IDN?'))
		else:
			print('2450 is not online')
		if self.online_status['KEITHLEY2400']==True:
		    self.KEITHLEY2400_INST=self.rm.open_resource(const.KEITHLEY2400)
		    print('2400 is connected')
		    print(self.KEITHLEY2400_INST.query('*IDN?'))
		else:
			print('2400 is not online')

	'''
	Init the Instrument config
	Add Parameters
	'''
	def inst_init(self):
		if self.KEITHLEY2400_INST:
			self.KEITHLEY2400_INST.write('*RST')
			self.KEITHLEY2400_INST.write('SENS:CURR:PROT 1e-6')
			self.KEITHLEY2400_INST.write('SOUR:VOLT 0')
			self.KEITHLEY2400_INST.write('OUTP ON')
		else:
			print('KEITHLEY2400 is down')

		if self.KEITHLEY2450_INST:
			self.KEITHLEY2450_INST.write('*RST')
			self.KEITHLEY2450_INST.write('SOUR:VOLT 0.1')
			self.KEITHLEY2450_INST.write('SOUR:VOLT:ILIM 0.001')
		else:
			print('KEITHLEY2450 is down')

	def gate_test(self,volt=0):
		
		try:
			if self.KEITHLEY2400_INST and self.KEITHLEY2450_INST:
				self.KEITHLEY2400_INST.write('SOUR:VOLT %.4f' %volt)
				sour_curr=float(self.KEITHLEY2450_INST.query('READ?'))
				gate_curr=float(self.KEITHLEY2400_INST.query('READ?').split(',')[1])
				#print(self.KEITHLEY2450_INST.query('READ?'))
				#print(self.KEITHLEY2400_INST.query('READ?').split(',')[1])
				#print(sour_curr,gate_curr)
				if sour_curr and gate_curr:
					return [sour_curr,gate_curr]
				else:
				    return "Meter Error"
			else:
				return "Error Meter"
		except Exception as e:
			return "Meter Error"

			

	def drop_connection(self):
		if self.KEITHLEY2450_INST:
			self.KEITHLEY2450_INST.close()
			self.KEITHLEY2450_INST=None
		
		if self.KEITHLEY2400_INST:
			self.KEITHLEY2400_INST.close()
			self.KEITHLEY2400_INST=None

if __name__ == '__main__':
	x=Visa_Bridge()
	#print(x.check_online())
	x.gate_test(10)
	x.drop_connection()
	
